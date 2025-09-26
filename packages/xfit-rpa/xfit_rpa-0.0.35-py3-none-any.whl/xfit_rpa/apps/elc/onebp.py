import logging
import time
import json
from pathlib import Path

from xfit_rpa.core import XContext, XApp, XPage, XModule
from xfit_rpa.utils.date_util import DateRangeParser

app_domain = 'https://one.alimama.com'

try:
    import xbot
    import xbot_visual
except ImportError:
    # print("xbot 模块未找到")
    pass

# 使用示例
class ElcOnebpApp(XApp, register_name="onebp"):
    name = '万相无界'
    pass


class ElcPageContent(XPage, register_name="onebp.content"):
    name = "报表-内容营销"
    _url = 'https://one.alimama.com/index.html#!/report/live_migrate?rptType=live_migrate&bizCode=onebpLive'

    _watch_url = 'https://one.alimama.com/report/query.json'

    def execute(self, ctx: XContext):
        logging.info(f'------============page.execute {self.name}')
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
        self.url = self._url + "&" + "&".join([f"{k}={v}" for k, v in params.items()])
        ctx.current_page.request_params = params
        return self.url

    def _before_load(self, ctx: XContext):
        super()._before_load(ctx)
        # self._monitored_responses = []
        xbot_visual.web.browser.start_monitor_network(
            browser=ctx.page,
            url=f"{self._watch_url}*",
            use_wildcard=True, resource_type="All", _block=("main", 3, "开始监听网页请求")
        )

    def _after_load(self, ctx: XContext):
        super()._after_load(ctx)
        ctx.page.wait_load_completed()

        resp_item = self._wait_for_response(ctx)
        resp_data = self._parse_response(ctx, resp_item)
        ctx.executor.logger.info(resp_data)

        xbot_visual.web.browser.stop_monitor_network(browser=ctx.page, _block=("main", 11, "停止监听网页请求"))

    def _wait_for_response(self, ctx: XContext, timeout=10):
        start = time.time()
        while time.time() - start < timeout:
            response_list = xbot_visual.web.browser.get_responses(
                browser=ctx.page,
                url="",
                use_wildcard=False,
                resource_type="All", _block=("main", 6, "获取网页监听结果")
            )
            if isinstance(response_list, list):
                for loop_item in response_list:
                    # ctx.executor.logger.info(loop_item)
                    # ctx.executor.logger.info(loop_item.get("url"))
                    # ctx.executor.logger.info(loop_item.get("body"))
                    request_body = json.loads(loop_item.get("requestBody", '{}'))
                    if "date" in request_body.get("queryDomains", {}):
                        ctx.executor.logger.debug(loop_item)
                        return loop_item
            time.sleep(0.5)
        raise TimeoutError("No target response detected in time.")

    def _parse_response(self, ctx: XContext, response):
        if not response:
            return None
        try:
            request_body = json.loads(response.get("requestBody", '{}'))
            params = ['bizCode', 'unifyType', 'effectEqual', 'splitType']
            query_params = {k: request_body.get(k) for k in params}

            data = response.get("body", {})
            if isinstance(data, str):
                data = json.loads(data)
            data_list = data.get("data", {}).get("list", [])
            if len(data_list):
                for item in data_list:
                    item.update(query_params)
            return data_list
        except json.JSONDecodeError as e:
            ctx.executor.logger.error(f"JSON decode error: {e}")
            return None


class ElcPageContentSummary(XModule, register_name="onebp.content.summary"):
    name = "数据汇总"
    flow_yaml = str(Path(__file__).parent / "report.content_download_flow.yaml")


class ElcPageContentLive(ElcPageContent, register_name="onebp.content-live"):
    name = "报表-内容营销-直播"
    _url = 'https://one.alimama.com/index.html#!/report/live_migrate?rptType=live_migrate&bizCode=onebpLive'


class ElcPageContentShortVideo(ElcPageContent, register_name="onebp.content-shortVideo"):
    name = "报表-内容营销-短视频"
    _url = 'https://one.alimama.com/index.html#!/report/short_video_migrate?rptType=short_video_migrate&bizCode=onebpShortVideo'


class ElcPageContentUnion(ElcPageContent, register_name="onebp.content-union"):
    name = "报表-内容营销-短直联动"
    _url = 'https://one.alimama.com/index.html#!/report/union_migrate?rptType=union_migrate&bizCode=onebpUnion'

from xfit_rpa.engine import XEngine
#from xfit_rpa.ali import OnebpApp, PageContent
from xfit_rpa.executor.yingdao import YingDaoEngine, YingDaoExecutor

file_path='E:\\workspace\\xfit-python\\x-rpa\\xfit_rpa\\apps\\elc\\onebp.conf.yaml'
executor = YingDaoExecutor()
engine = XEngine(web_page, executor)
engine.run_from_yaml_config(file_path)