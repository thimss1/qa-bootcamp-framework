import random

from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.dao.orders_dao import OrdersDAO
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import pytest


@pytest.mark.orders
@pytest.mark.ecombe62
@pytest.mark.tcid220
def test_get_all_orders():
    """
        Test case to verify the functionality of retrieving all orders.
    """

    req_helper = WooAPIUtility()
    rs_api = req_helper.get(woo_endpoint='orders')
    assert rs_api, f"Get all orders end point returned nothing." \
                   f"Response of list all orders  is empty."


@pytest.mark.orders
@pytest.mark.ecombe63
@pytest.mark.tcid221
def test_get_order_by_id():
    """
        Test case to verify the functionality of retrieving an order by its ID.
    """

    # get an order (test data) from db
    order_dao = OrdersDAO()
    rand_order = order_dao.get_random_order_from_db()
    rand_order_id  = rand_order[0]["order_id"]

    # make the call
    order_helper = OrdersAPIHelper()
    rs_api = order_helper.call_retrieve_an_order(rand_order_id,expected_status_code=200)

    # verify the response

    assert rand_order_id == rs_api['id'], f"Get coupon by id returned wrong coupon.Expected Id: {rand_order_id}" \
                                f"Actual Id: {rs_api['id']},"


@pytest.mark.ecombe64
@pytest.mark.tcid222
def test_get_order_by_invalid_id():
    """
        Test case to verify the handling of retrieving an order with an invalid ID.
    """

    # get a product (test data) from db
    rand_order_id = random.randint(100,200)

    # make the call
    order_helper = OrdersAPIHelper()
    rs_api = order_helper.call_retrieve_an_order(rand_order_id,expected_status_code=404)

    # verify the response
    assert rs_api['message'] == 'Invalid ID.', f"get order with invalid id , response has bad 'code'." \
                                                                     f"Expected: 'woocommerce_rest_shop_coupon_invalid_id', Actual: '{rs_api['message']}'"


