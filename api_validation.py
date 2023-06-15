import requests
import json
import configparser
from utilities.configurations import *
from utilities.resources import *
from api_payLoad import *

# Get book

url = getConfig()['API']['endpoint'] + ApiResources.getBooks
response = requests.get(url,)
json_response = response.json()

BookList = json_response['books']
expected_title = "You Don't Know JS"
found_book = None
for book in BookList:
    if book['title'] == expected_title:
        found_book = book
        break

assert found_book['title'] == expected_title


# Authentication:


# Session Managing:
se = requests.session()
se.auth = auth = ('testtest', getPassword())


url = getConfig()['API']['endpoint'] + ApiResources.Authorization
headers = {"Content-Type": "application/json"}
auth_response = requests.post(url, json=authorizationPayLoad("testtest", "Test123!"), headers=headers, )
print(auth_response.status_code)
json_authResponse = auth_response.json()
print(json_authResponse)
assert auth_response.status_code == 200
assert json_authResponse == True


# Add Book

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
add_response = se.post(url, json=addBookPayLoad("9781593277574"), headers=headers, )
print(add_response.status_code)
