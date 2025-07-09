from playwright.sync_api import expect

from gui_tests.utils.BasePage import BasePage


class RoomPage(BasePage):
    """Room page."""

    def __init__(self, page):
        super().__init__(page)
        self.room_name_input = page.locator('#roomName')
        self.type_select = page.locator('#type')
        self.Accessible_select = page.locator('#accessible')
        self.room_price_input = page.locator('#roomPrice')
        self.wifi_checkbox = page.locator('#wifiCheckbox')
        self.refresh_checkbox = page.locator('#refreshCheckbox')
        self.tv_checkbox = page.locator('#tvCheckbox')
        self.sale_checkbox = page.locator('#safeCheckbox')
        self.radio_checkbox = page.locator('#radioCheckbox')
        self.views_checkbox = page.locator('#viewsCheckbox')
        self.create_button = page.locator('#createRoom')
        self.check_room = page.locator("div[data-testid='roomlisting']", has_text="Test Room").first
        self.edit_button = self.page.locator("button", has_text="Edit")

    # This method returns the first room listing element that matches the given room name
    def get_room_by_name(self, room_name):
        return self.page.locator("div[data-testid='roomlisting']", has_text=room_name).first

    # This method builds a new room with the provided parameters and verifies its creation
    def build_new_room_and_verify(
            self,
            room_name="Test Room",
            type_value="Family",
            accessible_value="true",
            room_price="100",
            expected_name=None,
            wifi=True,
            tv=True,
            radio=True,
            refresh=True,
            safe=True,
            views=True
    ):
        # Fill in the room name
        try:
            self.safe_fill(self.room_name_input, room_name)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to fill room name: {e}")

        # Select the room type from dropdown
        try:
            self.safe_select(self.type_select, type_value)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to select room type: {e}")

        # Select accessibility option (true/false)
        try:
            self.safe_select(self.Accessible_select, accessible_value)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to select accessibility: {e}")

        # Fill in the room price
        try:
            self.safe_fill(self.room_price_input, room_price)
        except Exception as e:
            raise Exception(f"[ERROR] Failed to fill room price: {e}")

        if wifi:
            self.safe_click(self.wifi_checkbox)
        if refresh:
            self.safe_check_radio(self.refresh_checkbox)
        if tv:
            self.safe_check_radio(self.tv_checkbox)
        if safe:
            self.safe_check_radio(self.sale_checkbox)
        if views:
            self.safe_check_radio(self.views_checkbox)
        if radio:
            self.safe_check_radio(self.radio_checkbox)

        self.safe_click(self.create_button)

        if expected_name is None:
            extras = []
            if wifi: extras.append("WiFi")
            if tv: extras.append("TV")
            if radio: extras.append("Radio")
            if refresh: extras.append("Refreshments")
            if safe: extras.append("Safe")
            if views: extras.append("Views")

            extras_str = ", ".join(extras)
            expected_name = f"{room_name}{type_value}{accessible_value}{room_price}"
            if extras:
                expected_name += extras_str if extras_str.startswith(",") else f"{extras_str}"
        # Verify the room is created
        room = self.get_room_by_name(expected_name)
        print(f"[DEBUG] Room created with name: {expected_name}")
        print(f"[DEBUG] Room locator: {room}")
        expect(room).to_be_visible()

    # This method deletes a room by its name and verifies it is no longer visible
    def delete_room_and_verify(self, room_name: str):
        room = self.get_room_by_name(room_name)
        delete_button = room.locator("span.fa-remove")
        self.safe_click(delete_button)
        expect(room).not_to_be_visible()

    # This method clicks the edit button for a specific room
    def click_edit_room(self, room_name):
        room = self.get_room_by_name(room_name)
        self.safe_click(room)
        self.safe_click(self.edit_button)
