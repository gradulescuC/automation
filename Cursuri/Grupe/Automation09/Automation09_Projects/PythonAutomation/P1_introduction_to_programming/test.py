# Application configuration.py
from os import path
class Configuration:
    DEFAULT_CONFIG_FILE = 'app.config.yaml'
    DEFAULT_CONFIG_OVERRIDE = 'app.override.yaml'
    DEFAULT_CONFIG_PATH = 'config'

    def __init__(self, config_file=None, config_path=None):
        self.config_file = self.DEFAULT_CONFIG_FILE
        self.config_path = self.DEFAULT_CONFIG_PATH
        self.app_config = {}
        # setup application configuration
        print(path.join(self.config_path, self.config_file))

conf = Configuration()