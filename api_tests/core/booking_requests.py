import os
import requests
import allure
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL_API")


def create_booking_request(data):
    # Sends a POST request to create a new booking and returns its ID and full response.
    url = f"{BASE_URL}/booking"
    headers = {"Content-Type": "application/json"}

    with allure.step("Create booking - POST /booking"):
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 200, f"Failed to create booking: {response.status_code} - {response.text}"

        response_json = response.json()
        assert "bookingid" in response_json, "Missing 'bookingid' in response"
        return response_json["bookingid"], response_json


def get_booking_request(booking_id):
    # Sends a GET request to retrieve booking details by booking ID.
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {"Accept": "application/json"}

    with allure.step(f"Get booking - GET /booking/{booking_id}"):
        response = requests.get(url, headers=headers)
        assert response.status_code == 200, f"Failed to get booking: {response.status_code} - {response.text}"
        response_json = response.json()
        return response_json


def update_booking_request(booking_id, updated_data, token):
    # Sends a PUT request to update an existing booking using a token for authentication.
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    response = requests.put(url, json=updated_data, headers=headers)
    assert response.status_code == 200, f"Failed to update booking: {response.status_code} - {response.text}"
    response_json = response.json()
    return response_json


def delete_booking_request(booking_id, token):
    # Sends a DELETE request to remove a booking using a token for authentication.
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    with allure.step(f"Delete booking - DELETE /booking/{booking_id}"):
        response = requests.delete(url, headers=headers)
        assert response.status_code == 201, f"Failed to delete booking: {response.status_code} - {response.text}"


def get_deleted_booking_request(booking_id):
    # Verifies that a previously deleted booking returns 404 (not found).
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 404, f"Booking still exists: {response.status_code} - {response.text}"


def partial_update_booking(booking_id, partial_data, token):
    # Sends a PATCH request to partially update booking fields using a token for authentication.
    url = f"{BASE_URL}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }
    response = requests.patch(url, json=partial_data, headers=headers)
    assert response.status_code == 200, f"Failed to partially update booking: {response.status_code} - {response.text}"

    return response.json()

