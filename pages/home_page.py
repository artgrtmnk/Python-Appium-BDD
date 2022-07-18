from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import Helpers
from pages.base_page import BasePage

class HomePage(BasePage):
    PAGE_IDENTIFIER = [AppiumBy.ID, 'recyclerview_home']
    PLUS_SIGN = [AppiumBy.ID, 'action_add_metric']
    WEIGHT_BLOCK = [AppiumBy.ID, 'metric_weight']
    WEIGHT_VALUE = [AppiumBy.ID, 'value']
    FAT_MASS_VALUE = [AppiumBy.ID, 'secondary_value']

    def verify_page(self):
        self.find_element(self.PAGE_IDENTIFIER)

    def tap_plus_sign(self):
        self.tap_on_element(self.PLUS_SIGN)

    def __get_weight_value(self):
        parent_element = self.find_element(self.WEIGHT_BLOCK)
        return parent_element.find_element(self.WEIGHT_VALUE[0], self.WEIGHT_VALUE[1]).text

    def __get_fat_mass_value(self):
        parent_element = self.find_element(self.WEIGHT_BLOCK)
        return parent_element.find_element(self.FAT_MASS_VALUE[0], self.FAT_MASS_VALUE[1]).text

    def compare_weight(self, weight_from_feature):
        weight_from_homepage = Helpers.parse_weight(self.__get_weight_value())
        weight_from_feature = float(weight_from_feature)

        assert weight_from_homepage == weight_from_feature

    def compare_fat_mass(self, fat_mass_from_feature):
        fat_mass_from_homepage = Helpers.parse_weight(self.__get_fat_mass_value())
        fat_mass_from_feature = float(fat_mass_from_feature)

        assert fat_mass_from_homepage == fat_mass_from_feature
