from typing import List, Dict, Any

import yaml

from xfit_rpa.utils.crypt_util import decrypt
from xfit_rpa.utils.oss_util import OssUtil


class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config_data = self._load_config()
        self._validate_config()
        self._init_browser()
        self._init_global_params()
        self._init_oss_list()
        self.account_list = self.process_accounts()

    def _load_config(self) -> Dict[str, Any]:
        """Load YAML configuration file"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)


    def _validate_config(self):
        """Validate required configuration sections"""
        # required_sections = ['account_list', 'oss_list', 'global_params']
        # for section in required_sections:
        #     if section not in self.config_data:
        #         raise ValueError(f"Missing required section in config: {section}")

    def _init_global_params(self):
        self.config_data['global_params'] = self.config_data.get('global_params', {})

    def _init_browser(self):
        self.config_data['browser'] = {
            'name': 'chrome',
            **self.config_data.get('browser', {})
        }

    def _init_oss_list(self) -> List['OssUtil']:
        """Initialize OssUtil instances for all OSS configurations"""
        oss_list = []
        oss_configs = self.process_oss_configs()

        for name, config in oss_configs.items():
            oss_instance = OssUtil(
                access_key_id=config['access_key_id'],
                access_key_secret=config['access_key_secret'],
                endpoint=config['endpoint'],
                bucket_name=config['bucket_name'],
                upload_dir=config.get('upload_dir')
            )
            oss_list.append(oss_instance)
        self.config_data['global_params']['oss_list'] = oss_list
        return oss_list

    def decrypt_with_app_key(self, encrypted_value: str) -> str:
        """Decrypt a value using the app_key from global_params"""
        # Implement your decryption logic here
        app_key = self.config_data['global_params'].get('app_key')
        if not app_key:
            # raise ValueError("app_key is missing from global_params")
            return encrypted_value
        try:
            return decrypt(app_key, encrypted_value, self.config_data['global_params'].get('crypt_mode'))
        except Exception as e:
            # self.logger.error(f"Error decrypting value: {e}")
            return encrypted_value

    def process_accounts(self) -> List[Dict[str, Any]]:
        """Process account list, decrypting passwords"""
        accounts = []
        for account in self.config_data.get('account_list', []):
            # Create a copy to avoid modifying original config
            processed = account.copy()
            if 'password' in processed:
                processed['password'] = self.decrypt_with_app_key(processed['password'])
            accounts.append(processed)
        return accounts

    def process_oss_configs(self) -> Dict[str, Any]:
        """Process OSS configurations, decrypting secrets and standardizing params"""
        oss_configs = {}
        for oss in self.config_data.get('oss_list', []):
            # Standardize parameter names and decrypt secrets
            params = oss['params'].copy()

            # Handle different parameter naming conventions
            bucket_name = params.get('bucket_name') or params.get('bucket')

            # Decrypt access keys if present
            if 'access_key_secret' in params:
                params['access_key_secret'] = self.decrypt_with_app_key(params['access_key_secret'])
            # if 'access_key_id' in params:
            #     params['access_key_id'] = self.decrypt_with_app_key(params['access_key_id'])

            oss_configs[oss['name']] = {
                'access_key_id': params.get('access_key_id'),
                'access_key_secret': params.get('access_key_secret'),
                'endpoint': params['endpoint'],
                'bucket_name': bucket_name,
                'upload_dir': params.get('upload_dir')
            }

        # Add to global_params as requested
        # self.config_data['global_params']['oss_configs'] = oss_configs
        return oss_configs

    def get_global_params(self) -> Dict[str, Any]:
        """Get processed global parameters"""
        return self.config_data.get('global_params', {})
