import random

from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
import pytest

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.ecombe21
@pytest.mark.tcid24
@pytest.mark.ecombe21
def test_get_all_products_returns_not_empty():
    """
      Test case to verify that the 'get all products' endpoint returns a non-empty response.

    """
    woo_api_helper = WooAPIUtility()
    rs_api = woo_api_helper.get(woo_endpoint='products')
    assert rs_api, f"Get all products end point returned nothing."


@pytest.mark.ecombe22
@pytest.mark.tcid25
@pytest.mark.ecombe22
def test_get_product_by_id():
    """
        Test case to verify the 'get product by id' functionality.

    """
    # get a product (test data) from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # make the call
    product_helper = ProductsAPIHelper()
    rs_api = product_helper.call_get_product_by_id(rand_product_id)
    api_name = rs_api['name']

    # verify the response
    assert db_name == api_name, f"Get product by id returned wrong product. Id: {rand_product_id}" \
                                f"Db name: {db_name}, Api name: {api_name}"


@pytest.mark.ecombe28
def test_get_product_by_invalid_id():
    """
       Test to verify the handling of 'get product by invalid ID'.
    """
    # get a product (test data) from db
    rand_product_id = random.randint(10000, 200000)

    # make the call
    product_helper = ProductsAPIHelper()
    rs_api = product_helper.call_get_product_by_id(rand_product_id)

    # verify the response
    assert rs_api['message'] == 'Invalid ID.', f"Get product by invalid id returned wrong message."

