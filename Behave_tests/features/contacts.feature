Feature: Manage contacts

  Scenario: Create a new contact
    Given the API is running
    When I create a contact with first name "John", last name "Doe", phone number "1234567890", and description "Test user"
    Then the contact should be created successfully
    And the response should contain the contact's id

  Scenario: Retrieve a contact
    Given the API is running
    When I create a contact with first name "Jane", last name "Doe", phone number "0987654321"
    And I retrieve the contact by first name "Jane" and last name "Doe"
    Then the contact should be found
    And the contact's phone number should be "0987654321"

  Scenario: Update a contact
    Given the API is running
    When I create a contact with first name "Alice", last name "Smith", phone number "1112223333"
    And I update the contact's first name to "Alicia"
    Then the contact's first name should be "Alicia"

  Scenario: Delete a contact
    Given the API is running
    When I create a contact with first name "Bob", last name "Brown", phone number "4445556666"
    And I delete the contact by first name "Bob" and last name "Brown"
    Then the contact should not be found
