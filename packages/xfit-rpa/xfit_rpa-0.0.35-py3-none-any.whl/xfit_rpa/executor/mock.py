from typing import Any
import uuid

from ..core import XExecutor, XAction, ActionType, XContext
from ..engine import XEngine


class MockLocator:
    def locator(self, selector: str, **kwargs: Any):
        print(f"Finding element by selector: {selector}")
        return self

    def find_by_xpath(self, xpath: str):
        print(f"Finding element by XPath: {xpath}")
        return self

    def hover(self):
        print(f"Hovering over")
        return self

    def click(self):
        print(f"Click on element")
        return self

    def fill(self, value: str):
        print(f"Filling {value}")
        return self


class MockPage:
    def goto(self, url):
        print(f"Navigating to {url}")
        return self

    def locator(self, selector):
        print(f"Finding element by selector: {selector}")
        return MockLocator()


class MockExecutor(XExecutor):
    def __init__(self):
        super().__init__()

    def goto_url(self, url: str, context: XContext):
        context.page.goto(url)

    def execute_action(self, action: XAction, context: XContext):
        """执行动作"""
        params = context.get_effective_params()
        element = self._resolve_locator(action, context)

        return self._do_action(element, params, action)

    def _resolve_locator(self, action: 'XAction', context: XContext):
        """解析定位器"""
        if context.locator:
            print(f"Using parent locator: {action}")
        else:
            print(f"Using page locator: {action}")

        return MockLocator()

    def _do_action(self, locator, params: dict, action: 'XAction'):
        """执行具体动作"""
        if not locator:
            raise ValueError("Locator cannot be None")
        if action.type == ActionType.CONTAINER:
            return locator
        elif action.type == ActionType.CLICK:
            locator.click()
        elif action.type == ActionType.HOVER:
            locator.hover()
        elif action.type == ActionType.FILL:
            locator.fill(params['value'])
        elif action.type == ActionType.INPUT_VALUE:
            # 假设这里是获取输入框的值
            return str(uuid.uuid4()).replace("-", "_")
        else:
            raise ValueError(f"Unsupported action type: {action.type}")
        return None


class MockEngine(XEngine):
    executor_class = MockExecutor
