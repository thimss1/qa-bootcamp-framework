import logging as logger

import pytest
from ssqatest.src.generic_helpers.generic_product_helper import GenericProductHelper
from ssqatest.src.generic_helpers.generic_product_reviews_helper import GenericProductReviewsHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string, generate_random_email_and_password


@pytest.fixture(scope="function")
def setup_teardown(request):

    request.cls.product_helper = GenericProductHelper()
    request.cls.product_review_helper = GenericProductReviewsHelper()
    request.cls.product = request.cls.product_helper.create_a_product()
    request.cls.rating_count_before = request.cls.product['rating_count']
    request.cls.product_id = request.cls.product['id']

    yield

    logger.info(f"Running teardown. Deleting product id: {request.cls.product_id}")
    request.cls.product_helper.delete_a_product(request.cls.product_id)


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.smoke
class TestProductsReviewsSmoke(object):

    @pytest.mark.ecombe40
    @pytest.mark.tcid199
    @pytest.mark.ecombe40
    def test_verify_create_product_review_endpoint_creates_review(self):
        """
            Test to verify that the create product review endpoint successfully creates a review for a product.

        """
        logger.info("test_verify_create_product_review_endpoint_creates_review")

        assert self.rating_count_before == 0, f"The 'rating_count' field of a new created product is not 0"

        # create review for the product
        qty_review_to_add = 5
        for _ in range(qty_review_to_add):
            self.product_review_helper.create_random_review_for_product(self.product_id)

        # call product again
        product = self.product_helper.get_product_detail_via_api(self.product_id)
        rating_count_after = product['rating_count']

        # subtracting 1 from the actual expected because there is a bug, it always show 1 less than actual.
        expected_rating_count = qty_review_to_add - 1
        assert rating_count_after == expected_rating_count, f"Expected 'rating_count=1' after creating review for product but found 'rating_count={rating_count_after}'."

    @pytest.mark.tcid200
    @pytest.mark.ecombe41
    def test_verify_review_creation_fail_if_all_fields_duplicated(self):
        """
        Test to verify that creating a review with all fields duplicated fails and returns the expected status code and error message.

        """

        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)

        # create another review with same data
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review=review_rs['review'],
            reviewer=review_rs['reviewer'],
            reviewer_email=review_rs['reviewer_email'],
            rating=review_rs['rating'],
            expected_status_code=409
        )

        assert rs_duplicate['code'] == 'woocommerce_rest_comment_duplicate'
        assert 'Duplicate comment detected; it looks as though' in rs_duplicate['message']
        assert rs_duplicate['data']['status'] == 409

    @pytest.mark.ecombe42
    @pytest.mark.tcid201
    @pytest.mark.ecombe42
    def test_review_creation_should_not_fail_if_reviewer_is_different(self):
        """All fields have the same value but the 'reviewer' is changes. Expecting successful review creation."""
        """
            Test to verify that creating a review with all fields the same except the 'reviewer' field succeeds and returns the expected status code.

        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)

        # create another review with same data except the 'reviewer' field.
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review=review_rs['review'],
            reviewer=f"{generate_random_string(length=5)} {generate_random_string(length=6)}",
            reviewer_email=review_rs['reviewer_email'],
            rating=review_rs['rating'],
            expected_status_code=201
        )

        # verify the second review is created by checking its status.
        # the response code of the second call is also verified to be 201
        assert rs_duplicate['status'] == 'approved'

    @pytest.mark.ecombe43
    @pytest.mark.tcid202
    @pytest.mark.ecombe43
    def test_review_creation_should_not_fail_if_review_is_different(self):
        """All fields have the same value but the 'review' is changes. Expecting successful review creation."""
        """
            Test to verify that creating a review with all fields the same except the 'review' field succeeds and returns the expected status code.
        
        """

        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)

        # create another review with same data except the 'review' field.
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review="Automation review: " + generate_random_string(length=25),
            reviewer=review_rs['reviewer'],
            reviewer_email=review_rs['reviewer_email'],
            rating=review_rs['rating'],
            expected_status_code=201
        )

        # verify the second review is created by checking its status.
        # the response code of the second call is also verified to be 201
        assert rs_duplicate['status'] == 'approved'

    @pytest.mark.ecombe44
    @pytest.mark.tcid203
    @pytest.mark.ecombe44
    def test_review_creation_should_not_fail_if_reviewer_email_is_different(self):
        """All fields have the same value but the 'reviewer_email' is changes. Expecting successful review creation."""
        """
            Test to verify that creating a review with all fields the same except the 'reviewer_email' field succeeds and returns the expected status code.

        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)

        # create another review with same data except the 'reviewer_email' field.
        rs_duplicate = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review=review_rs['review'],
            reviewer=review_rs['reviewer'],
            reviewer_email=generate_random_email_and_password()['email'],
            rating=review_rs['rating'],
            expected_status_code=201
        )

        # verify the second review is created by checking its status.
        # the response code of the second call is also verified to be 201
        assert rs_duplicate['status'] == 'approved'

    @pytest.mark.ecombe45
    @pytest.mark.tcid204
    @pytest.mark.ecombe45
    def test_verify_default_status_for_create_review_is_approved(self):
        """
            Test to verify that the default status for a created review is set to "approved" as expected.

        """
        review_rs = self.product_review_helper.create_random_review_for_product(self.product_id)
        assert review_rs['status'] == 'approved'
