# ABB - QA Test

## Task 1 - Comments to the Product Owner (PO): :space_invader:

#### About the User Story Definition:

The User story is clear and concise, but there are some points we need to clarify.
- Clarify if the search functionality should be limited to specific fields (Title, Author, Publisher) or if it should search across all book attributes.
- Specify whether the search should be case-sensitive or case-insensitive.
- Confirm if there are any limitations or constraints on the search input. 

  a. Minimum query lenght (how many letters to start searching).

  b. Maximum query lenght.

  c. Maximum number of results to display (Is pagination available?).

  d. Support special characters and numbers.

  e. Support multi-language search.

- Specify if there is a sorting order of the search results (alphabetically for the title, author, or Publisher - for relevance)
- Specify if there are any search filters.

#### About Acceptance Criteria:

The Acceptance criteria are well defined and provide clear expectations, but there are some points we should check.
- Specify the sorting or ordering of the search results.
- Determine if partial matches should be considered when displaying the search results.
- Clarify the desired behavior when no matching books are found or when the search input is invalid.

## Task 2 - Test Cases: :soccer:

| **Title** | **Description** | **Precondition** | **Steps** |  **Expected Result** | Post-Condition | Priority |
| -------: | :------: | :------ | :------ | :------ |-------: | -------: | 
| Test 1 - Search Screen| Verify the presence of search field in the book catalog | N/A | 1. Go to the BookStore Web Page | The search field is displayed like a free text input with a search button | N/A | Medium |
| Test 2 - Search Field| Verify that the search field accepts free text input | Enter valid characters in the search field | 1. Enter a name of a book | The entered text is visible in the search field | N/A | High |
| Test 3 - Refresh Search field| Verify that the search results are updated while typing in the search field | Write at least two letters to start the search | 1. Enter one letter at a time until you reach five | The result list is refreshed with books matching the search input| N/A | Medium| 
| Test 4 - Search a book by Title | Verify that the search functionality searches by Title | Verify that the book is in the Database | 1. Enter the name of an existing book | The Book matching the search input is displayed | N/A | High |
| Test 5 - Search a book by All atributes | Verify that the search functionality searches across all book attributes | There is a book with all the values in the Database | 1. Search a book by Title, Author & Publisher | Books matching the search input are displayed, regardless of the attribute being searched | N/A | High |
| Test 6 - Search with Uppercase | Verify the case sensitivity of the search functionality | At least one letter must be uppercase | 1. Enter the name of an existing book with a letter in upper case  | Confirm if the search is case-sensitive or case-insensitive | N/A | Medium |
| Test 7 - Check Search Sorting | Verify the sorting or ordering of search results | There is a book name with many different authors in the Database | 1. Enter the name of a book that has different authors  | Confirm the desired sorting order of the search results | N/A | Low |
| Test 8 - Search with a partial value| Verify the handling of partial matches in search results| The book is in the Database| 1. Enter the last two letters of an existing book name | Determine if partial matches are included in the search results | N/A | High |
| Test 9 - Search a non existing book | Verify the behavior when no matching books are found | The book doesn't exist in the Database | 1. Enter the name of a non existing book| Confirm the expected behavior when no books match the search input | N/A | Medium |
| Test 10 - Search with special characters | Verify the behavior when the search input is invalid | N/A | 1. Enter the name of a book with special characters | Determine the expected response or error handling for invalid search inputs | N/A | Medium |
| Test 11 - Search with only one letter | Verify that the search is not executed | N/A | 1. Enter only one letter | The search doesn't display any value | N/A | Low | 
| Test 12 - Search a book with number in his title | Verify if the search allow numbers in the search | N/A | 1. Enter a title that has number in it | The search display the books who has number in the title | N/A | Medium | 

## Task 3 - Automate REST API Books endpoint: :robot:

Swagger = [demoqa.com/swagger/#/](url)

