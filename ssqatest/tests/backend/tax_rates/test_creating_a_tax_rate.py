import pytest
import logging as logger
from ssqatest.src.api_helpers.tax_rates_helper import TaxHelper
from ssqatest.src.dao.tax_rate_dao import TaxDAO


@pytest.mark.tex_rates
@pytest.mark.ecombe94
@pytest.mark.tcid227
def test_create_tax_rate():
    """
        Test case to verify the functionality of creating a tax rate.
    """

    tax_obj = TaxHelper()
    tax_dao = TaxDAO()

    data = {
          "country": "US",
          "state": "AL",
          "cities": ["Alpine", "Brookside", "Cardiff"],
          "postcodes": ["35014", "35036", "35041"],
          "rate": "4",
          "name": "State Tax",
          "shipping": False
        }
    payload = dict(data)
    new_tax = tax_obj.call_create_tax_rate(payload)
    tax_id = new_tax['id']
    tax_info = tax_dao.get_tax_by_id(tax_id)

    id_in_api = new_tax['id']
    id_in_db = tax_info[0]['tax_rate_id']
    assert id_in_api == id_in_db, f'Create tax_rate response "id" not same as "ID" in database.' \
                                  f'id: {tax_id}'