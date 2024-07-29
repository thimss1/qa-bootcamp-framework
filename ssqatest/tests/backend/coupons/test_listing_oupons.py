import random

from ssqatest.src.api_helpers.CouponsAPIHelper import CouponsAPIHelper
from ssqatest.src.dao.coupons_dao import CouponsDAO
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import pytest


@pytest.mark.customers
@pytest.mark.ecombe82
@pytest.mark.tcid4
def test_get_all_coupons():
    """
    Test case to verify the functionality of retrieving all coupons.
    """
    req_helper = WooAPIUtility()
    rs_api = req_helper.get(woo_endpoint='coupons')
    assert rs_api, f"Get all coupons end point returned nothing."\
                   f"Response of list all coupons  is empty."


@pytest.mark.customers
@pytest.mark.ecombe81
@pytest.mark.tcid42
def test_get_coupon_by_id():
    """
        Test case to verify the functionality of retrieving a coupon by its ID.
    """

    # get a copoun (test data) from db
    rand_copoun = CouponsDAO().get_random_coupon_from_db(1)
    rand_coupon_id = rand_copoun[0]['ID']
    rand_coupon_code = rand_copoun[0]['post_title']

    # # make the call
    coup_helper = CouponsAPIHelper()
    rs_api = coup_helper.call_retrieve_coupon(rand_coupon_id)

    # verify the response
    assert rand_coupon_id == rs_api['id'], f"Get coupon by id returned wrong coupon.Expected Id: {rand_coupon_id}" \
                                f"Actual Id: {rs_api['id']},"
    assert rand_coupon_code == rs_api['code'], f"Get coupon by id returned wrong coupon.Expected Id: {rand_coupon_code}" \
                                           f"Actual Id: {rs_api['code']},"


@pytest.mark.coupon
@pytest.mark.ecombe84
@pytest.mark.tcid54
def test_get_coupon_by_invalid_id():
    """
        Test case to verify that  retrieving a coupon using an invalid ID returns the right error.
    """

    rand_coupon_id = random.randint(1000,2000)

    # make the call
    coup_helper = CouponsAPIHelper()
    rs_api = coup_helper.call_retrieve_coupon(rand_coupon_id,expected_status_code=404)

    # verify the response
    assert rs_api['code'] == "woocommerce_rest_shop_coupon_invalid_id", f"get coupon with invalid id , response has bad 'code'." \
                                                                    f"Expected: 'woocommerce_rest_shop_coupon_invalid_id', Actual: '{rs_api['code']}'"



