
import pytest

from ssqatest.src.generic_helpers.generic_reports_helper import GenericReportsHelper
from ssqatest.src.generic_helpers.generic_product_helper import GenericProductHelper


@pytest.fixture(scope='module')
def reports_products_totals_setup():

    generic_reports_helper = GenericReportsHelper()
    generic_products_helper = GenericProductHelper()

    info = {'generic_reports_helper': generic_reports_helper,
            'generic_products_helper': generic_products_helper,
            'generic_order_helper': 'generic_order_helper'}

    return info


@pytest.mark.smoke
@pytest.mark.reports
@pytest.mark.ecombe86
@pytest.mark.tcid194
@pytest.mark.ecombe86
def test_verify_reports_products_total_response_is_as_expected(reports_products_totals_setup):
    """
    Verifies the response has the expected product types.
    The quantities will change so updating the response to have qty 0 for each item.
    :return:
    """
    generic_reports_helper = reports_products_totals_setup['generic_reports_helper']

    api_all_reports = generic_reports_helper.get_reports_products_totals()

    # update the total to 0 to match the expected hardcoded values
    for i in api_all_reports:
        i.update({"total": 0})

    expected_all_reports = generic_reports_helper.get_sample_data('report_products_totals_response')

    # verify all expected reports are in the api response
    for expected_report in expected_all_reports:
        if expected_report not in api_all_reports:
            raise Exception(f"Report '{expected_report.get('slug')}' does not exist in 'reports/products/totals' endpoint response.")

    # verify all report in api response are in the expected reports
    for api_report in api_all_reports:
        if api_report not in expected_all_reports:
            raise Exception(f"Report '{api_report['slug']}' not expected but found in 'reports/products/totals' endpoint response.")


@pytest.mark.smoke
@pytest.mark.reports
@pytest.mark.parametrize("product_type", [
    pytest.param('external', marks=[pytest.mark.tcid195,pytest.mark.ecombe87]),
    pytest.param('grouped', marks=[pytest.mark.tcid196,pytest.mark.ecombe88]),
    pytest.param('simple', marks=[pytest.mark.tcid197,pytest.mark.ecombe89]),
    pytest.param('variable', marks=[pytest.mark.tcid198,pytest.mark.ecombe90])
            ])
def test_verify_reports_products_totals_by_product_type(reports_products_totals_setup, product_type):
    """
        Test to verify the 'reports/products/totals' endpoint for a specific product type.

        Args:
            reports_products_totals_setup (dict)
            product_type
    """
    generic_reports_helper = reports_products_totals_setup['generic_reports_helper']
    generic_products_helper = reports_products_totals_setup['generic_products_helper']

    # get current value, then create a product witht '' type, call the endpoint again and verify the quantity increased
    all_totals = generic_reports_helper.get_reports_products_totals()
    for i in all_totals:
        if i['slug'] == product_type:
            before_value = i['total']
            break
    else:
        raise Exception(f"'external' sug not found in 'reports/products/totals' response.")

    new_product = generic_products_helper.create_a_product(product_type=product_type)
    assert new_product['type'] == product_type

    new_totals = generic_reports_helper.get_reports_products_totals()
    for i in new_totals:
        if i['slug'] == product_type:
            after_value = i['total']
            break
    else:
        raise Exception(f"'external' sug not found in 'reports/products/totals' response.")

    assert after_value == (before_value + 1), f"Value 'total' in response 'reports/products/totals' did not increase by 1 after creating a product."
