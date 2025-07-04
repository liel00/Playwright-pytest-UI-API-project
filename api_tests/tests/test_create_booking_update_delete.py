import allure
import pytest

from api_tests.data.booking_data import post_booking_data, get_booking_data, put_updated_data, delete_data, \
    partial_data, patch_data
from api_tests.core.booking_requests import (
    create_booking_request,
    get_booking_request,
    update_booking_request,
    delete_booking_request,
    get_deleted_booking_request, partial_update_booking
)


class TestBooking:

    @allure.title("Create new booking")
    @pytest.mark.API
    def test_create_booking(self):
        booking_id, booking_data = create_booking_request(post_booking_data)
        assert isinstance(booking_id, int), "booking_id should be an integer"
        assert booking_data["booking"]["firstname"] == post_booking_data["firstname"]
        assert booking_data["booking"]["lastname"] == post_booking_data["lastname"]

    @allure.title("Create and retrieve a booking")
    @pytest.mark.API
    def test_get_booking(self):
        booking_id, _ = create_booking_request(get_booking_data)
        fetched_data = get_booking_request(booking_id)

        assert fetched_data["firstname"] == get_booking_data["firstname"]
        assert fetched_data["lastname"] == get_booking_data["lastname"]

    @allure.title("Update an existing booking")
    @pytest.mark.API
    def test_update_booking(self, get_token):
        booking_id, _ = create_booking_request(put_updated_data)
        updated = update_booking_request(booking_id, put_updated_data, get_token)

        assert updated == put_updated_data

    @allure.title("Delete booking and ensure it's removed")
    @pytest.mark.API
    def test_delete_booking(self, get_token):
        booking_id, _ = create_booking_request(delete_data)
        delete_booking_request(booking_id, get_token)
        get_deleted_booking_request(booking_id)

    @pytest.mark.API
    def test_partial_update_booking(self, get_token):
        booking_id, _ = create_booking_request(patch_data)
        patch = partial_update_booking(booking_id, partial_data, get_token)
        assert patch["firstname"] == partial_data["firstname"]
        assert patch["lastname"] == partial_data["lastname"]
        assert patch["totalprice"] == partial_data["totalprice"]