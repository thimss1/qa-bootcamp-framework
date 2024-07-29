
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import os


class RefundsHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def get_refund_by_id(self, refund_id):
        return self.woo_api_utility.get(f"refunds/{refund_id}")

    def call_create_refund(self, ord_id, payload, expected_status_code=201):
        return self.woo_api_utility.post(f'orders/{ord_id}/refunds', params=payload, expected_status_code=expected_status_code)

    def call_update_refund(self, ord_id, payload=None):
        return self.woo_api_utility.put(f'orders/{ord_id}/refunds', params=payload)

    def delete_refund(self, ord_id, refund_id, payload=None):
        return self.woo_api_utility.delete(f'orders/{ord_id}/refunds/{refund_id}?force=true')