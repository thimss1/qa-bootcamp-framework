
import random

from ssqatest.src.utilities.dbUtility import DBUtility


class CouponsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_expired_coupons(self, qty=1):

        sql = f'''SELECT post_id as coupon_id, post_title as coupon_code FROM {self.db_helper.database}.{self.db_helper.table_prefix}postmeta pm 
                  JOIN {self.db_helper.database}.{self.db_helper.table_prefix}posts p ON pm.post_id = p.id
                  WHERE p.post_type = 'shop_coupon' AND pm.meta_key = 'date_expires'
                  AND FROM_UNIXTIME(meta_value) < NOW() LIMIT 100;'''

        coupons = self.db_helper.execute_select(sql)

        return random.sample(coupons, int(qty))

    def get_order_items_details(self, order_item_id):
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_order_itemmeta 
                  WHERE order_item_id = {order_item_id};'''
        rs_sql = self.db_helper.execute_select(sql)
        line_details = dict()
        for meta in rs_sql:
            line_details[meta['meta_key']] = meta['meta_value']

        return line_details

    def get_random_coupon_from_db(self, qty=1):
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                       WHERE post_type = "shop_coupon" LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))
