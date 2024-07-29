
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
import pytest
import random
import math
import logging as logger


@pytest.fixture(scope='module')
def my_setup_teardown():
    # hard code 50% coupon
    # TODO: instead of hard coding, get from API, if not exist create, if expired update, ...
    coupon_code = '50OFF'
    discount_pct = '50.00'

    # get a random product for order
    rand_products = ProductsAPIHelper().call_list_products()
    random.shuffle(rand_products)
    for i in rand_products:
        if i['price']:
            rand_product = i
            break
    else:
        raise Exception("Unable to find product with price.")

    info = dict()
    info['generic_order_helper'] = GenericOrderHelpers()
    info['coupon_code'] = coupon_code
    info['discount_pct'] = discount_pct
    info['product_id'] = rand_product['id']
    info['product_price'] = rand_product['price']

    return info


@pytest.mark.tcid60
@pytest.mark.ecombe127
def test_apply_valid_coupon_to_order(my_setup_teardown):
    """
    Validates when x% coupon is applied to an order, the 'total' amount is reduced by x%
    """
    # coupon info and product info in setup

    # create payload and make call to create order
    generic_order_helper = my_setup_teardown['generic_order_helper']
    order_payload_addition = {
        "line_items": [{"product_id": my_setup_teardown['product_id'], "quantity": 1}],
        "coupon_lines": [{"code": my_setup_teardown['coupon_code']}],
        "shipping_lines": [{"method_id": "flat_rate", "method_title": "Flat Rate", "total": "0.00"}]
        }

    rs_order = generic_order_helper.create_order(additional_args=order_payload_addition)

    # calculate expected total price based on coupon and product price
    expected_total = float(my_setup_teardown['product_price']) * (float(my_setup_teardown['discount_pct'])/100)

    # get total from order response and verify
    total = math.ceil(float(rs_order['total']))
    expected_total = math.ceil(expected_total)

    assert total == expected_total, f"Order total is not reduced after applying 50% coupon. Expected cost: {expected_total}, Actual: {total}"
