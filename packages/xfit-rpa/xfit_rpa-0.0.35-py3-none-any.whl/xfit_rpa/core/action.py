import logging
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, Any, Optional, List, Callable, Union

from .base import Executable, with_retry, log_execution_time
from .context import XContext
from .registry import _ClassMeta
from ..utils.file_util import FileUtil


class ActionType(Enum):
    """所有支持的动作类型枚举
    默认是 click，有children默认是容器类型
    """
    CONTAINER = auto()  # 容器类型（仅用于分组）
    CLICK = 'click'  # 点击元素
    HOVER = 'hover'  # 悬停元素
    FILL = 'fill'  # 填写输入框
    INPUT_VALUE = 'input_value'  # 获取输入框值
    # KEY_PRESS = auto()  # 键盘按键
    # SCROLL = auto()  # 滚动到元素
    # WAIT = auto()  # 等待元素

    SCREENSHOT = 'screenshot'  # 截图

    @classmethod
    def from_str(cls, value: str) -> 'ActionType':
        """从字符串转换为枚举值（不区分大小写）"""
        try:
            return cls[value.upper()]
        except KeyError:
            raise ValueError(f"Invalid action type: {value}. Valid types are: {[e.name for e in cls]}")


@dataclass
class XAction(Executable, metaclass=_ClassMeta, register_name="action.base"):
    # action_type: Union[ActionType, str]  # 支持直接传枚举或字符串
    selector: Union[str, dict]
    type: Union[str, ActionType] = 'click'
    action_type: Optional[str] = None
    name: str = ''
    description: Optional[str] = ''
    default_params: Dict[str, Any] = field(default_factory=dict)
    runtime_params: Dict[str, Any] = field(default_factory=dict)
    children: List['XAction'] = field(default_factory=list)  # 子动作

    def __post_init__(self):
        # 钩子函数默认为空列表
        # logging.debug(f'============action.__init__ {self.name}')
        if not self.type:
            self.type = ActionType.CONTAINER
        elif isinstance(self.type, str):
            self.type = ActionType.from_str(self.type)
        if isinstance(self.selector, str):
            self.selector = {type: 'xpath', 'value': self.selector}
        pass

    def add_child(self, action: 'XAction') -> 'XAction':
        """添加子动作并自动设置父选择器"""
        self.children.append(action)
        return self

    @with_retry(context_arg='ctx')
    @log_execution_time()
    def execute(self, ctx: XContext):
        # 创建当前action的执行上下文
        # exec_ctx = self._exec_context(ctx)
        exec_ctx = ctx.clone_for_action(self)

        self._before_execute(exec_ctx)

        # 执行当前动作
        self._do_execute(exec_ctx)

        self._after_execute(exec_ctx)

    def _exec_context(self, ctx: XContext) -> XContext:
        return XContext(
            page=ctx.page,
            executor=ctx.executor,
            locator=ctx.locator,
            global_params=ctx.global_params,
            default_params={**ctx.default_params, **self.default_params},
            runtime_params={**ctx.runtime_params, **self.runtime_params},
            state=deepcopy(ctx.state),
            current_app=ctx.current_app,
            current_page=ctx.current_page,
            current_module=ctx.current_module
        )

    def _do_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============action._do_execute {self.name}')
        if ctx.executor and hasattr(ctx.executor, 'execute_action'):
            result = ctx.executor.execute_action(self, ctx)
            if result:
                self._process_result(result, ctx)

        # 执行子动作
        for child in self.children:
            child.execute(ctx)

    def _process_result(self, result, ctx: XContext):
        ctx.executor.logger.debug(f'============action._process_result {self.name}, {result}, {ctx}')
        if len(self.children):
            ctx.locator = result

    def _before_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============action.before_execute {self.name}, {ctx.runtime_params}')
        # 执行前睡眠
        ctx.smart_sleep()
        pass

    def _after_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============action.after_execute {self.name}')
        pass

    def __repr__(self):
        return f"XAction({self.action_type}, {self.type}, {self.selector}, {self.name}, {len(self.children)} children)"


@dataclass
class XValueAction(XAction, register_name="action.value"):
    """获取输入框值"""
    param_name: str = None  # 输入框值保存的参数名，获取后保留到 module.request_params 或 page.request_params 中

    def _process_result(self, result, ctx: XContext):
        super()._process_result(result, ctx)
        if self.param_name and isinstance(result, str):
            ctx.current_module.request_params[self.param_name] = result


@dataclass
class XDownloadAction(XAction, register_name="action.download"):
    """下载文件动作"""
    name_rule: Optional[Callable[[str, XContext], str]] = None  # 文件名匹配规则
    rename_rule: Optional[Callable[[str, XContext], str]] = None  # 文件命名规则

    # rename_rule = lambda path, ctx: f"{ctx.runtime_params['report_name']}.xlsx"
    # rename_rule = "{report_name}_{date}.xlsx"
    # rename_rule = "{account[brand_code]}_{report_name}_{date}}.csv".format(**data)

    def _before_execute(self, ctx: XContext):
        super()._before_execute(ctx)

    def _after_execute(self, ctx: XContext):
        _name_rule = ctx.runtime_params.get('name_rule', self.name_rule)
        _rename_rule = ctx.runtime_params.get('rename_rule', self.rename_rule)
        download_name = ctx.format_name_rule(_name_rule)
        target_name = ctx.format_name_rule(_rename_rule)
        if download_name:
            download_dir = ctx.global_params['download_dir']
            if target_name:
                new_name = FileUtil.rename_file(download_name, target_name, download_dir)
                ctx.global_params['upload_files'].append(new_name)
            else:
                ctx.global_params['upload_files'].append(download_name)
        super()._after_execute(ctx)


@dataclass
class XDownloadTaskAction(XAction, register_name="action.download_task"):
    """
    下载任务动作，用于下载页面匹配下载文件以及下载后重命名文件
    与 XValueAction 结合使用（如有生成日期/时间/随机数，通过input_value获取），两者确保一致
    或者通过平台文件生成规则直接定义
    """
    name_rule: Optional[Callable[[str, XContext], str]] = None  # 文件名匹配规则
    rename_rule: Optional[Callable[[str, XContext], str]] = None  # 文件命名规则

    def _after_execute(self, ctx: XContext):
        _name_rule = ctx.runtime_params.get('name_rule', self.name_rule)
        _rename_rule = ctx.runtime_params.get('rename_rule', self.rename_rule)
        task_name = ctx.format_name_rule(_name_rule, ctx.current_module.request_params)
        target_name = ctx.format_name_rule(_rename_rule)

        if task_name:
            ctx.global_params['download_tasks'].append({
                'task_name': task_name,
                'target_name': target_name
            })
        super()._after_execute(ctx)


@dataclass
class XTableAction(XAction, register_name="action.table"):
    """
    表格操作动作
    - 遍历表格行，执行 children 动作
    - 支持翻页
    """
    row_selector: Dict[str, Any] = field(default_factory=dict)   # 定位行的规则
    next_page_selector: Optional[Dict[str, Any]] = None          # 翻页按钮
    max_pages: Optional[int] = None                              # 防止死循环

    def is_table_action(self) -> bool:
        return True