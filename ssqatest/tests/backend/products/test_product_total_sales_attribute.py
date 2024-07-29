

import pytest
from ssqatest.src.generic_helpers.generic_product_helper import GenericProductHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers


@pytest.fixture()
def setup():
    generic_product_helper = GenericProductHelper()
    generic_order_helper = GenericOrderHelpers()
    random_product = generic_product_helper.get_random_products(qty=1)

    return {"generic_product_helper": generic_product_helper,
            "random_product": random_product,
            "generic_order_helper": generic_order_helper}


@pytest.mark.parametrize("ordered_qty",
                         [
                             pytest.param(1, marks=[pytest.mark.tcid191,pytest.mark.ecombe39]),
                             pytest.param(3, marks=[pytest.mark.tcid192,pytest.mark.ecombe38]),
                     ])
def test_product_total_sales_attribute(setup, ordered_qty):
    """
        Test case to verify that the 'total_sales' attribute of a product is updated correctly after placing an order.

        Args:
             setup
            ordered_qty
    """
    # setup data and helper objects
    generic_product_helper = setup["generic_product_helper"]
    generic_order_helper = setup["generic_order_helper"]
    random_product = setup['random_product']
    total_sales_before = random_product[0]['total_sales']
    product_id = random_product[0]['id']

    # create an order using the product from the setup
    partial_payload = {"line_items": [{"product_id": product_id, "quantity": ordered_qty}]}
    generic_order_helper.create_order(additional_args=partial_payload)

    # get the product detail after order is placed
    product_details = generic_product_helper.get_product_detail_via_api(product_id)
    total_sales_after = product_details['total_sales']

    # verify the 'total_sales' is updated
    expected_total_sales_after = total_sales_before + ordered_qty
    assert total_sales_after == expected_total_sales_after, f"The 'total_sales' parameter of a product expected to update " \
                                                            f"after placing an order for the product." \
                                                            f"Actual value: {total_sales_after}, Expected value: {expected_total_sales_after}"



