import random

import pytest
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.generic_helpers.generic_product_helper import GenericProductHelper


pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.tcid211
@pytest.mark.ecombe68
def test_verify_order_calculates_correct_price_item_not_on_sale():
    """
        Test case to verify that an order calculates the correct price when the item is not on sale.

    """
    # create new product that not on sale
    generic_product_helper = GenericProductHelper()
    product_info = generic_product_helper.create_a_product()

    # just to be sure verify product is not on sale
    assert not product_info['on_sale'], f"Product must not be 'on_sale' for this test to be valid."

    product_id = product_info['id']
    product_price = product_info['regular_price']

    # create order using the newly created product
    generic_order_helper = GenericOrderHelpers()
    line_items = [{"product_id": product_id, "quantity": 1}]
    order_json = generic_order_helper.create_order(additional_args={'line_items': line_items})

    order_total_price = order_json['total']

    assert float(order_total_price) == float(product_price), f"Unexpected 'total' price in response of 'create order' " \
                                                             f"for product that is not on sale. " \
                                                             f"Product price: {product_price}, " \
                                                             f"Order total price: {order_total_price}"


@pytest.mark.ecombe69
@pytest.mark.tcid212
@pytest.mark.ecombe69
def test_verify_order_calculates_correct_price_item_is_on_sale():
    """
        Test case to verify that an order calculates the correct price when the item is on sale.

    """
    # create new product that is on sale
    generic_product_helper = GenericProductHelper()
    regular_price = round(random.uniform(10, 100), 2)
    sale_price = round(regular_price * .75, 2)
    product_info = generic_product_helper.create_a_product(on_sale=True, regular_price=str(regular_price), sale_price=str(sale_price))

    product_id = product_info['id']

    # create order using the newly created product
    generic_order_helper = GenericOrderHelpers()
    line_items = [{"product_id": product_id, "quantity": 1}]
    order_json = generic_order_helper.create_order(additional_args={'line_items': line_items})

    order_total_price = order_json['total']

    assert float(order_total_price) == float(sale_price), f"Unexpected 'total' price in response of 'create order' " \
                                                          f"for product that is 'on sale'." \
                                                          f"Product price: {sale_price}, " \
                                                          f"Order total price: {order_total_price}"


@pytest.mark.tcid2122
@pytest.mark.ecombe70
def test_verify_order_calculates_correct_price_2_items_on_sale_and_not():
    """
       Test case to verify that an order calculates the correct price when there are 2 items, one on sale and one not on sale.

    """
    generic_product_helper = GenericProductHelper()

    # create new product that is not on sale
    product_info_not_on_sale = generic_product_helper.create_a_product()
    product_id_not_on_sale = product_info_not_on_sale['id']
    product_price_not_on_sale = product_info_not_on_sale['regular_price']

    # create new product that is on sale
    regular_price = round(random.uniform(10, 100), 2)
    sale_price = round(regular_price * .75, 2)
    product_info_on_sale = generic_product_helper.create_a_product(on_sale=True, regular_price=str(regular_price), sale_price=str(sale_price))
    product_id_on_sale = product_info_on_sale['id']
    product_price_on_sale = product_info_on_sale['sale_price']

    # create order with the two products as line items
    generic_order_helper = GenericOrderHelpers()
    line_items = [
        {"product_id": product_id_not_on_sale, "quantity": 1},
        {"product_id": product_id_on_sale, "quantity": 1}
    ]
    order_json = generic_order_helper.create_order(additional_args={'line_items': line_items})

    order_total_price = order_json['total']

    expected_total = float(product_price_not_on_sale) + float(product_price_on_sale)
    expected_total = round(expected_total, 2)
    assert float(order_total_price) == float(expected_total), f"Unexpected 'total' price in response of 'create order' " \
                                                          f"for product that is 'on sale'." \
                                                          f"Products combined price: {expected_total}, " \
                                                          f"Order total price: {order_total_price}"

