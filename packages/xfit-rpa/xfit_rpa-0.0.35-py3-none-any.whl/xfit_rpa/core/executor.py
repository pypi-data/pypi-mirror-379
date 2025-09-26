import logging
from abc import ABC, abstractmethod
from typing import Any, Union

from .base import XRequest, XResponse
from .context import XContext


# from .page import XPage


# from .action import XAction


class XExecutor(ABC):
    """执行器接口，定义了所有执行器必须实现的方法"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        """获取执行器的日志记录器"""
        return self.logger

    # def do_request(self, method: str, url: str, headers: dict, body: Any, ctx: XContext):

    def normalize_request(self, request: Any, ctx: XContext) -> XRequest:
        raise NotImplementedError

    def normalize_response(self, response: Any, ctx: XContext) -> XResponse:
        """标准化响应"""
        raise NotImplementedError

    def on_events(self, page: Any, ctx: XContext):
        raise NotImplementedError("Each executor must implement `on_events`")

    def off_events(self, page: Any, ctx: XContext):
        raise NotImplementedError("Each executor must implement `off_events`")

    def convert_event(self, event_obj: Any, event_name: str, ctx: XContext) -> Any:
        raise NotImplementedError("Each executor must implement `convert_event`")

    @abstractmethod
    def goto_url(self, url: str, ctx: XContext):
        """跳转到指定的URL"""
        raise NotImplementedError

    @abstractmethod
    def execute_action(self, action: 'XAction', ctx: XContext) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_elements(self, selector: Union[str, dict], ctx: XContext):
        raise NotImplementedError

    def __repr__(self):
        return f"XExecutor({self.__class__.__name__})"
