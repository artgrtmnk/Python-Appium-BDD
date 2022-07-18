from behave import given, when, then

@given(u'user launched the app')
def step_impl(context):
    context.home_page.verify_page()

