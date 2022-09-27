#  Copyright (c) 2021 , Aktana, Inc.
#  All Rights Reserved.

from util.db_helper import DBHelper
from util.rundeck_handler import RundeckHandler

import yaml
import requests
from os import path
from pyjavaproperties import Properties
from sqlalchemy import create_engine


# Application configuration.py
class Configuration:
    DEFAULT_CONFIG_FILE = 'app.config.yaml'
    DEFAULT_CONFIG_OVERRIDE = 'app.override.yaml'
    DEFAULT_CONFIG_PATH = 'config'

    def __init__(self, config_file=None, config_path=None):
        self.config_file = config_file if config_file else self.DEFAULT_CONFIG_FILE
        self.config_path = config_path if config_path else self.DEFAULT_CONFIG_PATH
        self.app_config = {}
        # setup application configuration
        if path.exists(path.join(self.config_path, self.config_file)):
            self.app_config = self.load_yaml_config(self.config_file, self.config_path)
        self.override_config = {}

        # setup application override configuration
        if path.exists(path.join(self.config_path, self.DEFAULT_CONFIG_OVERRIDE)):
            self.override_config = self.load_yaml_config(self.DEFAULT_CONFIG_OVERRIDE, self.config_path)

    def customer_configuration(self, customer, environment):
        customer_parameters = {
            'customer': customer,
            'environment': environment
        }

        customer_parameters.update(self.load_custom_config(customer, environment))
        customer_parameters.update(self.setup_from_gradle_properties(customer, environment))
        customer_parameters.update(self.setup_from_gradle_prod_properties(customer))
        customer_parameters.update(self.setup_from_transform_properties(customer, environment))
        customer_parameters.update(self.setup_from_transform_prod_properties(customer))
        customer_parameters.update(self.kettle_postprocessor_file(customer))
        customer_parameters.update(self.r_create_environment_script(customer))

        # General override for local play
        customer_parameters.update(self.setup_from_override_properties(customer))

        return customer_parameters

    def load_custom_config(self, customer, environment):
        custom_config_path = f"{self.config_path}/custom/{customer}"
        config_filename = f"{customer}.config.yaml"
        config_env_filename = f"{customer}-{environment}.config.yaml"
        custom_config = {}
        # Get custom customer configuration
        if path.exists(path.join(custom_config_path, config_filename)):
            custom_config.update(self.load_yaml_config(config_filename, custom_config_path))
        # Get custom customer configuration at environment level
        if path.exists(path.join(custom_config_path, config_env_filename)):
            custom_config.update(self.load_yaml_config(config_env_filename, custom_config_path))
        return custom_config

    def setup_from_gradle_properties(self, customer, environment):
        workspace = self.config_value(self.app_config, ['aktana', 'workspace'])
        workspace = self.config_value(self.override_config, ['aktana', 'workspace'], workspace)

        config_file = f'{workspace}/customer-etl/{customer}/customization/gradle-{environment}.properties'
        config = Properties()
        config.load(open(config_file))
        parameters = {}
        parameters['db_user'] = config['aktloader.user']
        parameters['db_password'] = config['aktloader.password']
        parameters['enginedb'] = config['enginedb']
        parameters['stagedb'] = config['stagedb']
        parameters['copystormdb'] = config['copystormdb']
        parameters['parent_customer'] = config['flyway.placeholders.parentcustomer']
        parameters['timezone'] = config['flyway.placeholders.timezone']

        # DB Host to be extracted from the from aktloader.url
        aktloader_url = config['aktloader.url']
        db_host = aktloader_url.replace('jdbc:mysql://', '')
        db_host = db_host[:db_host.find(':')]
        parameters['db_host'] = db_host
        parameters['db_port'] = '3306'  # Default - Need to be parsed from graddle properties

        parameters['rundeck_url'] = config['rundeck.url']
        parameters['rundeck_project'] = config['rundeck.project']
        parameters['rundeck_token'] = config['rundeck.token']

        # Workaround to match EMD US case scenario
        # To be tested with the API_URL
        if len(config['flyway.placeholders.region']) == 2:
            parameters['region'] = config['flyway.placeholders.region']
        else:
            parameters['region'] = config['flyway.placeholders.region'][:2]

        parameters['country_code'] = config['flyway.placeholders.isocountrycode']

        return parameters

    def kettle_postprocessor_file(self, customer):
        workspace = self.config_value(self.app_config, ['aktana', 'workspace'])
        workspace = self.config_value(self.override_config, ['aktana', 'workspace'], workspace)

        kettle_file_location = f'{workspace}/customer-etl/{customer}/' \
                               f'customization/generated/pubetl/etl_postprocessor.ktr'
        parameters = {}
        if path.exists(kettle_file_location):
            parameters['postprocessor_kettle'] = kettle_file_location
        else:
            parameters['postprocessor_kettle'] = {}
        return parameters

    def r_create_environment_script(self, customer):
        workspace = self.config_value(self.app_config, ['aktana', 'workspace'])
        workspace = self.config_value(self.override_config, ['aktana', 'workspace'], workspace)

        r_create_script = f'{workspace}/customer-etl/src/main/resources/db/migration/custom/' \
                          f'{customer}/R__Create_{customer}_views.sql'
        parameters = {}
        if path.exists(r_create_script):
            parameters['r_create_sql'] = r_create_script
        else:
            parameters['r_create_sql'] = {}
        return parameters

    def setup_from_gradle_prod_properties(self, customer):
        workspace = self.config_value(self.app_config, ['aktana', 'workspace'])
        workspace = self.config_value(self.override_config, ['aktana', 'workspace'], workspace)

        config_file = f'{workspace}/customer-etl/{customer}/customization/gradle-prod.properties'
        config = Properties()
        config.load(open(config_file))

        parameters = {'prod_enginedb': config['enginedb'],
                      'prod_stagedb': config['stagedb'],
                      'prod_copystormdb': config['copystormdb']}

        return parameters

    def setup_from_transform_properties(self, customer, environment):
        workspace = self.config_value(self.app_config, ['aktana', 'workspace'])
        workspace = self.config_value(self.override_config, ['aktana', 'workspace'], workspace)

        transform_file = f'{workspace}/customer-etl/{customer}/customization/' \
                         f'generated/{environment}/transform/aktana_transform.properties'
        config = Properties()
        config.load(open(transform_file))

        parameters = {"api_secret": config['PARTNERAPI_SECRET'],
                      "api_user": config['PARTNERAPI_USERNAME'],
                      "api_password": config['PARTNERAPI_PASSWORD']}

        api_aktana_host = config['ETL_INPUT_DB_HOSTNAME']
        api_aktana_host = api_aktana_host[api_aktana_host.find('.') + 1:]
        parameters["api_aktana_host"] = api_aktana_host
        return parameters

    def setup_from_transform_prod_properties(self, customer):
        workspace = self.config_value(self.app_config, ['aktana', 'workspace'])
        workspace = self.config_value(self.override_config, ['aktana', 'workspace'], workspace)

        transform_file = f'{workspace}/customer-etl/{customer}/customization/' \
                         f'generated/prod/transform/aktana_transform.properties'
        config = Properties()
        config.load(open(transform_file))
        parameters = {"prod_api_secret": config['PARTNERAPI_SECRET'],
                      "prod_api_user": config['PARTNERAPI_USERNAME'],
                      "prod_api_password": config['PARTNERAPI_PASSWORD']}

        return parameters

    def setup_from_override_properties(self, customer):
        parameters = {}
        # If local in initial config then consider for override
        if "local" in self.override_config:
            # Local level parameters for MySQL connection
            parameters.update(self.override_config['local'])
        if "customer" in self.override_config:
            if customer in self.override_config['customer']:
                # Customer level parameters as ssh local port
                parameters.update(self.override_config['customer'][customer])
        return parameters

    def load_yaml_config(self, filename, filepath):
        config_file = f"{filepath}/{filename}"
        with open(config_file, 'r') as stream:
            return yaml.safe_load(stream)

    def config_value(self, config, keys, default_value=None):
        value = None
        node_value = config
        for param in keys:
            if param in node_value:
                node_value = node_value[param]
                value = node_value
        if value is None:
            value = default_value
        return value

    def generate_sql_engine(self, config, db_name):
        url = DBHelper.DB_URL_FORMAT.format(
            user=config['db_user'],
            password=config['db_password'],
            host=config['db_host'],
            port=config['db_port'],
            db=db_name
        )
        return create_engine(url)

    def generate_rundeck(self, config):
        return RundeckHandler(
            host=config['rundeck_url'],
            project=config['rundeck_project'],
            token=config['rundeck_token']
        )

    def swagger_token_environment(self, config):
        region = config['region']
        environment = config['environment']
        customer = config['customer']
        aktana_host = config['api_aktana_host']

        token_url = f'https://{region}dse{environment}.{aktana_host}:443/{customer}/api/v3.0/Token'

        body_uat = dict()
        body_uat['secret'] = config['api_secret']
        body_uat['username'] = config['api_user']
        body_uat['password'] = config['api_password']

        response = requests.post(token_url,
                                 json=body_uat)

        if response.status_code == 200:
            # Byte issue , remove the b' and apostrophe
            token = str(response.content)[2:-1]
        else:
            print(response.status_code)
        return token

    def swagger_token_prod(self, config):
        region = config['region']
        customer = config['customer']
        aktana_host = config['api_aktana_host']

        token_url = f'https://{region}dseprod.{aktana_host}:443/{customer}/api/v3.0/Token'

        body_uat = dict()
        body_uat['secret'] = config['prod_api_secret']
        body_uat['username'] = config['prod_api_user']
        body_uat['password'] = config['prod_api_password']

        response = requests.post(token_url,
                                 json=body_uat)

        if response.status_code == 200:
            # Byte issue , remove the b' and apostrophe
            token = str(response.content)[2:-1]
        else:
            print(response.status_code)
        return token