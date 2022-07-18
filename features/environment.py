import glob
import os
from datetime import datetime
import json
from types import SimpleNamespace

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

    capabilities_json = open('capabilities.json')
    data = json.dumps(json.load(capabilities_json))
    capabilities_parsed = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    if capabilities_parsed.desired_capabilities.platformVersion == 'your_platform_version' \
            or capabilities_parsed.desired_capabilities.deviceName == 'your_device_name' \
            or capabilities_parsed.desired_capabilities.udid == 'your_udid':
        raise Exception('Specify your capabilities in capabilities.json in the root folder!')

    context.driver = webdriver.Remote(
        command_executor=capabilities_parsed.command_executor,
        desired_capabilities={
            "platformName": capabilities_parsed.desired_capabilities.platformName,
            "platformVersion": capabilities_parsed.desired_capabilities.platformVersion,
            "deviceName": capabilities_parsed.desired_capabilities.deviceName,
            "udid": capabilities_parsed.desired_capabilities.udid,
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
