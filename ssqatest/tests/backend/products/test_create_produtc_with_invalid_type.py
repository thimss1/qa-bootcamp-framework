
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO

import pytest


@pytest.mark.ecombe118
def test_create_product_with_invalid_type():
    """
        Test to verify the functionality of creating a product with an invalid type.
    """
    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "abcde"
    payload['regular_price'] = "10.99"

    # make the call
    product_rs = ProductsAPIHelper().call_create_product(payload,expected_status_code=400)

    assert product_rs['code'] == 'rest_invalid_param', f"Create product api call response has wrong code"



