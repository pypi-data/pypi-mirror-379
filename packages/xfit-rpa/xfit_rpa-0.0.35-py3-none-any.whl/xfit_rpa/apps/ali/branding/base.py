import json
from typing import List

from xfit_rpa.core import XContext, XApp, XPage
from xfit_rpa.core.base import XResponse, XRequest
from xfit_rpa.utils import build_query_string
from xfit_rpa.utils.date_util import DateRangeParser
from .metadata import brand_zone_url, brand_zone_monitor, star_shop_url, product_mapping


# 使用示例
class BrandingApp(XApp, register_name="branding"):
    name = '品销宝'
    pass


class PageBrandingReport(XPage, register_name="branding.report"):
    name = "报表-品牌专区"
    _url = brand_zone_url
    productId = '101005201'

    def __post_init__(self):
        super().__post_init__()
        # https://brandsearch.taobao.com/report/query/rptAdvertiserSubListNew.json?r=mx_986&attribution=click&startDate=2025-08-07&endDate=2025-09-01&effectConversionCycle=30&trafficType=%5B1%2C2%2C4%2C5%5D&productId=101005201&csrfID=17567946052770-4026856710653057983

        self.monitor_url = brand_zone_monitor
        self.register_event('response', self.on_response)

    def execute(self, ctx: XContext):
        exec_ctx = self._exec_context(ctx)
        _date_ranges = []
        for val in exec_ctx.runtime_params.get('_date_ranges', []):
            if isinstance(val, str):
                _date_ranges = _date_ranges + DateRangeParser.parse(val)
            elif isinstance(val, list) and len(val) == 2:
                _date_ranges.append(val)
            else:
                pass
        for date_range in _date_ranges:
            for effect in exec_ctx.runtime_params.get('_effect', []):
                self.runtime_params['effect'] = effect
                self.runtime_params['startdate'] = date_range[0]
                self.runtime_params['enddate'] = date_range[1]
                super().execute(exec_ctx)

    def _get_url(self, ctx: XContext):
        params = ctx.get_query_params()
        self.url = self._url + "&" + build_query_string(params)
        ctx.current_page.request_params = params
        return self.url

    def on_response(self, ctx: XContext, response_list: List[XResponse]):
        ctx.executor.logger.info(f"============page.on_response: {len(response_list)} responses")
        for response in response_list:
            ctx.executor.logger.debug(f"============page.on_response: {response.url}")
            if self.monitor_url in response.url:
                request_body = response.request.json_query_params()
                ctx.executor.logger.debug(f"============page.on_response: {request_body}")
                if self._is_report_response(response.request):
                    data_list = self._parse_response(ctx, response)
                    self.set_event_handled( True)
                    ctx.executor.logger.info(f"============page.request_body: {json.dumps(request_body)} ")
                    ctx.executor.logger.info(
                        f"============page.parse_response: {len(data_list)} data {json.dumps(data_list)}")
                    self._handle_response(ctx, data_list)

    def _parse_response(self, ctx: XContext, response):
        try:
            request_body = response.request.json_query_params()
            params = {'productId': 'productId', 'effectConversionCycle': 'effect', 'attribution': 'type'}
            query_params = {alias: request_body.get(k) for k, alias in params.items()}
            query_params['productId'] = product_mapping.get(query_params['productId'], query_params['productId'])
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

    def _is_report_response(self, request: XRequest):
        request_body = request.json_query_params()
        if (request_body.get("startDate") == self.runtime_params.get('startdate') and
                request_body.get("endDate") == self.runtime_params.get('enddate') and
                # request_body.get("attribution") == self.runtime_params.get('type') and
                request_body.get("productId") == self.productId):
            return True
        return False


class PageBrandZone(PageBrandingReport, register_name="branding.brand-zone"):
    name = "报表-品牌专区报表"
    _url = brand_zone_url  ## &effect=30&startdate=2025-08-07&enddate=2025-09-01&isVs=0&platform=all&type=impression
    productId = '101005201'


class PageStarShop(PageBrandingReport, register_name="branding.star-shop"):
    name = "报表-品牌专区报表"
    _url = star_shop_url  ## &effect=30&startdate=2025-08-07&enddate=2025-09-01&isVs=0&platform=all&type=impression
    productId = '101005202'
