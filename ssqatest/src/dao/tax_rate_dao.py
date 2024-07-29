
from ssqatest.src.utilities.dbUtility import DBUtility
import random


class TaxDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_tax_rate_from_db(self, qty=1):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_tax_rates
                 ORDER BY tax_rate_id DESC LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_tax_by_id(self, id):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_tax_rates 
                     WHERE tax_rate_id = '{id}';'''
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql
