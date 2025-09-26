from typing import Any, Dict, Tuple, Callable, Union

from ..core import XExecutor, XAction, ActionType, XContext
from ..core.base import XRequest, XResponse
from ..engine import XEngine

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    # print("xbot 模块未找到")
    pass


class PlaywrightExecutor(XExecutor):
    def __init__(self, ctx: XContext):
        super().__init__()
        self._attached_handlers: Dict[Tuple[Any, str], Callable] = {}

    def normalize_request(self, pw_request: Any, ctx: XContext) -> XRequest:
        return XRequest(
            url=pw_request.url,
            method=pw_request.method,
            headers=pw_request.headers,
            post_data=pw_request.post_data,
            resource_type=pw_request.resource_type,
            raw=pw_request
        )

    def normalize_response(self, pw_response: Any, ctx: XContext) -> XResponse:
        return XResponse(
            url=pw_response.url,
            status=pw_response.status,
            headers=pw_response.headers,
            body=pw_response.body(),  # 注意：可能需要异步处理
            request=self.normalize_request(pw_response.request),
            raw=pw_response
        )

    def on_events(self, page: Any, ctx: XContext):
        handlers = ctx.current_page.get_event_handlers()

        for event_name, handler in handlers.items():
            def wrapped(event_obj, _handler=handler, _event_name=event_name):
                try:
                    unified_event = self.convert_event(event_obj, _event_name, ctx)
                    _handler(ctx, unified_event)
                except Exception as e:
                    print(f"[❌] Error handling event {_event_name}: {e}")

            page.on(event_name, wrapped)
            self._attached_handlers[(page, event_name)] = wrapped

    def off_events(self, page: Any, ctx: XContext):
        # page.wait_for_load_state("load")
        """解绑事件"""
        # handlers = ctx.current_page.get_event_handlers()
        # for event_name, handler in handlers.items():
        #     page.remove_listener(event_name, handler)
        for (pg, event_name), handler in list(self._attached_handlers.items()):
            if pg == page:
                page.remove_listener(event_name, handler)
                del self._attached_handlers[(pg, event_name)]

    def convert_event(self, event_obj: Any, event_name: str, ctx: XContext):
        if event_name == "response":
            return self.normalize_response(event_obj, ctx)
        elif event_name == "request":
            return self.normalize_request(event_obj, ctx)
        return event_obj  # fallback

    def goto_url(self, url: str, ctx: XContext):
        self.on_events(ctx.page, ctx)
        ctx.page.goto(url)
        self.off_events(ctx.page, ctx)

    def execute_action(self, action: XAction, ctx: XContext):

        params = ctx.get_effective_params()
        element = self._resolve_locator(action, ctx)
        if action.type is None or action.type == ActionType.CONTAINER:
            return element

        return self._do_action(element, params, action)

    def _resolve_locator(self, action: XAction, ctx: XContext) -> 'Locator':
        method_name = action.selector.get("method") or "locator"

        if method_name == "label" or method_name == "get_by_label":
            return ctx.page.get_by_label(action.selector)
        elif method_name == "role" or method_name == "get_by_role":
            return ctx.page.get_by_role(**action.selector.get("value"))
        elif method_name == "locator":
            return ctx.page.locator(action.selector.get("value"))
        else:
            raise ValueError(f"未知 executor_method: {method_name}")

    def _do_action(self, locator, params: dict, action: 'XAction'):
        if hasattr(action, 'type'):
            if action.type == ActionType.CLICK:
                locator.click()
            elif action.type == ActionType.HOVER:
                locator.hover()
            elif action.type == ActionType.FILL:
                locator.fill(params.get("value", ""))
            elif action.type == ActionType.INPUT_VALUE:
                return locator.input_value()
            # ...其他动作...
            elif action.type != ActionType.CONTAINER:
                raise NotImplementedError(f"Action type {action.type} not implemented")
            return None
        else:
            raise NotImplementedError(f"Unknown action: {action}")

    def get_elements(self, selector: Union[str, dict], ctx: XContext):
        pass


class PlaywrightEngine(XEngine):
    executor_class = PlaywrightExecutor
