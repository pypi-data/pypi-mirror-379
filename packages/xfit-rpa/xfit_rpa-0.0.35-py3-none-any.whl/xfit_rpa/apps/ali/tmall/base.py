import json
from pathlib import Path
from typing import List

from xfit_rpa.core import XContext, XApp, XPage, XModule
from xfit_rpa.core.base import XResponse, XRequest
from xfit_rpa.utils import build_query_string
from .metadata import item_search_url, item_search_request_url


# 使用示例
class TmallApp(XApp, register_name="tmall"):
    name = '天猫'
    pass


class PageItemSearch(XPage, register_name="tmall.item-search"):
    name = "天猫-商品搜索"
    _url = item_search_url

    def __post_init__(self):
        super().__post_init__()
        # https://brandsearch.taobao.com/report/query/rptAdvertiserSubListNew.json?r=mx_986&attribution=click&startDate=2025-08-07&endDate=2025-09-01&effectConversionCycle=30&trafficType=%5B1%2C2%2C4%2C5%5D&productId=101005201&csrfID=17567946052770-4026856710653057983

        self.monitor_url = item_search_request_url
        self.register_event('response', self.on_response)

    def execute(self, ctx: XContext):
        exec_ctx = self._exec_context(ctx)
        _search_list = []
        for _q in _search_list:
            self.runtime_params['q'] = _q
            super().execute(exec_ctx)

    def _get_url(self, ctx: XContext):
        params = ctx.get_query_params()
        self.url = self._url + "&" + build_query_string(params)
        ctx.current_page.request_params = params
        return self.url

    def on_response(self, ctx: XContext, response_list: List[XResponse]):
        ctx.executor.logger.info(f"============page.on_response: {len(response_list)} responses")
        ctx.smart_sleep(15)
        for response in response_list:
            ctx.executor.logger.debug(f"============page.on_response: {response.url}")
            if self.monitor_url in response.url:
                request_body = response.request.json_query_params()
                ctx.executor.logger.debug(f"============page.on_response: {request_body}")
                if self.is_item_search_request(response.request):
                    data_list = self.parse_item_search_response(ctx, response)
                    self.set_event_handled(True)
                    ctx.executor.logger.info(f"============page.request_body: {json.dumps(request_body)} ")
                    ctx.executor.logger.info(
                        f"============page.parse_response: {len(data_list)} data {json.dumps(data_list)}")
                    self._handle_response(ctx, data_list)

    @classmethod
    def parse_item_search_response(cls, ctx: XContext, response: XResponse):
        try:
            request_body = response.request.json_query_params()
            params = {'productId': 'productId'}
            query_params = {alias: request_body.get(k) for k, alias in params.items()}
            query_params.update(ctx.get_account_info())

            data = response.json_body()
            data_list = data.get("data", {}).get("rptQueryResp", {}).get("rptDataDaily", [])
            if len(data_list):
                for item in data_list:
                    item.update(query_params)
            return data_list
        except json.JSONDecodeError as e:
            ctx.executor.logger.error(f"JSON decode error: {e}")
            return None

    @classmethod
    def is_item_search_request(cls, request: XRequest):
        return False


class PageItemSearchContent(XModule, register_name="tmall.item-search.content"):
    name = "天猫-商品搜索-下一页"
    '''通过反复点击下一页获取商品数据'''
    flow_yaml = str(Path(__file__).parent / "tmall.item_search.next_flow.yaml")


class PageItemDetail(XPage, register_name="tmall.item-detail"):
    name = "天猫-商品详情"
    pass
