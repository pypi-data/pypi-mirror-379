import json
from typing import List

from xfit_rpa.core import XContext, XApp, XPage
from xfit_rpa.core.base import XResponse
from xfit_rpa.utils import build_query_string
from xfit_rpa.utils.date_util import DateRangeParser
from .metadata import deal_summary_url, flow_src_url, compete_shop_analysis_url, compete_shop_compare_url


# 使用示例
class PpzhApp(XApp, register_name="ppzh"):
    name = '品牌商智'
    pass


class PageDealSummary(XPage, register_name="ppzh.brand-deal"):
    name = "交易-交易概况"
    _url = deal_summary_url

    def __post_init__(self):
        super().__post_init__()
        # https://brandsearch.taobao.com/report/query/rptAdvertiserSubListNew.json?r=mx_986&attribution=click&startDate=2025-08-07&endDate=2025-09-01&effectConversionCycle=30&trafficType=%5B1%2C2%2C4%2C5%5D&productId=101005201&csrfID=17567946052770-4026856710653057983


class PageFlowSrc(XPage, register_name="ppzh.flow-src"):
    name = "流量-流量分析-流量来源"
    _url = flow_src_url


class PageCompeteShopAnalysis(XPage, register_name="ppzh.compete-shop"):
    name = "行业-竞争分析-店铺分析"
    _url = compete_shop_analysis_url


class PageCompeteShopCompare(XPage, register_name="ppzh.compete-shop-src"):
    name = "行业-竞争分析-店铺对比"
    _url = compete_shop_compare_url
