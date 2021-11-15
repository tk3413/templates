from behave import *
from src.hello import hello

@given("we have some code")
def step_impl(context):
    print("HELLO")
    pass


@when("it is called")
def step_impl(context):
    context.result = hello(name="taimore")
    print("result is: {}".format(context.result))

@then("we are able to validate the result")
def step_impl(context):
    assert True == True
