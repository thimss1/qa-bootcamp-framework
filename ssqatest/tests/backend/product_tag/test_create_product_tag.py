from ssqatest.src.api_helpers.ProductTagAPIHelper import ProductTagHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string
import pytest


@pytest.mark.ecombe110
def test_create_product_tag():
    """
        Test to verify the functionality of creating a product tag.
    """
    name = generate_random_string()
    description = generate_random_string(30)
    data = {
        "name": name,
        "description": description
    }
    tag_helper = ProductTagHelper()
    rs_api = tag_helper.call_create_product_tag(data)

    assert rs_api['name'] == name, "product tag not created"




