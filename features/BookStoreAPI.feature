Feature: Verify if Books are listed, added, and deleted using Library API

  Scenario: Verify if a user can search for a book
    Given the book title which we need to search
    When we execute the getBook method
    Then  the book is successfully listed


  Scenario: Verify if a user can log in with a valid username and password
    Given A user with a valid username and password
    When  we execute the Authentication method
    Then  the user is logged in


  Scenario: Authorized user is able to Add a book
    Given A book is available
    When  I add a book to the store
    Then  the book is successfully added


    Scenario: Authorized user is able to Remove a book
    Given A list of books are available
    When  I remove a book to the store
    Then  the book is successfully deleted


