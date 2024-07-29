from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.utilities.genericUtilities import generate_random_string
import pytest
import random


@pytest.mark.ecombe99
def test_create_order_note():
    """
       Test to verify the functionality of creating an order note.
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
    new_order__note_info = order_helper.call_retrieve_an_order_note(order_id,note_id)
    assert new_order__note_info['note'] == rand_string, f"create order note failed" \
       f"Expected: {rand_string}, Actual: {new_order__note_info['note']}"


@pytest.mark.ecombe100
def test_create_order_note_invalid_order_id():
    """
        Test to verify the handling of creating an order note with an invalid order ID.
     """
    order_helper = OrdersAPIHelper()

    order_id = random.randint(100,200)
    rand_string = generate_random_string(40)
    payload = {"note": rand_string}
    order_note_json = order_helper.call_create_order_note(order_id, payload, expected_status_code=404)

    # get order information
    assert order_note_json['code'] == 'woocommerce_rest_order_invalid_id', f"create order note with invalid id returned wrong code"
