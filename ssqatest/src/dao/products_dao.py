
from ssqatest.src.utilities.dbUtility import DBUtility
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                  WHERE post_type = "product" LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                  WHERE ID = {product_id};'''

        return self.db_helper.execute_select(sql)

    def get_products_created_after_given_date(self, _date):

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                  WHERE post_type = "product" AND post_date > "{_date}" 
                  LIMIT 10000;'''

        return self.db_helper.execute_select(sql)

    def get_random_products_that_are_downloadable(self, qty=1):
        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts WHERE post_type = 'product' AND id IN 
                      (SELECT post_id FROM {self.db_helper.database}.{self.db_helper.table_prefix}postmeta WHERE meta_key= "_downloadable" AND meta_value = "yes");"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_random_products_that_are_not_on_sale(self, qty=1):

        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts WHERE post_type = 'product' AND id NOT IN 
                    (SELECT post_id FROM {self.db_helper.database}.{self.db_helper.table_prefix}postmeta WHERE `meta_key`="_sale_price");"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_random_products_that_are_on_sale(self, qty=1):

        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts WHERE post_type = 'product' AND id IN 
                    (SELECT post_id FROM {self.db_helper.database}.{self.db_helper.table_prefix}postmeta WHERE `meta_key`="_sale_price");"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_random_variable_products_that_have_image(self, qty=1):

        sql = f"""SELECT p2.id, p2.post_title, p2.post_name FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts p1 
                  JOIN {self.db_helper.database}.{self.db_helper.table_prefix}posts p2
                  ON p1.post_parent = p2.id WHERE p1.post_type = "attachment" AND p1.post_mime_type = "image/jpeg" 
                  AND p2.post_type = "product" AND p2.post_excerpt LIKE "%variable%" GROUP BY p2.id LIMIT 100;"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))