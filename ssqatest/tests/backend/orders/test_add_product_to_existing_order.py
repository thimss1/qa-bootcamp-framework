from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.dao.products_dao import ProductsDAO


import pytest


@pytest.mark.ecombe105
def test_add_product_to_existing_order():
    """
        Test to verify the functionality of adding a product to an existing order.
    """
    order_helper = OrdersAPIHelper()
    product_dao = ProductsDAO()
    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    payload = {"line_items": [
                {
                  "product_id": product_id,
                  "quantity": 1
                }
              ]}
    rs_api = order_helper.call_update_an_order(order_id,payload)
    assert rs_api, f"add product to order failed "
