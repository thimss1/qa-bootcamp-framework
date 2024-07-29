
import os

from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility


class OrdersAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def call_create_order(self, payload, expected_status_code=201):
        return self.woo_api_utility.post('orders', params=payload, expected_status_code=expected_status_code)

    def call_update_an_order(self, order_id, payload):
        return self.woo_api_utility.put(f'orders/{order_id}', params=payload)

    def call_retrieve_an_order(self, order_id, expected_status_code=200):
        return self.woo_api_utility.get(f"orders/{order_id}", expected_status_code=expected_status_code)

    def delete_order(self, order_id,expected_status_code=200):
        return self.woo_api_utility.delete(f'orders/{order_id}', expected_status_code=expected_status_code)

    def call_create_order_note(self,order_id, payload, expected_status_code=201):
        return self.woo_api_utility.post(f'orders/{order_id}/notes', params=payload, expected_status_code=expected_status_code)

    def call_retrieve_an_order_note(self,order_id, note_id,expected_status_code=200):
        return self.woo_api_utility.get(f"orders/{order_id}/notes/{note_id}", expected_status_code=expected_status_code)

    def delete_order_note(self, order_id,note_id,expected_status_code=200,force=True):
        return self.woo_api_utility.delete(f'orders/{order_id}/notes/{note_id}', expected_status_code=expected_status_code, params={"force": force})