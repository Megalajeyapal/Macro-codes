Feature: Fire alarm report to fire panel
Scenario: Zone Fire reported in fire panel
Given simulator running
 When fire alarm reported
Then alarm details in fire event screen