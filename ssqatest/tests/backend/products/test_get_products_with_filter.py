from ssqatest.src.api_helpers.ProductsAPIHelper import ProductsAPIHelper

from ssqatest.src.dao.products_dao import ProductsDAO
import pytest
from datetime import datetime, timedelta


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.ecombe27
    @pytest.mark.tcid51
    @pytest.mark.ecombe27
    def test_list_products_with_filter_after(self):
        """
            Test case to verify the 'list products with filter' functionality using the 'after' parameter.

        """
        # create data
        x_days_from_today = 300
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()

        # make the call
        payload = dict()
        payload['after'] = after_created_date
        rs_api = ProductsAPIHelper().call_list_products(payload)
        assert rs_api, f"Empty response for 'list products with filer"

        # get data from db
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        # verify response match db
        assert len(rs_api) == len(db_products), f"List products with filter 'after' returned unexpected number of products." \
                                                f"Expected: {len(db_products)}, Actual: {len(rs_api)}"
        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List products with filter, product ids in response mismatch in db."
