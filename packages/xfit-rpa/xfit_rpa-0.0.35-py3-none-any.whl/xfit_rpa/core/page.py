import logging
import os.path
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List, ClassVar, Callable

from .base import Executable, EventMixin
from .context import XContext
from .module import XModule
from .registry import _ClassMeta
from ..utils.file_util import FileUtil


@dataclass
class XPage(Executable, EventMixin, metaclass=_ClassMeta, register_name="page.base"):
    name: ClassVar[str]
    description: ClassVar[Optional[str]] = None
    url: Optional[str] = None
    monitor_url: Optional[str] = None
    default_params: Dict[str, Any] = field(default_factory=dict)
    runtime_params: Dict[str, Any] = field(default_factory=dict)

    '''request_params: { url: https://xxx.domain.com/path/resource?p1=v1&p2=v2, dateType: daily, startDate: 2025-01-01 }  # 用于存储请求参数，例如API调用等'''
    request_params: Dict[str, Any] = field(default_factory=dict)

    task_modules: List[XModule] = field(default_factory=list)

    def __post_init__(self):
        if not self.url and hasattr(self, '_url'):
            self.url = self._url
        # 钩子函数默认为空列表
        logging.debug(f'============page.__init__ {self.__class__.name}, {self.url}')
        pass

    def add_task_module(self, module: XModule) -> 'XPage':
        self.task_modules.append(module)
        return self

    def execute(self, ctx: XContext):
        # exec_ctx = self._exec_context(ctx)
        exec_ctx = ctx.clone_for_page(self)

        self._before_load(exec_ctx)
        self._load_url(exec_ctx)
        self._after_load(exec_ctx)

        self._before_execute(exec_ctx)
        self._do_execute(exec_ctx)
        self._after_execute(exec_ctx)

    def _exec_context(self, ctx: XContext) -> XContext:
        return XContext(
            page=ctx.page,
            executor=ctx.executor,
            global_params=ctx.global_params,
            default_params={**ctx.default_params, **self.default_params},
            runtime_params={**ctx.runtime_params, **self.runtime_params},
            state=deepcopy(ctx.state),
            current_app=ctx.current_app,
            current_page=self,
            current_module=None
        )

    def _do_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============page._do_execute {self.name}')
        for module in self.task_modules:
            module.execute(ctx)
        pass

    def _before_execute(self, ctx: XContext):
        ctx.executor.logger.debug(
            f'============page.before_execute {self.name}, {self.url}, runtime_params: {ctx.runtime_params}, request_params: {self.request_params}')
        # 执行前睡眠
        ctx.smart_sleep()
        pass

    def _after_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============page.after_execute {self.name}')
        pass

    def _load_url(self, ctx: XContext):
        _url = self._get_url(ctx)
        if _url:
            ctx.executor.logger.debug(f'============page.to_url {_url}')
            if ctx.executor and hasattr(ctx.executor, 'goto_url'):
                ctx.executor.goto_url(_url, ctx)
            else:
                ctx.executor.logger.warning(
                    f'============page.to_url {_url} url is empty or goto method not available.')

    def _before_load(self, ctx: XContext):
        ctx.executor.logger.debug(f'============page.before_load {self.name}, {self.url}')
        self.set_event_handled( False)
        # 在加载页面前执行一些操作
        pass

    def _after_load(self, ctx: XContext):
        ctx.executor.logger.debug(f'============page.after_load {self.name}, {self.url}')
        ctx.smart_sleep(4)
        self.set_event_handled( False)
        # 在加载页面后执行一些操作
        pass

    def _get_url(self, ctx: XContext) -> str:
        return self.url

    def _handle_response(self, ctx: XContext, data_list: List[Dict[str, Any]], file_name=None):
        _rename_rule = ctx.runtime_params.get('rename_rule', file_name)
        if _rename_rule:
            target_name = ctx.format_name_rule(_rename_rule)
            download_dir = ctx.global_params['download_dir']
            if target_name and download_dir:
                new_name = os.path.sep.join([download_dir, target_name])
                FileUtil.write_csv(new_name, data_list)
                ctx.global_params['upload_files'].append(new_name)

    def __repr__(self):
        return f"XPage({self.name}, {self.description}), {self.url})"
