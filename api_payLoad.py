def authorizationPayLoad(userName, password):
    body = {
        "userName": userName,
        "password": password
    }
    return body


def addBookPayLoad(isbn):
    body = {
        "userId": "testtest",
        "collectionOfIsbns": [
            {
                "isbn": isbn
            }
        ]
    }
    return body
