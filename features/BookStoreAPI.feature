# Created by fedco at 14/06/2023
Feature: Verify if Books are listed, added, and deleted using Library API
  # Enter feature description here

  Scenario: Verify getBook API functionality
    Given the book title which we need to search
    When we execute the getBook method
    Then  the book is successfully listed
