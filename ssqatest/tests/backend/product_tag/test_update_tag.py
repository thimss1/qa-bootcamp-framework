import random
from ssqatest.src.api_helpers.ProductTagAPIHelper import ProductTagHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string

import pytest


@pytest.mark.ecombe116
def test_update_product_tag_name():
    """
        Test to verify the functionality of updating the name of a product tag.
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
    updated_name = generate_random_string()
    payload = {
        "name": updated_name
    }
    tag_json = tag_helper.call_update_product_tag(tag_id,payload)
    assert tag_json['id'] == tag_id , "update tag failed"


@pytest.mark.ecombe117
def test_update_product_tag_by_invalid_id():
    """
        Test to verify the handling of updating a product tag with an invalid ID.
    """
    tag_helper = ProductTagHelper()
    tag_id = random.randint(1000,2000)
    updated_name = generate_random_string()
    payload = {
        "name": updated_name
    }
    tag_json = tag_helper.call_update_product_tag(tag_id, payload,expected_status_code=404)
    assert tag_json['code'] == "woocommerce_rest_term_invalid", "update by invalid id returned wrong code"
