

from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger



class CouponsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_create_coupon(self, payload):
        logger.debug("Calling 'Create Coupon'.")
        return self.woo_api_utility.post('coupons', params=payload, expected_status_code=201)

    def call_retrieve_coupon(self, coupon_id, expected_status_code=200):
        logger.debug(f"Calling retrieve a coupon. Coupon id: {coupon_id}")
        return self.woo_api_utility.get(f'coupons/{coupon_id}', expected_status_code=expected_status_code)

    def call_list_all_coupons(self, payload=None):
        logger.debug("Calling list all coupons.")
        return self.woo_api_utility.get('coupons', params=payload)

    def call_delete_coupon(self, coupon_id, force=True):
        logger.debug(f"Calling list all coupons.")
        return self.woo_api_utility.delete(f'coupons/{coupon_id}', params={"force": force})

    def call_update_coupon(self, coup_id, payload=None):
        return self.woo_api_utility.put(f'coupons/{coup_id}', params=payload)

