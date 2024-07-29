from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers


import pytest


@pytest.mark.ecombe109
def test_update_order_payment_method():
    """
       Test to verify the functionality of updating the payment method of an order.
    """
    order_helper = GenericOrderHelpers()
    order_helper2 = OrdersAPIHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    info = {"payment_method_title": "abcde",
            }

    order_json = order_helper2.call_update_an_order(order_id,payload=info)
    # verify response
    assert order_json['payment_method_title'] == 'abcde', f"update order payment method failed"
