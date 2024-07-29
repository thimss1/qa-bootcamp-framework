import random

from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers


import pytest


@pytest.mark.ecombe107
def test_create_order_with_multiple_product():
    """
       Test to verify the functionality of creating an order with multiple products.
    """
    generic_order_helper = GenericOrderHelpers()
    product_dao = ProductsDAO()

    rand_product = product_dao.get_random_product_from_db(2)
    product_id1 = rand_product[0]['ID']
    product_id2 = rand_product[1]['ID']

    customer_id = 0

    info = {"line_items": [
        {
            "product_id": product_id1,
            "quantity": 1
        },
        {
            "product_id": product_id2,
            "quantity": 2
        }
    ],
        "customer_id": customer_id
    }
    order_json = generic_order_helper.create_order(additional_args=info)
    assert order_json, f"create order  with multiple product  failed"
