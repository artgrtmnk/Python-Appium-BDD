from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class RecordPage(BasePage):
    PAGE_IDENTIFIER = [AppiumBy.XPATH, "//*[contains(@text, ', what would you like to record?')]"]
    WEIGHT_OPTION = [AppiumBy.ID, 'add_weight']

    def verify_page(self):
        self.find_element(self.PAGE_IDENTIFIER)

    def tap_weight_option(self):
        self.tap_on_element(self.WEIGHT_OPTION)
