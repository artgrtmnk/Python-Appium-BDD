from appium import webdriver
from allure_behave.hooks import allure_report
from datetime import datetime
import glob
import os


def before_feature(context, feature):
    try:
        files = glob.glob('features/artifacts/*')
        for f in files:
            os.remove(f)
    except:
        pass

    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "12",
            "deviceName": "S21 Artem",
            "udid": "R5CR82BS9WV",
            "appActivity": "com.withings.wiscale2.MainActivity",
            "appPackage": "com.withings.wiscale2",
            "noReset": "true",
            "fullReset": "false"
        }
    )


def after_scenario(context, feature):
    test_datetime = datetime.now().strftime("%d%m%Y%H%M%S")
    context.driver.save_screenshot("features/artifacts/success %s.png" % test_datetime)


def after_feature(context, feature):
    context.driver.quit()
    allure_report("features/artifacts")
