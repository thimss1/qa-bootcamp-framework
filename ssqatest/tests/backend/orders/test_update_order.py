
from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
from ssqatest.src.utilities.genericUtilities import generate_random_string

import pytest

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.parametrize("new_status",
                         [
                             pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke,pytest.mark.ecombe55]),
                             pytest.param('completed', marks=[pytest.mark.tcid56,pytest.mark.ecombe56]),
                             pytest.param('on-hold', marks=[pytest.mark.tcid57,pytest.mark.ecombe57]),
                         ])
def test_update_order_status(new_status):
    """
        Test case to verify the update of an order's status.

        Args:
             new_status

        """
    # create new order
    generic_order_helper = GenericOrderHelpers()
    if new_status == 'completed':
        # by default the order is supposed to be 'pending' according to the documentation
        # but it is setting it to 'completed' so for the 'completed' test specifying the status to
        # make the test valid
        order_json = generic_order_helper.create_order({'status': 'pending'})
    else:
        order_json = generic_order_helper.create_order()
    cur_status = order_json['status']
    assert cur_status != new_status, f"Current status of order is already {new_status}. " \
                                     f"Unable to run test."

    # update the status
    order_id = order_json['id']
    payload = {"status": new_status}
    order_helper = OrdersAPIHelper()
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to '{new_status}'," \
          f"but order is still '{new_order_info['status']}'"


@pytest.mark.ecombe58
@pytest.mark.tcid58
@pytest.mark.ecombe58
def test_update_order_status_to_random_string():
    """
        Test case to verify the update of an order's status to a random string fails.
    """
    new_status = 'abcdefg'

    # create new order
    # order_helper = OrdersAPIHelper()
    # order_json = order_helper.call_create_order()

    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']

    # update the status
    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', f"Update order status to random string did not have " \
         f"correct code in response. Expected: 'rest_invalid_param' Actual: {rs_api['code']}"

    assert rs_api['message'] == 'Invalid parameter(s): status',  f"Update order status to random " \
     f"string did not have correct messge in response. " \
     f"Expected: 'rest_invalid_param' Actual: {rs_api['message']}"


@pytest.mark.tcid59
@pytest.mark.ecombe59
def test_update_order_customer_note():
    """
        Test case to verify the update of an order's customer note.

    """
    order_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()

    order_json = generic_order_helper.create_order()
    order_id = order_json['id']

    rand_string = generate_random_string(40)
    payload = {"customer_note": rand_string}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    assert new_order_info['customer_note'] == rand_string, f"Update order's 'customer_note' field," \
       f"failed. Expected: {rand_string}, Actual: {new_order_info['customer_note']}"