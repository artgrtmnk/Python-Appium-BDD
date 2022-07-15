from behave import given, when, then
from pages.home_page import HomePage
from pages.record_page import RecordPage
from pages.add_weight_page import AddWeightPage


@given(u'the app is launched')
def step_impl(context):
    home_page = HomePage(context)
    home_page.verify_page()


@when(u'tap on plus sign in the top right corner')
def step_impl(context):
    home_page = HomePage(context)
    home_page.tap_plus_sign()


@then(u'record screen is opened')
def step_impl(context):
    record_page = RecordPage(context)
    record_page.verify_page()


@when(u'tap on Weight')
def step_impl(context):
    record_page = RecordPage(context)
    record_page.tap_weight_option()


@then(u'add weight screen is opened')
def step_impl(context):
    add_weight_page = AddWeightPage(context)
    add_weight_page.verify_page()


@when(u'enter "{weight}" in the weight field')
def step_impl(context, weight):
    add_weight_page = AddWeightPage(context)
    add_weight_page.enter_weight(weight)
    print('weight')


@when(u'enter "{fat_mass}" in the fat mass field')
def step_impl(context, fat_mass):
    add_weight_page = AddWeightPage(context)
    add_weight_page.enter_fat_mass(fat_mass)


@when(u'tap save button')
def step_impl(context):
    add_weight_page = AddWeightPage(context)
    add_weight_page.tap_save_button()


@then(u'home screen is opened')
def step_impl(context):
    home_page = HomePage(context)
    home_page.verify_page()


@then(u'weight is "{weight}"')
def step_impl(context, weight):
    home_page = HomePage(context)
    home_page.compare_weight(weight)


@then(u'fat mass is "{fat_mass}"')
def step_impl(context, fat_mass):
    home_page = HomePage(context)
    home_page.compare_fat_mass(fat_mass)
