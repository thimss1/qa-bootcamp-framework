import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage


@pytest.mark.usefixtures("init_driver")
class TestDropDown:
    """
        Test class to verify the display of sorting drop-down on the home page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        yield

    @pytest.mark.ecomfe5
    def test_sorting_drop_down_displayed_on_top_page(self, setup):
        """
        Test to verify that the sorting drop-down is displayed on the top of home page.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_sorting_drop_down_displayed_on_top_home_page")
        self.homepage.go_to_home_page()
        dropdown = self.homepage.get_sorting_dropdown_top_page()
        assert 'Default sorting' in dropdown, 'drop down is not displayed'

    @pytest.mark.ecomfe6
    def test_sorting_drop_down_displayed_on_bottom_page(self, setup):
        """
        Test to verify that the sorting drop-down is displayed on the bottom of home page.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_sorting_drop_down_displayed_on_bottom_home_page")
        self.homepage.go_to_home_page()
        dropdown = self.homepage.get_sorting_dropdown_bottom_page()
        assert 'Default sorting' in dropdown, 'drop down is not displayed'



