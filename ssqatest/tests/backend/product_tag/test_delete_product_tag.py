import random
from ssqatest.src.api_helpers.ProductTagAPIHelper import ProductTagHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility

import pytest


@pytest.mark.ecombe111
def test_delete_product_tag_by_id():
    """
       Test to verify the functionality of deleting a product tag by its ID.
    """
    name = generate_random_string()
    description = generate_random_string(30)
    data = {
        "name": name,
        "description": description
    }
    tag_helper = ProductTagHelper()
    rs_api = tag_helper.call_create_product_tag(data)
    tag_id = rs_api['id']
    tag_json = tag_helper.delete_product_tag(tag_id)
    assert tag_json['id'] == tag_id , "delete product tag by id failed"


@pytest.mark.ecombe112
def test_delete_product_tag_by_invalid_id():
    """
    Test to verify the handling of deleting a product tag with an invalid ID.
    """

    tag_helper = ProductTagHelper()
    tag_id = random.randint(1000,2000)
    tag_json = tag_helper.delete_product_tag(tag_id,expected_status_code=404)
    assert tag_json['code'] == 'woocommerce_rest_term_invalid', "delete product tag by invalid id returned wrong code"

