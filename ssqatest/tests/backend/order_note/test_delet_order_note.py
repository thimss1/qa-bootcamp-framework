import pytest
import logging as logger
import random
from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.utilities.genericUtilities import generate_random_string


@pytest.mark.ecombe101
def test_delete_order_note():
    """
       Test to verify the functionality of deleting an order note.
    """
    logger.info("TEST: test_delete_order_note")

    order_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()

    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    rand_string = generate_random_string(40)
    payload = {"note": rand_string}
    order_note_json = order_helper.call_create_order_note(order_id, payload)
    note_id = order_note_json['id']
    order_note_info = order_helper.delete_order_note(order_id,note_id)
    assert order_note_info['id'] == note_id, f"order note not deleted"


@pytest.mark.ecombe102
def test_delete_order_note_invalid_id():
    """
        Test to verify the handling of deleting an order note with an invalid note ID.
    """
    order_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    note_id = random.randint(1000, 2000)
    order_note_info = order_helper.delete_order_note(order_id, note_id,expected_status_code=404)
    assert order_note_info['code'] == "woocommerce_rest_invalid_id", f"Delete order note with invalid id , response has bad 'code'."


