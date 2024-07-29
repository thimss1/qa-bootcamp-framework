from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.dao.customers_dao import CustomersDAO

from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper
from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers

import pytest


@pytest.fixture(scope='module')
def my_orders_smoke_setup():
    product_dao = ProductsDAO()
    generic_order_helper = GenericOrderHelpers()

    # TODO: the product should have price
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    info = {'product_id': product_id,
            'generic_order_helper': generic_order_helper, }

    return info


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.ecombe52
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):
    """
       Test case to verify the creation of a paid order by a guest user.

       Args:
       my_orders_smoke_setup (dict): Information needed for the test.

    """
    generic_order_helper = my_orders_smoke_setup['generic_order_helper']

    customer_id = 0
    product_id = my_orders_smoke_setup['product_id']

    # make the call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = generic_order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    generic_order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.ecombe53
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):
    """
        Test case to verify the creation of a paid order by a newly created customer.

        Args:
            my_orders_smoke_setup

    """
    # create helper objects
    generic_order_helper = my_orders_smoke_setup['generic_order_helper']
    customer_helper = CustomersAPIHelper()

    # make the call
    cust_info = customer_helper.call_create_customer()
    customer_id = cust_info['id']
    product_id = my_orders_smoke_setup['product_id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        "customer_id": customer_id
    }
    order_json = generic_order_helper.create_order(additional_args=info)

    # # verify response
    expected_products = [{'product_id': product_id}]
    generic_order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.ecombe54
def test_create_paid_order_returning_customer(my_orders_smoke_setup):
    """
        Test case to verify the creation of a paid order by a returning  customer.

        Args:
            my_orders_smoke_setup

    """

    # create helper objects
    generic_order_helper = my_orders_smoke_setup['generic_order_helper']

    # make the call
    cust_dao = CustomersDAO()

    existing_cust = cust_dao.get_random_customer_from_db()
    cust_id = existing_cust[0]['ID']
    product_id = my_orders_smoke_setup['product_id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        "customer_id": cust_id
    }
    order_json = generic_order_helper.create_order(additional_args=info)

    # # verify response
    expected_products = [{'product_id': product_id}]
    generic_order_helper.verify_order_is_created(order_json, cust_id, expected_products)
