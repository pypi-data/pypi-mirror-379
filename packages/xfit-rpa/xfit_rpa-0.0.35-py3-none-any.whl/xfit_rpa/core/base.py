import json
import logging
import sys
import time
from abc import ABC
from dataclasses import dataclass
from functools import wraps
from typing import Dict, Union, Optional, Any, Callable, List
from urllib.parse import urlparse, parse_qs, parse_qsl

from .context import XContext


def is_module_imported(module_name):
    return module_name in sys.modules


def log_execution_time(logger=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            context = next((arg for arg in args if isinstance(arg, XContext)), None)
            if context:
                _logger = context.executor.logger
            else:
                _logger = logger or logging

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            # 模块名
            module_name = func.__module__
            class_name = None

            # 判断是否是绑定方法（self 或 cls）
            if args:
                if hasattr(args[0], '__class__'):  # 实例方法
                    class_name = args[0].__class__.__name__
                elif isinstance(args[0], type):  # 类方法
                    class_name = args[0].__name__

            full_name = f"{module_name}."
            if class_name:
                full_name += f"{class_name}."
            full_name += func.__name__

            msg = f"Execution time for {full_name}: {execution_time:.4f} seconds"
            _logger.info(msg)
            return result

        return wrapper

    return decorator


def with_retry(context_arg: str = 'context'):
    """重试装饰器工厂"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 从参数中获取context
            context = kwargs.get(context_arg) or next((arg for arg in args if isinstance(arg, XContext)), None)

            if not context:
                raise ValueError("Context not found for retry mechanism")

            config = context.get_flow_config()
            last_exception = None

            for attempt in range(1, config["max_retries"] + 1):
                try:
                    result = func(*args, **kwargs)
                    if attempt > 1:
                        context.executor.logger.info(f"✅ Retry succeeded on attempt {attempt}")
                    return result
                except Exception as e:
                    last_exception = e
                    if attempt < config["max_retries"]:
                        wait_time = config["retry_delay"] * attempt
                        context.executor.logger.warning(
                            f"⚠️ Attempt {attempt} failed: {str(e)}. "
                            f"Retrying in {wait_time}s..."
                        )
                        time.sleep(wait_time)
            raise last_exception if last_exception else Exception("Retry failed")

        return wrapper

    return decorator


class Executable(ABC):
    def execute(self, ctx: XContext):
        if not self._should_execute(ctx):
            return
        exec_ctx = self._exec_context(ctx)
        self._before_execute(exec_ctx)
        self._do_execute(exec_ctx)
        self._after_execute(exec_ctx)

    def _should_execute(self, ctx: XContext):
        """是否执行本层逻辑，默认执行"""
        return True

    def _exec_context(self, ctx: XContext):
        return ctx

    def _do_execute(self, ctx: XContext):
        pass

    def _before_execute(self, ctx: XContext):
        """执行前钩子"""
        pass

    def _after_execute(self, ctx: XContext):
        """执行后钩子"""
        pass


@dataclass
class XRequest:
    url: str
    method: str
    headers: Dict[str, str]
    post_data: Optional[Union[str, bytes, Dict]] = None
    resource_type: Optional[str] = None  # "document", "xhr", "fetch" 等
    raw: Any = None

    def json_post_data(self):
        if isinstance(self.post_data, str):
            try:
                return json.loads(self.post_data)
            except json.JSONDecodeError:
                pass
        elif isinstance(self.post_data, bytes):
            try:
                return json.loads(self.post_data.decode())
            except json.JSONDecodeError:
                pass
        return self.post_data

    def json_query_params(self):
        parsed_url = urlparse(self.url)
        query_params = parse_qs(parsed_url.query)
        return {k: v[0] for k, v in query_params.items()}

    def __repr__(self):
        return f"<XRequest {self.method} {self.url}>"


@dataclass
class XResponse:
    url: str
    status: int
    headers: Dict[str, str]
    body: Optional[Union[str, bytes, Dict]] = None
    request: Optional[XRequest] = None  # 关联的请求对象
    raw: Any = None

    def json_body(self):
        if isinstance(self.body, str):
            try:
                return json.loads(self.body)
            except json.JSONDecodeError:
                pass
        elif isinstance(self.body, bytes):
            try:
                return json.loads(self.body.decode())
            except json.JSONDecodeError:
                pass
        return self.body

    def __repr__(self):
        return f"<XResponse {self.url}>"


class EventMixin:
    def __init__(self):
        # self._event_handlers: Dict[str, List[Callable]] = {}
        self._event_handlers: Dict[str, Callable] = {}
        self._event_handled:  bool = False
        self.monitor_url = None

    def register_event(self, event_name: str, handler: Callable[[XContext, Any], None]):
        # if event_name not in self._event_handlers:
        #     self._event_handlers[event_name] = []
        # self._event_handlers[event_name].append(handler)
        self._event_handlers[event_name] = handler

    def unregister_event(self, event_name: str, handler: Callable):
        if event_name in self._event_handlers:
            # self._event_handlers[event_name].remove(handler)
            self._event_handlers.pop(event_name)

    def get_event_handlers(self) -> Dict[str, Callable]:
        return self._event_handlers

    def set_event_handled(self, handled: bool):
        self._event_handled = handled

    def is_event_handled(self) -> bool:
        return self._event_handled or len(self._event_handlers) == 0