from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper


import pytest


@pytest.mark.ecombe108
def test_update_order_shipping_address():
    """
       Test to verify the functionality of updating the shipping address of an order.
    """
    order_helper = GenericOrderHelpers()
    order_helper2 = OrdersAPIHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    info = {"shipping": {
                    "address_1": "Addis Ababa",
                    "address_2": "",
                    "city": "Addis Ababa",
                    "state": "Addis Ababa",
                    "postcode": "1000",
                    "country": "Ethiopia"
                  }
            }

    # verify response
    rs_api = order_helper2.call_update_an_order(order_id,info)
    assert rs_api, f"update shipping address failed"
