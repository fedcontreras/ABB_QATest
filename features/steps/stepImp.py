from behave import *
import requests
from utilities.configurations import getConfig
from utilities.resources import ApiResources


@given('the book title which we need to search')
def step_imp(context):
    context.expected_title = "You Don't Know JS"


@when('we execute the getBook method')
def step_impl(context):
    url = getConfig()['API']['endpoint'] + ApiResources.getBooks
    response = requests.get(url)
    context.response = response
    context.json_response = response.json()


@then('the book is successfully listed')
def step_impl(context):
    BookList = context.json_response['books']
    found_book = None
    for book in BookList:
        if book['title'] == context.expected_title:
            found_book = book
            break
    assert found_book['title'] == context.expected_title
