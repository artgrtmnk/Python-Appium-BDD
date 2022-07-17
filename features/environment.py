import glob
import os
from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from allure_behave.hooks import allure_report
from appium import webdriver

from pages.home_page import HomePage
from pages.add_weight_page import AddWeightPage
from pages.record_page import RecordPage


def before_feature(context, feature):
    reports = glob.glob('features/artifacts/reports/*')
    screenshots = glob.glob('features/artifacts/screenshots/*')
    folders = [reports, screenshots]

    try:
        for folder in folders:
            for file in folder:
                os.remove(file)
    except:
        pass

    context.driver = webdriver.Remote(
        # you need to specify your ip and port in the next line if it is different (same as in Appium)
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "",  # you need to specify your Android version
            "deviceName": "",  # you need to specify your Device name
            "udid": "",  # you need to specify your udid
            "appActivity": "com.withings.wiscale2.MainActivity",
            "appPackage": "com.withings.wiscale2",
            "noReset": "true",
            "fullReset": "false"
        }
    )

    # Page objects definition
    context.home_page = HomePage(context)
    context.add_weight_page = AddWeightPage(context)
    context.record_page = RecordPage(context)


def after_scenario(context, scenario):
    test_datetime = datetime.now().strftime("%d%m%Y%H%M%S")
    screenshot_name = f"{scenario.name}_{scenario.status}_{test_datetime}.png"

    context.driver.save_screenshot(f"features/artifacts/screenshots/{screenshot_name}")
    if scenario.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name=screenshot_name,
                      attachment_type=AttachmentType.PNG)


def after_feature(context, feature):
    context.driver.quit()
    allure_report("features/artifacts/reports")
