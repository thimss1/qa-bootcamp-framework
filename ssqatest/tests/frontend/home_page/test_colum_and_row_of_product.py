
import pytest

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestColumnRow:
    """
    Test class to verify the number of columns and rows in the home page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()
        yield

    @pytest.mark.tcid104
    @pytest.mark.ecomfe2
    @pytest.mark.ecomfe3
    def test_four_columns_and_rows(self, setup):
        """
        Test to verify that there are four columns and rows in the home page.

         Args:
            setup: A setup object
        """

        all_product_elements = self.homepage.get_all_product_elements()

        assert len(all_product_elements)/4 == 4, \
            f"Unexpected number of products displayed on home page. "
