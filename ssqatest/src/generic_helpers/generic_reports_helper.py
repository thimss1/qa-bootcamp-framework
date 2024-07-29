import json
import os

from ssqatest.src.api_helpers.ReportsAPIHelper import ReportsAPIHelper
from ssqatest.src.configs.MainConfigs import MainConfigs
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility


class GenericReportsHelper:

    def __init__(self):
        self.reports_api_helper = ReportsAPIHelper()
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def list_all_reports(self):
        return self.reports_api_helper.call_list_reports()

    def get_reports_products_totals(self):
        rs_api = WooAPIUtility().get("reports/products/totals", expected_status_code=200)
        return rs_api

    def get_sample_data(self, sample_data_name):

        if sample_data_name.lower() == 'list_reports_api_response':
            expected_data_path = os.path.join(self.cur_file_dir, '..', 'data', 'list_reports_response.json')

            with open(expected_data_path, 'r') as f:
                content = f.read()

            base_url = MainConfigs.get_base_url()
            clean_content = content.replace('https://example.com', base_url)

            return json.loads(clean_content)

        if sample_data_name.lower() == 'report_products_totals_response':
            expected_data_path = os.path.join(self.cur_file_dir, '..', 'data', 'reports_products_totals_response.json')

            with open(expected_data_path, 'r') as f:
                data = json.load(f)

            return data
