Feature: Field bus communication fault and reset condition
Scenario: Make system fault free quiescent state with one field bus connected state
Given Make sure configuration for the field bus module is present in the system
 And connect the field bus to the respective slot
 When start the panel
 And wait for a minute
Then ensure there is new field bus found in slot xx information event registered in event log
 And wait for a minute
 Then ensure there is no fault from respective slot field bus in the panel
Scenario: Remove a field bus from port
Given let panel working with 2 field bus in normal condition
 When Disconnect the RJ45 connector from first field bus
 And wait for a event from above slot and note the event reported time as performance report
Then ensure there is a fault in the panel as "System Sensor module disconnected from slot X in panel Y"
Scenario: RESET the field bus communication fault
Given let panel working with 2 field bus in normal condition
 When Disconnect the RJ45 connector from first field bus
 And wait for a minute
 And Perform 'FAULT RESET' from Panel RESET button
Then ensure there is a fault is cleared in the panel says System SAFE
Scenario: Reconnect field bus to the disconnected port
Given let panel working with 2 field bus in communication fault condition
 When Reconnect field bus in the first port
 And wait for a minute and don't RESET the panel
 And ensure in event log as field bus found information event registered
Then ensure there is a fault exist in the panel as "System sensor module disconnected from slot X in panel Y"
Scenario: Disconnect field bus for the second time from the port and reset fault
Given let panel working with field bus in communication fault condition
 When Disconnect the RJ45 connector from first field bus
 And wait for a minute
Then ensure there is a fault in the panel as "System sensor module disconnected from slot X in panel Y"
 And reconnect the field bus to disconnected port.
 And Perform 'FAULT RESET' from Panel RESET button
 Then ensure field bus communication fault is cleared in the panel says System SAFE
Scenario: Check system normal with fully populated field bus in the panel
Given let panel working with field bus in normal condition
 When Disconnect the RJ45 connector from all field bus
 And wait for a minute
Then ensure all field bus reports the communication fault in the panel as "System sensor module disconnected from slot X in panel Y"
 And reconnect the field bus to disconnected port.
 And Perform 'FAULT RESET' from Panel RESET button
 Then ensure field bus communication fault is cleared in the panel says System SAFE
Scenario: Check communication fault from field bus which is not connected
Given let panel working with all field bus in normal condition
 When Disconnect the RJ45 connector from 3 field bus
 And wait for a minute
Then ensure multiple fault in the panel dependent upon number of loop module as "System sensor module disconnected from slot X in panel Y"
 And reconnect one field bus to disconnected port.
 And Perform 'FAULT RESET' from Panel RESET button
 Then ensure one field bus communication fault is cleared and other two field bus should still report "System Sensor module disconnected from slot XX in panel Y"