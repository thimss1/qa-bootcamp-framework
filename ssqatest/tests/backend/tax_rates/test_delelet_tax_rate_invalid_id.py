import random

import pytest
import logging as logger
from ssqatest.src.api_helpers.tax_rates_helper import TaxHelper
from ssqatest.src.dao.tax_rate_dao import TaxDAO


@pytest.mark.ecombe123
def test_delete_tax_rate_invalid_id():
    """
      Test to verify the handling of deleting a tax rate with an invalid ID.
    """
    tax_obj = TaxHelper()
    tax_id = random.randint(100,800)

    tax_api_info = tax_obj.delete_tax_rate(tax_id,expected_status_code=400)
    assert tax_api_info['code'] == 'woocommerce_rest_invalid_id', f"tax rate delete invalid id return wrong code"