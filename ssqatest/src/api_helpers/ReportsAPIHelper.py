

from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger



class ReportsAPIHelper:

    def __init__(self):
        self.woo_api_utility = WooAPIUtility()

    def call_list_reports(self):
        logger.debug("Calling 'list all reports'.")
        return self.woo_api_utility.get('reports', expected_status_code=200)

