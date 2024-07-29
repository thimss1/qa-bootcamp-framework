import random

from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
import pytest


@pytest.mark.ecombe103
def test_get_all_order_notes():
    """
        Test to verify the functionality of retrieving all order notes for an order.
    """
    req_helper = WooAPIUtility()
    generic_order_helper = GenericOrderHelpers()

    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    rs_api = req_helper.get(woo_endpoint=f'orders/{order_id}/notes')
    assert rs_api, f"Get all order notes end point returned empty response."


@pytest.mark.ecombe104
def test_get_order_note_by_id():
    """
       Test to verify the functionality of retrieving an order note by ID.
    """
    order_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()

    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    rand_string = generate_random_string(40)
    payload = {"note": rand_string}
    order_note_json = order_helper.call_create_order_note(order_id, payload)
    note_id = order_note_json['id']
    # get order information
    new_order__note_info = order_helper.call_retrieve_an_order_note(order_id, note_id)

    # verify the response

    assert new_order__note_info['id'] == note_id, f"Get order note by id failed."


@pytest.mark.ecombe106
def test_get_order_note_by_invalid_id():
    """
        Test to verify the handling of retrieving an order note using an invalid note ID.
"""
    order_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()

    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    note_id = random.randint(200,900)
    new_order__note_info = order_helper.call_retrieve_an_order_note(order_id, note_id,expected_status_code=404)

    # verify the response
    assert new_order__note_info['code'] == 'woocommerce_rest_invalid_id', f"get order note with invalid id , response has bad 'code'."


