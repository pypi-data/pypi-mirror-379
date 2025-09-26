from typing import Any, List

from xfit_rpa.core.base import XResponse, XRequest

try:
    import xbot
    import xbot_visual
except ImportError:
    # print("xbot 模块未找到")
    pass


def normalize_response(xbot_response: Any) -> XResponse:
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


def get_xbot_responses(page) -> List[XResponse]:
    raw_responses = xbot_visual.web.browser.get_responses(
        browser=page,
        url="",
        use_wildcard=False,
        resource_type="All"
    )
    return [normalize_response(r) for r in raw_responses]


def start_monitor_network(page: Any, monitor_url='*', use_wildcard=True, resource_type='All'):
    xbot_visual.web.browser.start_monitor_network(
        browser=page,
        url=monitor_url,
        use_wildcard=use_wildcard,
        resource_type=resource_type,
        _block=("main", 2, "开始监听网页请求")
    )
