
import os
import logging as logger


class MainConfigs:

    @staticmethod
    def get_base_url():
        base_url = os.environ.get('BASE_URL')
        if base_url:
            return base_url
        else:
            raise Exception("Environment variable 'BASE_URL' is required to be set.")

    @staticmethod
    def get_db_configs():
        DB_PORT = os.environ.get("DB_PORT")
        DB_HOST = os.environ.get("DB_HOST")
        DB_DATABASE = os.environ.get("DB_DATABASE")
        DB_TABLE_PREFIX = os.environ.get("DB_TABLE_PREFIX")

        db_configs = dict()

        if DB_PORT:
            db_configs['port'] = int(DB_PORT)
        else:
            raise Exception("Environment variable 'DB_PORT' must be set.")

        if DB_HOST:
            db_configs['db_host'] = DB_HOST
        else:
            raise Exception("Environment variable 'DB_HOST' must be set.")

        if DB_DATABASE:
            db_configs['database'] = DB_DATABASE
        else:
            raise Exception("Environment variable 'DB_DATABASE' must be set.")

        if DB_TABLE_PREFIX:
            db_configs['table_prefix'] = DB_TABLE_PREFIX
        else:
            raise Exception("Environment variable 'DB_TABLE_PREFIX' must be set.")

        return db_configs

    @staticmethod
    def get_coupon_code(filter):
        if filter.upper() == 'FREE_COUPON':
            return 'SSQA100'
        if filter == '50':
            return 'code50'
        else:
            raise Exception(f"Unknown value for parameter 'filter'. filter={filter}")