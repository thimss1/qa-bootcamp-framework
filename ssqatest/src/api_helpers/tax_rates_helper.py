
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger


class TaxHelper(object):

    def __init__(self):
        self.woo_utility = WooAPIUtility()

    def get_tax_rate_by_id(self, tax_id):
        return self.woo_utility.get(f"taxes/{tax_id}")

    def call_create_tax_rate(self, payload):
        return self.woo_utility.post('taxes', params=payload, expected_status_code=201)

    def call_update_tax_rate(self, tax_id, payload=None):
        return self.woo_utility.put(f'taxes/{tax_id}', params=payload)

    def delete_tax_rate(self, tax_id, payload=None,expected_status_code=201):
        return self.woo_utility.delete(f'taxes/{tax_id}', params={"force": True},expected_status_code=expected_status_code)