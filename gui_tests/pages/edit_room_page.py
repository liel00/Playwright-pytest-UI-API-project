from playwright.sync_api import expect
from gui_tests.utils.BasePage import BasePage


class EditRoomPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.room_name_input_in_edit = page.locator('#roomName')
        self.type_select_in_edit = page.locator('#type')
        self.Accessible_select_in_edit = page.locator('#accessible')
        self.room_price_input_in_edit = page.locator('#roomPrice')
        self.wifi_checkbox_in_edit = page.locator('#wifiCheckbox')
        self.refresh_checkbox_in_edit = page.locator('#refreshmentsCheckbox')
        self.tv_checkbox_in_edit = page.locator('#tvCheckbox')
        self.sale_checkbox_in_edit = page.locator('#safeCheckbox')
        self.radio_checkbox_in_edit = page.locator('#radioCheckbox')
        self.views_checkbox_in_edit = page.locator('#viewsCheckbox')
        self.update_button = page.locator('#update')
        self.rooms_button = page.locator("a.nav-link", has_text="Rooms")

    # This method returns the first room listing element that matches the given room name
    def get_room_by_name(self, room_name):
        return self.page.locator("div[data-testid='roomlisting']", has_text=room_name).first

    # This method edits an existing room with the provided parameters
    def edit_room(
            self,
            room_name="Edited Room",
            type_value="Double",
            accessible_value="false",
            room_price="200",
            expected_name=None,
            wifi=False,
            tv=False,
            radio=False,
            refresh=False,
            safe=False,
            views=False
    ):
        try:
            self.safe_fill(self.room_name_input_in_edit, room_name)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to fill room name: {e}")

        try:
            self.safe_select(self.type_select_in_edit, type_value)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to select room type: {e}")

        try:
            self.safe_select(self.Accessible_select_in_edit, accessible_value)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to select accessibility: {e}")

        try:
            self.safe_fill(self.room_price_input_in_edit, room_price)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to fill room price: {e}")

        try:
            self.set_checkbox_state(self.wifi_checkbox_in_edit, wifi)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to set WiFi checkbox: {e}")

        try:
            self.set_checkbox_state(self.refresh_checkbox_in_edit, refresh)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to set refresh checkbox: {e}")

        try:
            self.set_checkbox_state(self.tv_checkbox_in_edit, tv)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to set TV checkbox: {e}")

        try:
            self.set_checkbox_state(self.sale_checkbox_in_edit, safe)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to set safe checkbox: {e}")

        try:
            self.set_checkbox_state(self.views_checkbox_in_edit, views)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to set views checkbox: {e}")

        try:
            self.set_checkbox_state(self.radio_checkbox_in_edit, radio)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to set radio checkbox: {e}")

        try:
            self.safe_click(self.update_button)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to click update button: {e}")

        # Build expected name string
        extras = []
        if wifi: extras.append("WiFi")
        if tv: extras.append("TV")
        if radio: extras.append("Radio")
        if refresh: extras.append("Refreshments")
        if safe: extras.append("Safe")
        if views: extras.append("Views")

        if expected_name is None:
            expected_name = f"{room_name}{type_value}{accessible_value}{room_price}"
            expected_name += ", " + ", ".join(extras) if extras else "No features added to the room"

        # Navigate back to the room list
        try:
            self.safe_click(self.rooms_button)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to click the rooms button: {e}")

        # Verify room updated correctly
        try:
            expect(self.get_room_by_name(expected_name)).to_be_visible(timeout=2000)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to verify room update: {e}")
