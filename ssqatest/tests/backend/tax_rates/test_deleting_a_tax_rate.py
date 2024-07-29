import pytest
import logging as logger
from ssqatest.src.api_helpers.tax_rates_helper import TaxHelper
from ssqatest.src.dao.tax_rate_dao import TaxDAO


@pytest.mark.tex_rates
@pytest.mark.ecombe96
@pytest.mark.tcid229
def test_delete_tax_rate():
    """
        Test case to verify the functionality of deleting a tax rate.
    """

    logger.info("TEST: delete a tax rate")
    tax_obj = TaxHelper()
    tax_dao = TaxDAO()

    rand_tax = tax_dao.get_random_tax_rate_from_db()
    id_in_db = rand_tax[0]['tax_rate_id']

    tax_api_info = tax_obj.delete_tax_rate(id_in_db)
    assert tax_api_info['id'] == id_in_db, f"tax rate  not deleted"