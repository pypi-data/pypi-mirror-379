import logging
import os
from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List, ClassVar

from .base import Executable
from .context import XContext
from .page import XPage
from .registry import _ClassMeta


@dataclass
class XApp(Executable, metaclass=_ClassMeta, register_name="app.base"):
    name: ClassVar[str]
    description: ClassVar[Optional[str]] = None
    default_params: Dict[str, Any] = field(default_factory=dict)
    runtime_params: Dict[str, Any] = field(default_factory=dict)

    task_pages: List[XPage] = field(default_factory=list)

    def __post_init__(self):
        # 钩子函数默认为空列表
        logging.debug(f'============app.__init__ {self.name}')
        pass

    def add_task_page(self, page: XPage) -> 'XApp':
        self.task_pages.append(page)
        return self

    def execute(self, ctx: XContext):
        # exec_ctx = self._exec_context(ctx)
        exec_ctx = ctx.clone_for_app(self)
        self._before_execute(exec_ctx)
        try:
            self._do_execute(exec_ctx)
        except Exception as e:
            ctx.executor.logger.error(f'============app._do_execute {self.name} error: {e}')
            raise e
        finally:
            pass
        self._after_execute(exec_ctx)
        return self

    def _exec_context(self, ctx: XContext) -> XContext:
        return XContext(
            page=ctx.page,
            executor=ctx.executor,
            global_params=ctx.global_params,
            default_params={**self.default_params, **ctx.default_params},
            runtime_params={**self.runtime_params, **ctx.runtime_params},
            current_app=ctx.current_app
        )

    def _do_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============app._do_execute {self.name}')
        for page in self.task_pages:
            try:
                page.execute(ctx)
                ctx.smart_sleep()
            except Exception as e:
                ctx.executor.logger.error(f'============app.page.execute 111')
                ctx.executor.logger.error(f'============app.page.execute {page} error: {e}')
            finally:
                pass

    def _before_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============app.before_execute {self.name}, runtime_params: {ctx.runtime_params}')
        pass

    def _after_execute(self, ctx: XContext):
        ctx.executor.logger.debug(f'============app.after_execute {self.name}')
        self._upload_to_oss(ctx)
        pass

    def _upload_to_oss(self, ctx: XContext):
        oss_list = ctx.global_params.get('oss_list', [])
        file_list = ctx.global_params.get('upload_files', [])
        for oss_item in oss_list:
            for file_item in file_list:
                ctx.executor.logger.debug(f'============app.upload_to_oss {file_item}')
                object_name = file_item.split(os.path.sep)[-1]
                oss_item.upload_object(object_name, file_item)

    def __repr__(self):
        return f"XApp({self.name}, {self.description}))"
