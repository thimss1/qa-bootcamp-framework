import random

from ssqatest.src.api_helpers.tax_rates_helper import TaxHelper
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility

import pytest


@pytest.mark.ecombe124
def test_get_all_tax_rates():
    """
      Test to verify that the 'get all tax rates' endpoint returns all tax rates.
    """
    req_helper = WooAPIUtility()
    rs_api = req_helper.get(woo_endpoint='taxes')
    assert rs_api, f"Get all tax rates end point returned nothing."


@pytest.mark.ecombe125
def test_get_tax_rate_by_id():
    """
        Test to verify the functionality of 'get tax rate by ID'.
    """

    tax_obj = TaxHelper()

    data = {
          "country": "US",
          "state": "AL",
          "cities": ["dc", "newyork", "Cardiff"],
          "postcodes": ["35014", "35036", "35041"],
          "rate": "10",
          "name": "State Tax",
          "shipping": False
        }
    payload = dict(data)
    new_tax = tax_obj.call_create_tax_rate(payload)
    tax_id = new_tax['id']

    rs_api = tax_obj.get_tax_rate_by_id(tax_id)

    assert rs_api['id'] == tax_id, f'retrieve tax rate by id failed'


@pytest.mark.ecombe126
def test_get_tax_rate_by_invalid_id():
    """
       Test to verify the handling of 'get tax rate by invalid ID'.
    """
    tax_obj = TaxHelper()
    tax_id = random.randint(1000, 2000)

    rs_api = tax_obj.get_tax_rate_by_id(tax_id)

    assert rs_api['code'] == 'tax_id', f'retrieve tax rate by invalid id returned wrong code'

