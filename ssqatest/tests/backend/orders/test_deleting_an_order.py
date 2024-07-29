import pytest
import logging as logger
import random
from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers


@pytest.mark.orders
@pytest.mark.ecombe60
@pytest.mark.tcid218
def test_deleting_an_order():
    """
        Test case to verify the functionality of deleting an order.
    """

    logger.info("TEST: Delete an order")

    product_dao = ProductsDAO()
    order_api_helper = OrdersAPIHelper()
    generic_order_helper = GenericOrderHelpers()

    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = generic_order_helper.create_order(additional_args=info)
    id_in_db = order_json['id']
    order_api_info = order_api_helper.delete_order(id_in_db)
    assert order_api_info['id'] == id_in_db, f"order not deleted" \
                                                     f"delete order returned 'code={order_api_info['id']}', Expected code = {id_in_db} "


@pytest.mark.orders
@pytest.mark.ecombe61
@pytest.mark.tcid219
def test_deleting_an_order_invalid_id():
    """
       Test case to verify the handling of deleting an order with an invalid ID.
    """

    logger.info("TEST: Delete an order")

    # set random id
    invaid_id = random.randint(1000,2000)
    order_helper =OrdersAPIHelper()
    cust_api_info = order_helper.delete_order(invaid_id,expected_status_code=404)
    assert cust_api_info['code'] == "woocommerce_rest_shop_order_invalid_id", f"Delete order with invalid id , response has bad 'code'." \
                                                            f"Expected: 'woocommerce_rest_shop_order_invalid_id', Actual: '{cust_api_info['code']}'"


