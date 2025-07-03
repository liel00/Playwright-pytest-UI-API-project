import allure
import pytest

from gui_tests.pages.edit_room_page import EditRoomPage
from gui_tests.pages.home_page import HomePage
from gui_tests.pages.login_page import LoginPage
from gui_tests.pages.room_page import RoomPage


class TestRoom:
    @allure.step(
        "Adding a new room: logging in, filling room details, selecting amenities, and verifying creation and deletion")
    @pytest.mark.sanity
    def test_add_new_room_and_delete(self, set_up_tear_down, page) -> None:
        home_page = HomePage(page)
        login_page = LoginPage(page)
        room_page = RoomPage(page)
        home_page.click_admin_button()
        login_page.login()
        room_page.build_new_room_and_verify()
        room_page.delete_room_and_verify("Test Room")

    @allure.step(
        "Editing an existing room: selecting room, modifying details, updating, and verifying changes and deletion")
    @pytest.mark.sanity
    def test_edit_room_and_delete(self, set_up_tear_down, page) -> None:
        home_page = HomePage(page)
        login_page = LoginPage(page)
        room_page = RoomPage(page)
        edit_page = EditRoomPage(page)
        home_page.click_admin_button()
        login_page.login()
        room_page.build_new_room_and_verify(room_name="Edit", type_value="Double",
                                            accessible_value="true", room_price="150")
        room_page.click_edit_room("Edit")
        edit_page.edit_room()
        room_page.delete_room_and_verify("Edited Room")
