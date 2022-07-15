from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AddWeightPage(BasePage):
    SAVE_BUTTON = [AppiumBy.ID, 'action_save']
    VALUES = [AppiumBy.ID, 'value']  # More than one element

    def verify_page(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((self.VALUES[0], self.VALUES[1])))

    def enter_weight(self, weight):
        value_elements = self.find_elements(self.VALUES)
        self.send_keys(value_elements[0], weight)

    def enter_fat_mass(self, fat_mass):
        value_elements = self.find_elements(self.VALUES)
        self.send_keys(value_elements[1], fat_mass)

    def tap_save_button(self):
        self.tap_on_element(self.SAVE_BUTTON)
