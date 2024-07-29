import pytest
import logging as logger
import random
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string


@pytest.mark.products
@pytest.mark.ecombe25
@pytest.mark.tcid28
def test_deleting_a_product():
    """
        Test case to verify the functionality of deleting a product.
    """

    logger.info("TEST: Delete a product")

    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the call
    product_rs = ProductsAPIHelper().call_create_product(payload)
    product_id = product_rs['id']

    pro_helper = ProductsAPIHelper()
    pro_api_info = pro_helper.call_delete_product(product_id)
    assert pro_api_info['id'] == product_id, f"delete product not successful" \
                                                    f"delete product returned 'code={pro_api_info['code']}', Expected code = {product_id} "


@pytest.mark.products
@pytest.mark.ecombe26
@pytest.mark.tcid223
def test_deleting_a_product_invalid_id():
    """
        Test case to verify the handling of deleting a product with an invalid ID.
    """

    logger.info("TEST: Delete a non-existent customer")

    invalid_id = random.randint(1000,2000)
    pro_helper = ProductsAPIHelper()
    pro_api_info = pro_helper.call_delete_product(invalid_id,expected_status_code=404)
    assert pro_api_info['code'] == "woocommerce_rest_product_invalid_id", f"Delete product with invalid id , response has bad 'code'." \
                                                                    f"Expected: 'woocommerce_rest_product_invalid_id', Actual: '{pro_api_info['code']}'"


