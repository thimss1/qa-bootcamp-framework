
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import os


class ProductTagHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def get_product_tag_id(self, tag_id, expected_status_code=201):
        return self.woo_api_utility.get(f"products/tags/{tag_id}", expected_status_code=expected_status_code)

    def call_create_product_tag(self,payload,expected_status_code=201):
        return self.woo_api_utility.post(f'products/tags', params=payload, expected_status_code=expected_status_code)

    def call_update_product_tag(self, tag_id, payload=None,expected_status_code=200):
        return self.woo_api_utility.put(f'products/tags/{tag_id}', params=payload, expected_status_code=expected_status_code)

    def delete_product_tag(self, tag_id, payload=None, expected_status_code=200):
        return self.woo_api_utility.delete(f'products/tags/{tag_id}', params={"force": True}, expected_status_code=expected_status_code)