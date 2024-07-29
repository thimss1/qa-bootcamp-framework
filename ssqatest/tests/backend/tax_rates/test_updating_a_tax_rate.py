import pytest
import logging as logger
from ssqatest.src.api_helpers.tax_rates_helper import TaxHelper
from ssqatest.src.dao.tax_rate_dao import TaxDAO
from ssqatest.src.utilities import genericUtilities as gu


@pytest.mark.tex_rates
@pytest.mark.ecombe95
@pytest.mark.tcid228
def test_update_tax_rate():
    """
        Test case to verify the functionality of updating a tax rate.
    """

    logger.info("TEST: Create refund with valid data")
    tax_obj = TaxHelper()
    tax_dao = TaxDAO()

    rand_tax = tax_dao.get_random_tax_rate_from_db()
    id_in_db = rand_tax[0]['tax_rate_id']
    tax_name = gu.generate_random_string(10)

    data = {
          "name": tax_name
        }
    payload = dict(data)
    updated_tax_rate = tax_obj.call_update_tax_rate(id_in_db,payload)
    assert updated_tax_rate['name'] == data['name'], f"tax rate value did not update."