from typing import Dict, Any

import yaml

from xfit_rpa.core import XApp, XPage, XModule, XAction
from xfit_rpa.core.builder import XBuilder
from xfit_rpa.core.context import XContext
from xfit_rpa.config import ConfigLoader


# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class XEngine:
    def __init__(self, page, executor):
        self.page = page
        self.executor = executor
        self.logger = executor.get_logger()
        self.config = {}
        # self.logger = logging.getLogger("XEngine")

    def get_global_params(self):
        return self.config.get('global_params', {})

    def load_yaml_config(self, yaml_file_path: str):
        conf_loader = ConfigLoader(yaml_file_path)
        self.config = {
            **conf_loader.config_data,
            'global_params': conf_loader.get_global_params(),
            'account_list': conf_loader.account_list
        }
        # with open(yaml_file_path, 'r', encoding='utf-8') as f:
        #     self.config = yaml.safe_load(f)
        return self.config

    def run_from_yaml_config(self, yaml_file_path: str):
        self.load_yaml_config(yaml_file_path)

        return self.run_from_dict_config(self.config)

    def run_from_dict_config(self, cfg: Dict[str, Any]):
        apps = XBuilder.build_all(cfg)
        global_params = cfg.get('global_params', {})
        for account in cfg.get('account_list', []):
            ctx = XContext(
                page=self.page,
                executor=self.executor,
                logger=self.logger,
                global_params={**global_params, 'account': account},
                current_app=None
            )
            for app in apps:
                ctx.current_app = app
                self.run_app(app, ctx)

    def run_app(self, app: 'XApp', ctx: XContext = None):
        if ctx is None:
            ctx = XContext(
                page=self.page,
                executor=self.executor,
                logger=self.logger,
                current_app=app
            )
        # ctx.set("executor", self.executor)
        # ctx.set("engine", self)
        if hasattr(app, "execute"):
            return app.execute(ctx)

    def _run_app(self, app: XApp, parent_ctx: XContext):
        for page in app.task_pages:
            try:
                page.execute(parent_ctx)
            except Exception as e:
                self.logger.error(f'============app.page.execute {page} error: {e}')
            finally:
                pass

    def _run_page(self, page: XPage, parent_ctx: XContext):
        ctx = parent_ctx.clone_for_page(page)
        self.logger.info(f"Running page: {page.name}")
        ctx.smart_sleep()

        for module in page.task_modules:
            try:
                self._run_module(module, ctx)
            except Exception as e:
                self.logger.error(f"Module {module.name} failed: {e}")

    def _run_module(self, module: XModule, parent_ctx: XContext):
        ctx = parent_ctx.clone_for_module(module)
        self.logger.info(f"Running module: {module.name}")
        for action in module.actions:
            self._run_action(action, ctx)

    def _run_action(self, action: XAction, ctx: XContext):
        self.logger.info(f"Running action: {action.name}")
        action.execute(ctx)
