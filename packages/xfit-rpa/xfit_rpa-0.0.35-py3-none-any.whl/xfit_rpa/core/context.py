import logging
import random
import time
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, Type, List, Callable, Union

from xfit_rpa.core import XExecutor

# from xfit_rpa.core import XApp, XPage, XModule, XAction

DEFAULT_FLOW_CONFIG = {
    "min_sleep": 1.0,
    "max_sleep": 3.0,
    "fixed_sleep": None,  # None表示使用随机范围
    "max_retries": 3,
    "retry_delay": 2.0
}


@dataclass
class XContext:
    """RPA 运行时上下文"""
    page: Optional[Any] = None
    executor: Optional[XExecutor] = None
    logger: Optional[Any] = field(default_factory=lambda: logging.getLogger("XContext"))  # 统一日志引用
    # logger: logging.Logger = field(default_factory=lambda: logging.getLogger("XEngine"))

    locator: Optional[Any] = None

    # {account: {}, oss_list: []}
    # 参数池：global 覆盖 default，default 为组件默认值，runtime 为流程运行动态值
    global_params: Dict[str, Any] = field(default_factory=dict)
    default_params: Dict[str, Any] = field(default_factory=dict)
    runtime_params: Dict[str, Any] = field(default_factory=dict)

    # 执行过程中临时状态，例如提取值、断言标记、循环次数等
    state: Dict[str, Any] = field(default_factory=dict)

    # 当前上下文对象，用于 trace
    current_app: Optional[Type['XApp']] = None
    current_page: Optional[Type['XPage']] = None
    current_module: Optional[Type['XModule']] = None

    def __post_init__(self):
        self._init_global_params()

    def _init_global_params(self):
        defaults = {
            "account": {},  # 当前运行账号信息
            "oss_list": [],  # OSS 文件写入缓存
            "download_dir": "",  # 下载目录
            "download_tasks": [],  # 下载任务列表
            "upload_files": [],  # 存储步骤输出结果
            "sync_date": time.strftime("%Y%m%d"),
            "suffix": time.strftime("%H%M%S")
        }
        for key, val in defaults.items():
            if key not in self.global_params or not self.global_params[key]:
                self.global_params[key] = val

    def clone_for_app(self, app: Type['XApp']) -> 'XContext':
        return XContext(
            page=self.page,
            executor=self.executor,
            global_params=self.global_params,
            default_params={**app.default_params, **self.default_params},
            runtime_params={**app.runtime_params, **self.runtime_params},
            current_app=app
        )

    def clone_for_page(self, page: Type['XPage']) -> 'XContext':
        return XContext(
            page=self.page,
            executor=self.executor,
            global_params=self.global_params,
            default_params={**self.default_params, **page.default_params},
            runtime_params={**self.runtime_params, **page.runtime_params},
            state=deepcopy(self.state),
            current_app=self.current_app,
            current_page=page,
            current_module=None
        )

    def clone_for_module(self, module: Type['XModule']) -> 'XContext':
        return XContext(
            page=self.page,
            executor=self.executor,
            global_params=self.global_params,
            default_params={**self.default_params, **module.default_params},
            runtime_params={**self.runtime_params, **module.runtime_params},
            state=deepcopy(self.state),
            current_app=self.current_app,
            current_page=self.current_page,
            current_module=module
        )

    def clone_for_action(self, action: Type['XAction']) -> 'XContext':
        return XContext(
            page=self.page,
            executor=self.executor,
            locator=self.locator,
            global_params=self.global_params,
            default_params={**self.default_params, **action.default_params},
            runtime_params={**self.runtime_params, **action.runtime_params},
            state=deepcopy(self.state),
            current_app=self.current_app,
            current_page=self.current_page,
            current_module=self.current_module
        )

    def get_account_info(self, extra_keys: List[str] = []):
        result = {}
        key_list = extra_keys + ['account_id', 'account_name']
        account_info = self.global_params.get('account', {})
        for key in key_list:
            if key in account_info:
                result[key] = account_info[key]
        return result

    def get_effective_params(self) -> Dict[str, Any]:
        """获取最终生效的参数，优先级: runtime_params > default_params > global_params"""
        return {
            **self.global_params,
            **self.default_params,
            **self.runtime_params
        }

    def get_query_params(self, query_params: List[str] = None) -> Dict[str, Any]:
        """从runtime_params中提取query_params"""
        params = {}
        args = self.get_effective_params()
        query_params = query_params or args.get('query_params', [])
        for key in query_params:
            if key in args:
                params[key] = args[key]

        return params

    def format_name_rule(self, name_rule: Union[Callable[[str, 'XContext', Optional[dict]], str], str],
                         params: dict = None) -> str:
        # logging.debug(f"Formatting name rule: {name_rule}, params: {params}")
        if params is None:
            params = {}
        if callable(name_rule):
            return name_rule(self, params)
        elif isinstance(name_rule, str):
            _params = {**self.get_effective_params(), **params}
            return name_rule.format(**_params)
        else:
            return name_rule

    def get_flow_config(self) -> Dict[str, Any]:
        """从runtime_params中提取控制配置，合并默认值"""
        runtime_params = self.get_effective_params()
        return {
            **DEFAULT_FLOW_CONFIG,
            **runtime_params.get("flow_config", {})
        }

    def smart_sleep(self, base_seconds: float = 0) -> None:
        """智能睡眠方法"""
        import random
        config = self.get_flow_config()
        sleep_time = config["fixed_sleep"] or random.uniform(config["min_sleep"], config["max_sleep"])
        if sleep_time > 0:
            self.executor.logger.debug(f"🕒 Sleeping for {sleep_time + base_seconds:.2f}s...")
            time.sleep(sleep_time + base_seconds)
            # await asyncio.sleep(sleep_time)

    def __repr__(self):
        return f"XContext(app: {self.current_app}, page: {self.current_page}, module: {self.current_module}, runtime_params: {self.runtime_params})"
