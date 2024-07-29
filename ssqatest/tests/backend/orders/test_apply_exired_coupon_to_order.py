


import pytest

from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.dao.coupons_dao import CouponsDAO

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.tcid190
@pytest.mark.ecombe66
def test_order_with_expired_coupon_should_fail():
    """
        Test case to verify that creating an order with an expired coupon fails.
    """

    # find a coupon that is expired
    coupon = CouponsDAO().get_expired_coupons(qty=1)
    coupon_code = coupon[0]['coupon_code']

    # try to create order with the expired coupon
    generic_order_helper = GenericOrderHelpers()

    coupon_data = {"coupon_lines": [{"code": coupon_code}]}
    rs_order = generic_order_helper.create_order(additional_args=coupon_data, expected_status_code=400)

    assert rs_order['code'] == 'woocommerce_rest_invalid_coupon', \
            f"Creating order with expired coupon. 'code' field in response is not as expected." \
            f"Expected: 'woocommerce_rest_invalid_coupon', Actual: {rs_order['code']}"

    assert rs_order['message'] == 'This coupon has expired.', \
        f"Creating order with expired coupon. 'message' field in response is not as expected." \
        f"Expected: 'This coupon has expired.', Actual: {rs_order['code']}"

    assert rs_order['data']['status'] == 400, \
        f"Creating order with expired coupon. 'status' field in response is not as expected." \
        f"Expected: 400, Actual: {rs_order['data']['status']}"
