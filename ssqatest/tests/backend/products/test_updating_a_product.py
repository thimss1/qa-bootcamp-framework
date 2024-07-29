from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string

import pytest


@pytest.mark.products
@pytest.mark.ecombe29
@pytest.mark.tcid230
def test_update_product_name():
    """
        Test case to verify the functionality of updating a product's name.
    """

    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    product_rs = ProductsAPIHelper().call_create_product(payload)
    product_id = product_rs['id']

    # update the name
    pro_helper = ProductsAPIHelper()
    new_name = generate_random_string(10)
    payload = {"name":new_name }
    pro_helper.call_update_product(product_id,payload)

    # get order information
    new_pro_info = pro_helper.call_get_product_by_id(product_id)

    # verify the new product name is what was updated
    assert new_pro_info['name'] == new_name, f"Updated order status to hoodie"
    assert new_pro_info['name'] == new_name, f"Update  product code to random string did not have " \
                                                         f"correct code in response. Expected: {new_name} Actual:{new_pro_info['name']}"

