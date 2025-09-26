import time
from typing import Any, List, Union

from ..core import XExecutor, XAction, ActionType, XContext, XTableAction
from ..core.base import XRequest, XResponse
from ..engine import XEngine

try:
    import xbot
    import xbot_visual
except ImportError:
    # print("xbot 模块未找到")
    pass


class YingDaoExecutor(XExecutor):
    def __init__(self):
        super().__init__()
        try:
            self.logger = xbot.logging
        except Exception as e:
            self.logger.warning(f"YingDaoExecutor 初始化失败: {e}")

    def normalize_request(self, request: Any, ctx: XContext) -> XRequest:
        return super().normalize_request(request, ctx)

    def normalize_response(self, xbot_response: Any, ctx: XContext = None) -> XResponse:
        return XResponse(
            url=xbot_response.get("url"),
            status=xbot_response.get("status_code", 200),
            headers=xbot_response.get("headers", {}),
            body=xbot_response.get("body"),
            request=XRequest(
                url=xbot_response.get("url"),
                method=xbot_response.get("method", "GET"),
                headers=xbot_response.get("requestHeaders", {}),
                post_data=xbot_response.get("requestBody", {}),
                resource_type=xbot_response.get("type")
            ),
            raw=xbot_response
        )

    def get_xbot_responses(self, page, ctx: XContext = None) -> List[XResponse]:
        raw_responses = xbot_visual.web.browser.get_responses(
            browser=page,
            url="",
            use_wildcard=False,
            resource_type="All"
        )
        return [self.normalize_response(r, ctx) for r in raw_responses]

    def on_events(self, target: Any, ctx: XContext, **kwargs):
        _page = ctx.page
        handlers = target.get_event_handlers()
        monitor_url = target.monitor_url
        if handlers:
            self.logger.info(f"Executor.on_events start_monitor_network : {monitor_url}")
            xbot_visual.web.browser.start_monitor_network(
                browser=_page,
                url=f"*{monitor_url}*",
                use_wildcard=True, resource_type="All",
                _block=("main", 2, "开始监听网页请求")
            )
        return True

    def off_events(self, target: Any, ctx: XContext, timeout=60):
        _page = ctx.page
        _page.wait_load_completed()
        """解绑事件"""
        handlers = target.get_event_handlers()
        if not handlers:
            self.logger.info("No event handlers to process")
            return

        self.logger.info(f"Starting continuous event processing: {','.join(handlers.keys())}")

        start_time = time.time()
        while True:
            # 每次循环都重新处理所有事件
            for event_name, handler in handlers.items():
                try:
                    if event_name == "request" or event_name == "response":
                        response_list = self.get_xbot_responses(_page, ctx)
                        handler(ctx, response_list)
                    else:
                        # 其他类型事件的处理逻辑
                        handler(ctx)
                except Exception as e:
                    self.logger.error(f"Error processing event {event_name}: {str(e)}")

            # 检查退出条件
            if target.is_event_handled():
                self.logger.info("All events processed successfully")
                break

            if time.time() - start_time > timeout:
                self.logger.warning(f"Timeout after {timeout} seconds")
                break

            # 控制循环频率（避免CPU占用过高）
            time.sleep(0.5)  # 根据实际需求调整间隔

        # 停止网络监控（如果需要持续监控则移出循环）
        xbot_visual.web.browser.stop_monitor_network(browser=_page)

    def goto_url(self, url: str, ctx: XContext):
        self.on_events(ctx.current_page, ctx)
        ctx.page.navigate(url)
        self.off_events(ctx.current_page, ctx)

    def execute_action(self, action: XAction, ctx: XContext):
        """执行动作"""
        params = ctx.get_effective_params()
        element = self._resolve_locator(action, ctx)
        if action.type is None or action.type == ActionType.CONTAINER:
            return element

        return self._do_action(element, params, action)

    def _execute_table(self, action: 'XTableAction', ctx: XContext):
        pass

    def _resolve_locator(self, action: 'XAction', ctx: XContext):
        method_name = action.selector.get("method") or "find_by_xpath"
        if ctx.locator:
            method = getattr(ctx.locator, method_name)
            return method(action.selector.get("value"))
        else:
            method = getattr(ctx.page, method_name)
            return method(action.selector.get("value"))

    def _do_action(self, locator, params: dict, action: 'XAction'):
        if hasattr(action, 'type'):
            if action.type == ActionType.CLICK:
                locator.click()
            elif action.type == ActionType.HOVER:
                locator.hover()
            elif action.type == ActionType.FILL:
                locator.input(params.get("value", ""))
            elif action.type == ActionType.INPUT_VALUE:
                return locator.get_value()
            # ...其他动作...
            elif action.type != ActionType.CONTAINER:
                raise NotImplementedError(f"Action type {action.type} not implemented")
            return None
        else:
            raise NotImplementedError(f"Unknown action: {action}")

    def get_elements(self, selector: Union[str, dict], ctx: XContext):
        return ctx.page.query_selector_all(selector)


class YingDaoEngine(XEngine):
    executor_class = YingDaoExecutor
