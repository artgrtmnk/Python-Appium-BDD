from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, context):
        self.driver = context.driver

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_element(loc[0], loc[1])
        except Exception as e:
            print("Can't find an element.")
            raise e

    def find_elements(self, loc):
        try:
            return self.driver.find_elements(loc[0], loc[1])
        except Exception as e:
            print("Can't find elements.")
            raise e

    def send_keys(self, loc, value):
        if isinstance(loc, list):
            self.driver.find_element(loc[0], loc[1]).click()
            self.driver.find_element(loc[0], loc[1]).clear()
            self.driver.find_element(loc[0], loc[1]).send_keys(value)
        else:
            loc.click()
            loc.clear()
            loc.send_keys(value)

    def tap_on_element(self, loc):
        self.driver.find_element(loc[0], loc[1]).click()

