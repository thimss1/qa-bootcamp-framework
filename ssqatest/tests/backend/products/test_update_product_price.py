
from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper
from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.utilities.genericUtilities import generate_random_string

import random
import pytest

pytestmark = [pytest.mark.products, pytest.mark.regression]


@pytest.mark.tcid61
@pytest.mark.ecombe30
def test_update_regular_price_should_update_price():
    """
    Verifies updating the 'regular_price' field should automatically update the 'price' field.
    """

    # create helper objects and get random product from db
    product_helper = ProductsAPIHelper()
    product_dao = ProductsDAO()

    # for this test the 'sale_price' of the product must be empty. If product has sale price, updating the 'regular_price'
    # does not update the 'price'. So get a bunch of products and loop untill you find one that is not on sale. If all in
    # the list are on sale then take random one and update the sale price
    # get 100 random products and select one for the test. Use filter on_sale=True to get only on_sale items
    filters = {'on_sale': False, 'per_page': 100}
    rand_products = product_helper.call_list_products(filters)

    if rand_products:
        selected_product = random.choice(rand_products)
        product_id = selected_product['id']
    else:
        # if no product that on_sale=False is found, then take a random product and udpate it
        rand_products = product_helper.call_list_products()
        selected_product = random.choice(rand_products)
        product_id = selected_product['id']
        product_helper.call_update_product(product_id, {'sale_price': ''})

    # make the update to 'regular_price'
    new_price = str(random.randint(10, 100)) + '.' + str(random.randint(10, 99))
    payload = dict()
    payload['regular_price'] = new_price

    rs_update = product_helper.call_update_product(product_id, payload=payload)

    # verify the response has the 'price' and 'regular_price' has updated and 'sale_price' is not updated
    assert rs_update['price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                            f"update the 'price' field. price field actual value {rs_update['price']}," \
                                            f"but expected: {new_price}"

    assert rs_update['regular_price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                            f"update in the response. Actual response 'regular_price'={rs_update['price']}," \
                                            f"but expected: {new_price}"

    # get the product after the update and verify response
    rs_product = product_helper.call_retrieve_product(product_id)
    assert rs_product['price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                            f"update the 'price' field. price field actual value {rs_product['price']}," \
                                            f"but expected: {new_price}"

    assert rs_product[
               'regular_price'] == new_price, f"Update product api call response. Updating the 'regular_price' did not " \
                                              f"update. Actual 'regular_price'={rs_product['price']}," \
                                              f"but expected: {new_price}"


@pytest.mark.ecombe34
@pytest.mark.tcid65
@pytest.mark.ecombe37
def test_adding_sale_price_should_set_on_sale_flag_true():
    """
    Verifies When the sale price of a product is updated, then it should set the field 'on_sale' = True
    """

    # first get a product from db that is not on sale
    product_helper = ProductsAPIHelper()
    product_dao = ProductsDAO()

    filters = {'on_sale': False, 'per_page': 100}
    rand_products = product_helper.call_list_products(filters)
    selected_product = random.choice(rand_products)
    product_id = selected_product['id']

    # first check the status is False to start with
    original_info = product_helper.call_retrieve_product(product_id)
    assert not original_info['on_sale'], f"Getting test data with 'on_sale=False' but got 'True'. Unable to use this product for test."

    # update the sale price of the product
    sale_price = float(original_info['regular_price']) * 0.75  # sale is 75% of original

    payload = dict()
    payload['sale_price'] = str(sale_price)
    product_helper.call_update_product(product_id, payload=payload)

    # get the product sale price is updated
    after_info = product_helper.call_retrieve_product(product_id)
    assert after_info['sale_price'] == str(sale_price), f"Updated product 'sale_price' but value did not update." \
                                                        f"Product id: {product_id}, Expected sale price: {sale_price}," \
                                                        f"Actual sale price: {after_info['sale_price']}"


@pytest.mark.ecombe32
@pytest.mark.ecombe33
@pytest.mark.tcid63
@pytest.mark.tcid64
@pytest.mark.ecombe32
@pytest.mark.ecombe33
def test_update_on_sale_field_buy_updating_sale_price():
    """
    Two test case.
    First case update the 'sale_price > 0' and verify the field changes to 'on_sale=True'.
    Second case update the 'sale_price=""' and verify the field changes to 'on_sale=False'.
    """

    product_helper = ProductsAPIHelper()

    # create product for the tests and verify the product has on_sale=False
    regular_price = str(random.randint(10, 100)) + '.' + str(random.randint(10, 99))
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = regular_price
    product_info = product_helper.call_create_product(payload)
    product_id = product_info['id']
    assert not product_info['on_sale'], f"Newly created product should not have 'on_sale=True'. Product id: {product_id}"
    assert not product_info['sale_price'], f"Newly created product should not have value for 'sale_price' field."

    # (tcid-63) now update the 'sale_price' and verify the 'on_sale' is set to True
    sale_price = float(regular_price) * .75
    product_helper.call_update_product(product_id, {'sale_price': str(sale_price)})
    product_after_update = product_helper.call_retrieve_product(product_id)
    assert product_after_update['on_sale'], f"Updated 'sale_price' of product, but the 'on_sale' did not set to 'True'." \
                                            f"Product id: {product_id}"

    # (tcid-64) now update the sale_price to empty string and verify the 'on_sale is set to False
    product_helper.call_update_product(product_id, {'sale_price': ''})
    product_after_update = product_helper.call_retrieve_product(product_id)
    assert not product_after_update['on_sale'], f"Updated 'sale_price=""' of product, but the 'on_sale' did not set to 'False'." \
                                            f"Product id: {product_id}"
