from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO

import pytest


@pytest.mark.ecombe119
def test_create_variable_product():
    """
       Test to verify the functionality of creating a variable product.
     """
    # generate some data
    payload = {
        "name": generate_random_string(20),
        'type': "variable",
        'regular_price': "10.99",
        "attributes": [
            {
                "id": 6,
                "position": 0,
                "visible": False,
                "variation": True,
                "options": [
                    "Black",
                    "Green"
                ]
            },
            {
                "name": "Size",
                "position": 0,
                "visible": True,
                "variation": True,
                "options": [
                    "S",
                    "M"
                ]
            }
        ],
        "default_attributes": [
            {
                "id": 6,
                "option": "Black"
            },
            {
                "name": "Size",
                "option": "S"
            }
        ]}

    # make the call
    product_rs = ProductsAPIHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create variable product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create variable product api call response has" \
                                                  f"unexpected name. Expected: {payload['name']}, Actual: {product_rs['name']}"

    # verify the product exists in db
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create variable product, title in db does not match " \
                                                           f"title in api. DB: {db_product['post_title']}, API: {payload['name']}"
