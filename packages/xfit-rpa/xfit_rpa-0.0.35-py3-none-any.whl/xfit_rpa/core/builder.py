from typing import Dict, Any

from xfit_rpa.core import _ClassMeta
from xfit_rpa.core.action import XAction
from xfit_rpa.core.app import XApp
from xfit_rpa.core.module import XModule
from xfit_rpa.core.page import XPage


class XBuilder:
    @staticmethod
    def build_action(cfg: Dict[str, Any]) -> XAction:
        return XAction(
            name=cfg.get('name', 'unnamed_action'),
            action=cfg.get('action', 'click'),  # 默认 click，可自定义扩展
            selector=cfg.get('selector', ''),
            default_params=cfg.get('default_params', {}),
            runtime_params=cfg.get('params', {})  # params 为运行时参数
        )

    @staticmethod
    def build_module(cfg: Dict[str, Any], app_name: str, page_name: str) -> XModule:
        module_cls = _ClassMeta.get_instance(
            cfg['name'] if '.' in cfg['name'] else f"{app_name}.{page_name}.{cfg['name']}",
            default_params=cfg.get('default_params', {}),
            runtime_params=cfg.get('params', {})
        )
        actions = [XBuilder.build_action(acfg) for acfg in cfg.get('actions', [])]
        module_cls.actions.extend(actions)
        return module_cls

    @staticmethod
    def build_page(cfg: Dict[str, Any], app_name: str) -> XPage:
        page_cls = _ClassMeta.get_instance(
            cfg['name'] if '.' in cfg['name'] else f"{app_name}.{cfg['name']}",
            url=cfg.get('url', ''),
            default_params=cfg.get('default_params', {}),
            runtime_params=cfg.get('params', {})
        )
        for module_cfg in cfg.get('modules', []):
            module = XBuilder.build_module(module_cfg, app_name, cfg['name'])
            page_cls.add_task_module(module)
        return page_cls

    @staticmethod
    def build_app(cfg: Dict[str, Any]) -> XApp:
        app_cls = _ClassMeta.get_instance(
            cfg['name'],
            default_params=cfg.get('default_params', {}),
            runtime_params=cfg.get('params', {})
        )
        for page_cfg in cfg.get('pages', []):
            page = XBuilder.build_page(page_cfg, cfg['name'])
            app_cls.add_task_page(page)
        return app_cls

    @staticmethod
    def build_all(config: Dict[str, Any]):
        """
        根据完整配置构建多个 App，并注入到 engine.apps 中。
        """
        apps = []
        for app_cfg in config.get("apps", []):
            app = XBuilder.build_app(app_cfg)
            apps.append(app)
        return apps
