import pytest
import logging as logger
import time
from ssqatest.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestProductName:
    """
    Test class to verify the displayed  product name.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        yield

    @pytest.mark.tcid104
    @pytest.mark.ecomfe24
    def test_product_name_displayed(self, setup):
        """
        Test to verify that the product name is displayed under the product image.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_product_name_displayed")
        self.homepage.go_to_home_page()
        product_name = self.homepage.get_firts_product_name()

        # Assert that the product name is displayed under image
        assert product_name, "product name is not displayed under product image"

    @pytest.mark.ecomfe33
    def test_verify_x_y_result_is_displayed(self, setup):
        """
        Test to verify that the expected heading "Showing 1–16 of 17 results" is displayed.

        Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        expected_heading = 'Showing 1–16 of 17 results'
        time.sleep(10)
        displayed_heading = self.homepage.get_x_z_result()
        assert displayed_heading == expected_heading, \
            f"Showing 1–16 of 17 results is not displayed " \
            f"Expected: {expected_heading}, Actual: {displayed_heading}"
