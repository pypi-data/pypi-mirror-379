from pathlib import Path

from xfit_rpa.core import XContext, XApp, XPage, XModule
from xfit_rpa.utils import build_query_string
from .metadata import invoice_download_url


# 使用示例
class BusinessApp(XApp, register_name="business"):
    name = '阿里妈妈-客户工作台'
    pass


class PageInvoiceApply(XPage, register_name="business.invoice"):
    name = "财务管理-发票中心-发票申请"
    _url = invoice_download_url

    def _get_url(self, ctx: XContext):
        params = ctx.get_query_params()
        self.url = self._url + "&" + build_query_string(params)
        ctx.current_page.request_params = params
        return self.url

    # def _do_execute(self, ctx: XContext):
    #     # for download_file, upload_file in self.app_context.get_download_files().items():
    #     #     self._download_file(download_file, upload_file)
    #     self._download_file('download_file', 'upload_file')
    #
    # def _download_file(self, download_file, upload_file):
    #     pass


class PageInvoiceApplyDownload(XModule, register_name="business.invoice.download"):
    name = "财务管理-发票中心-发票申请-下载"
    flow_yaml = str(Path(__file__).parent / "invoice.download_flow.yaml")