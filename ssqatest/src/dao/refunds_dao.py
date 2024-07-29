
from ssqaapitest.src.utilities.dbUtility import DBUtility
import random


class RefundsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_refund_from_db(self, qty=1):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}refunds
                 ORDER BY id DESC LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_refund_by_id(self, order_id):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}refunds
                  WHERE ID = {order_id};'''

        return self.db_helper.execute_select(sql)
