Feature: Access the fire panel as a operator
Scenario: Access fire panel as a Operator with valid password
Given fire panel up and running
When select menu for login
Then select the operator and enter password
Scenario:
Access fire panel as a Operator with invalid password
Given fire panel up and running
When select menu for login
Then select the operator and invalid password
