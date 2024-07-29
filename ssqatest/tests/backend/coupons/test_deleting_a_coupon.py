import pytest
import logging as logger
from ssqatest.src.api_helpers.CouponsAPIHelper import CouponsAPIHelper
from ssqatest.src.utilities.genericUtilities import generate_random_coupon_code, generate_random_string
import random


@pytest.mark.coupon
@pytest.mark.ecombe80
@pytest.mark.tcid217
def test_deleting_a_coupon():
    """
       Test case to verify the functionality of deleting a coupon.

       This test case ensures that the delete functionality of the coupon API is working as expected.
    """

    logger.info("TEST: Delete a coupon")

    pct_off = str(random.randint(10, 90)) + ".00"
    coupon_code = generate_random_coupon_code(sufix="code", length=5)

    # get the helper object
    coupon_helper = CouponsAPIHelper()
    # prepare data and call api
    payload = dict()
    payload['code'] = coupon_code
    payload['amount'] = pct_off
    payload['discount_type'] = 'percent'
    rs_coupon = coupon_helper.call_create_coupon(payload=payload)
    coupon_id = rs_coupon['id']

    rs_coupon_2 = coupon_helper.call_retrieve_coupon(coupon_id)
    assert rs_coupon_2['code'] == coupon_code.lower(), f"Create coupon response has wrong 'code'. " \
                                             f"Expected: {coupon_code.lower()}, Actual: {rs_coupon_2['code']}."

    coup_helper = CouponsAPIHelper()
    coup_api_info = coup_helper.call_delete_coupon(coupon_id)
    assert coup_api_info['code'] == rs_coupon_2['code'], f"coupon not deleted"\
                                     f"delete coupon returned 'code={coup_api_info['code']}', Expected code = {rs_coupon_2['code']} "
