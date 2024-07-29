
import logging as logger

import pytest
from ssqatest.src.generic_helpers.generic_reports_helper import GenericReportsHelper


@pytest.mark.smoke
@pytest.mark.reports
@pytest.mark.ecombe85
@pytest.mark.tcid193
@pytest.mark.ecombe85
def test_verify_all_valid_report():
    """
    Verifies the 'list reports' endpoint responds with list of all expected reports.
    :return:
    """

    logger.info("Running test: test_verify_all_valid_report")
    generic_reports_helper = GenericReportsHelper()

    api_all_reports = generic_reports_helper.list_all_reports()
    expected_all_reports = generic_reports_helper.get_sample_data('list_reports_api_response')

    logger.debug(f"Expected all reports: {expected_all_reports}")
    logger.debug(f"API response all reports: {api_all_reports}")

    # verify every item that is expected is in the api response
    for expected_report in expected_all_reports:
        if expected_report not in api_all_reports:
            raise Exception(f"Report '{expected_report.get('slug')}' does not exist in 'list reports' endpoint response.")

    # verify every item in the response is in the expected list
    for api_report in api_all_reports:
        if api_report not in expected_all_reports:
            raise Exception(f"Report '{api_report['slug']}' not expected but found in 'list reports' endpoint response.")
