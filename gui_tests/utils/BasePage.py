class BasePage:
    def __init__(self, page):
        self.page = page

    def safe_fill(self, locator, value):
        # Safely fills a text input field after ensuring it is visible
        try:
            locator.wait_for(state="visible")
            locator.fill(value)
        except Exception as e:
            raise Exception(f"Failed to fill: {e}")

    def safe_click(self, locator):
        # Safely clicks on an element after ensuring it is visible
        try:
            locator.wait_for(state="visible")
            locator.click()
        except Exception as e:
            raise Exception(f"Failed to click: {e}")

    def safe_select(self, locator, value):
        # Safely selects a value from a dropdown element
        try:
            locator.wait_for(state="visible")
            locator.select_option(value)
        except Exception as e:
            raise Exception(f"Failed to select: {e}")

    def assert_element_text(self, locator, expected_text):
        # Waits for the element to be visible and verifies that its text matches the expected text
        try:
            locator.wait_for(state="visible")
            actual = locator.text_content()
            assert actual == expected_text, f"Expected '{expected_text}' but got '{actual}'"
        except Exception as e:
            raise Exception(f"validation failed: {e}")

    def element_exists(self, locator):
        # Checks if an element is attached to the DOM (exists on the page)
        try:
            locator.wait_for(state="attached", timeout=1000)
            return True
        except:
            return False

    def safe_check_radio(self, locator):
        # Safely checks a radio button and verifies it is selected
        try:
            locator.wait_for(state="visible")
            locator.check()
            assert locator.is_checked(), f" radio button was not selected"
        except Exception as e:
            raise Exception(f"Failed to : {e}")

    def set_checkbox_state(self, locator, should_be_checked: bool):
        try:
            locator.wait_for(state="visible")
            is_checked = locator.is_checked()
            if should_be_checked and not is_checked:
                locator.check()
                assert locator.is_checked(), f"Checkbox was not selected as expected"
            elif not should_be_checked and is_checked:
                locator.uncheck()
                assert not locator.is_checked(), f"Checkbox was not unselected as expected"
        except Exception as e:
            raise Exception(f"Failed to set checkbox state: {e}")
