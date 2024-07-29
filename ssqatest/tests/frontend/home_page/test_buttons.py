import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestAddButtonViewButton:
    """
     Test class to verify the functionality of the add button and view button.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid111
    @pytest.mark.ecomfe31
    def test_add_button_displays_view_button(self, setup):
        """
        Test to verify that clicking the 'add to cart' button displays the 'view cart' button.

        Args:
            setup: A setup object.
        """
        logger.info(f"Running Test: test_add_button_displays_view_button")
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()

        View_button = self.homepage.get_view_button_first_product()

        # Assert that clicking the add button does display view button
        assert View_button == 'View cart', "clicking the add button does not display view button"

    @pytest.mark.ecomfe23
    def test_clicking_product_displays_product_detail(self, setup):
        """
        Test to verify that clicking a product displays the product detail page.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: clicking_product_displays_product_detail")
        self.homepage.go_to_home_page()
        self.homepage.click_first_product()
        product_name = self.homepage.get_firts_product_name()

        # Assert that the product detail page is displayed
        assert product_name, "Clicking a product does not display a detail page"


@pytest.mark.usefixtures("init_driver")
class TestAddButtonViewButtonTwo:
    """
    Another test class to verify the functionality of the add button and view button.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid110
    @pytest.mark.ecomfe30
    def test_add_button_work(self, setup):
        """
        Test to verify that the 'add to cart' button adds the product to the cart.

       Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        count = self.header.get_cart_item_count()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        count_new = self.header.get_cart_item_count()

        # Assert that the add to cart button works
        assert int(count_new) == int(count) + 1, "Add to cart button did not add to cart"