import json
from pathlib import Path
from typing import List

from xfit_rpa.core import XContext, XApp, XPage, XModule
from xfit_rpa.core.base import XResponse
from xfit_rpa.utils import build_query_string
from xfit_rpa.utils.date_util import DateRangeParser
from .metadata import live_queryFieldIn, short_video_queryFieldIn, union_queryFieldIn, report_live_url, \
    report_short_video_url, report_union_url, page_download_url


# 使用示例
class OnebpApp(XApp, register_name="onebp"):
    name = '万相无界'
    pass


class PageContent(XPage, register_name="onebp.content"):
    name = "报表-内容营销"
    _url = report_live_url
    queryFieldIn = []
    bizCode = ''

    def __post_init__(self):
        super().__post_init__()
        if self.queryFieldIn:
            self.default_params = {
                'queryFieldIn': self.queryFieldIn
            }

        self.monitor_url = 'report/query.json'
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
            for effectEqual in exec_ctx.runtime_params.get('_effectEqual', []):
                self.runtime_params['effectEqual'] = effectEqual
                self.runtime_params['startTime'] = date_range[0]
                self.runtime_params['endTime'] = date_range[1]
                super().execute(exec_ctx)

    def _get_url(self, ctx: XContext):
        params = ctx.get_query_params()
        # self.url = self._url + "&" + "&".join([f"{k}={v}" for k, v in params.items()])
        if params.get('queryFieldIn') and isinstance(params.get('queryFieldIn'), list):
            params['queryFieldIn'] = '["' + '","'.join(params.get('queryFieldIn')) + '"]'

        self.url = self._url + "&" + build_query_string(params)
        ctx.current_page.request_params = params
        return self.url

    def on_response(self, ctx: XContext, response_list: List[XResponse]):
        ctx.executor.logger.info(f"============page.on_response: {len(response_list)} responses")
        for response in response_list:
            if self.monitor_url in response.url:
                request_body = response.request.json_post_data()
                ctx.executor.logger.info(f"============page.on_response: {request_body}")
                if self._is_report_response(request_body):
                    data_list = self._parse_response(ctx, response)
                    self.set_event_handled(True)
                    ctx.executor.logger.info(f"============page.request_body: {json.dumps(request_body)} ")
                    ctx.executor.logger.info(
                        f"============page.parse_response: {len(data_list)} data {json.dumps(data_list)}")
                    self._handle_response(ctx, data_list)
                    # if self.monitor_url in response.get("url", ""):
                    #     request_body = json.loads(response.get("requestBody", '{}'))
                    #     if self._is_report_response(request_body):
                    #         data_list = self._parse_response(ctx, response)
                    #         self.event_handled = True
                    #         ctx.executor.logger.info(f"============page.request_body: {json.dumps(request_body)} ")
                    #         ctx.executor.logger.info(
                    #             f"============page.parse_response: {len(data_list)} data {json.dumps(data_list)}")

    def _parse_response(self, ctx: XContext, response):
        try:
            request_body = response.request.json_post_data()
            params = ['bizCode', 'unifyType', 'effectEqual', 'splitType']
            query_params = {k: request_body.get(k) for k in params}
            query_params.update(ctx.get_account_info())

            data = response.json_body()
            data_list = data.get("data", {}).get("list", [])
            if len(data_list):
                for item in data_list:
                    item.update(query_params)
            return data_list
        except json.JSONDecodeError as e:
            ctx.executor.logger.error(f"JSON decode error: {e}")
            return None

    def _is_report_response(self, request_body):
        if (("date" in request_body.get("queryDomains", {}) and
             request_body.get("splitType") == "day") and
                request_body.get("bizCode") == self.bizCode):
            return True
        return False


class PageContentSummary(XModule, register_name="onebp.content.summary"):
    name = "数据汇总"
    flow_yaml = str(Path(__file__).parent / "report.content_download_flow.yaml")


class PageContentLive(PageContent, register_name="onebp.content-live"):
    name = "报表-内容营销-直播"
    _url = report_live_url

    queryFieldIn = live_queryFieldIn
    bizCode = 'onebpLive'


class PageContentShortVideo(PageContent, register_name="onebp.content-shortVideo"):
    name = "报表-内容营销-短视频"
    _url = report_short_video_url
    queryFieldIn = short_video_queryFieldIn
    bizCode = 'onebpShortVideo'


class PageContentUnion(PageContent, register_name="onebp.content-union"):
    name = "报表-内容营销-短直联动"
    _url = report_union_url
    queryFieldIn = union_queryFieldIn
    bizCode = 'onebpUnion'


class PageDownload(XPage, register_name="onebp.download"):
    name = "报表-下载管理-下载任务管理"
    _url = page_download_url

    def _do_execute(self, ctx: XContext):
        # for download_file, upload_file in self.app_context.get_download_files().items():
        #     self._download_file(download_file, upload_file)
        self._download_file('download_file', 'upload_file')

    def _download_file(self, download_file, upload_file):
        pass
