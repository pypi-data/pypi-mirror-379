import logging
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List, ClassVar, Callable

import yaml

from .action import XAction
from .base import Executable, EventMixin
from .context import XContext
from .registry import _ClassMeta


@dataclass
class XModule(Executable, EventMixin, metaclass=_ClassMeta, register_name="module.base"):
    name: ClassVar[str]
    description: ClassVar[Optional[str]] = None
    flow_yaml: ClassVar[Optional[str]] = None
    default_params: Dict[str, Any] = field(default_factory=dict)
    runtime_params: Dict[str, Any] = field(default_factory=dict)
    '''request_params: { dateType: daily, startDate: 2025-01-01 }  # 用于存储请求参数，例如API调用等'''
    request_params: Dict[str, Any] = field(default_factory=dict)

    actions: List[XAction] = field(default_factory=list)

    def __post_init__(self):
        # 钩子函数默认为空列表
        logging.debug(f'============module.__init__ {self.name}')
        self._init_actions()
        if self.flow_yaml:
            self._load_from_yaml(self.flow_yaml)

    def _init_actions(self):
        # self.add_action(XAction()) \
        #     .add_action(XAction()) \
        #     .add_action(XAction())
        pass

    def _load_from_yaml(self, yaml_path: str):
        from pathlib import Path
        abs_yaml_path = Path(yaml_path).resolve()
        # base_dir = Path(__file__).parent
        # print("Base directory for YAML:", base_dir)
        # abs_yaml_path = (base_dir / yaml_path).resolve()
        # abs_yaml_path = yaml_path
        if abs_yaml_path.exists():
            with open(abs_yaml_path, 'r', encoding='utf-8') as f:
                yaml_data = yaml.safe_load(f)
                for action_data in yaml_data['steps']:
                    action = self._parse_action(action_data)
                    self.add_action(action)
        else:
            raise FileNotFoundError(f"YAML file not found: {abs_yaml_path}")
        pass

    def _parse_action(self, action_data: dict) -> XAction:
        """解析动作数据字典"""
        children = action_data.pop('children', [])
        action_type = action_data.pop('action_type', 'base')
        # 拼出注册名称，例如：action.download
        register_name = action_type if '.' in action_type else f"action.{action_type}"

        try:
            action = _ClassMeta.get_instance(register_name, **action_data)
        except Exception:
            action = XAction(**action_data)  # fallback

        # 递归添加子 action
        for child_data in children:
            child = self._parse_action(child_data)
            action.add_child(child)

        # children = action_data.get('children', [])
        # action_data.pop('children', None)  # 移除children字段，避免递归解析时重复
        # action = self.default_action(**action_data)
        # if len(children):
        #     for child_data in children:
        #         child = self._parse_action(child_data)
        #         action.add_child(child)
        return action

    def add_action(self, action: XAction) -> 'XModule':
        self.actions.append(action)
        return self

    def execute(self, ctx: XContext):
        # exec_ctx = self._exec_context(ctx)
        exec_ctx = ctx.clone_for_module(self)

        self._before_execute(exec_ctx)

        # 执行前睡眠
        exec_ctx.smart_sleep()

        self._do_execute(exec_ctx)

        self._after_execute(exec_ctx)

    def _exec_context(self, ctx: XContext):
        return XContext(
            page=ctx.page,
            executor=ctx.executor,
            global_params=ctx.global_params,
            default_params={**ctx.default_params, **self.default_params},
            runtime_params={**ctx.runtime_params, **self.runtime_params},
            state=deepcopy(ctx.state),
            current_app=ctx.current_app,
            current_page=ctx.current_page,
            current_module=self
        )

    def _do_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============module._do_execute {self.name}')
        for action in self.actions:
            action.execute(ctx)

    def _before_execute(self, ctx: XContext):
        ctx.executor.logger.debug(
            f'============module.before_execute {self.name}, runtime_params: {ctx.runtime_params}, request_params: {self.request_params}')
        pass

    def _after_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============module.after_execute {self.name}')
        pass

    def __repr__(self):
        return f"XModule({self.name}, {self.description})"


@dataclass
class XTableModule(XModule, metaclass=_ClassMeta, register_name="module.table"):
    """表格模块，支持行遍历和分页"""
    row_selector: str = "table tr"
    next_selector: Optional[str] = None
    max_pages: Optional[int] = None
    extract_row: Optional[Callable[[Any, XContext], dict]] = None  # 提取数据函数

    actions: List[XAction] = field(default_factory=list)

    def _do_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f"============table_module._do_execute {self.name}")

        results = []
        page_count = 0

        while True:
            rows = ctx.executor.get_elements(self.row_selector, ctx)
            ctx.executor.logger.info(f"Found {len(rows)} rows")

            for row in rows:
                row_ctx = ctx.clone_for_module(self)
                row_ctx.locator = row

                # 提取数据
                if self.extract_row:
                    row_data = self.extract_row(row, row_ctx)
                    results.append(row_data)

                # 执行动作
                for action in self.actions:
                    action.execute(row_ctx)

            # 翻页
            if not self.next_selector:
                break
            if self.max_pages and page_count >= self.max_pages:
                break
            if not ctx.executor.has_next_page(self.next_selector, ctx):
                break

            ctx.executor.goto_next_page(self.next_selector, ctx)
            page_count += 1

        return results
