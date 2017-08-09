# -*- coding: utf-8 -*-
import __builtin__
import multiprocessing
import time

@Given("fire panel up and running")
@When("fire panel up and running")
def main(context):   
    startApplication("HMI")
    time.sleep(3)
    mouseClick(waitForObject(":_Image"), 468, 198, Qt.LeftButton)
    time.sleep(3)
    waitFor("object.exists(':_QQuickView')", 20000)
    pass#test.compare(findObject(":_QQuickView").active, False)
  
@When("select menu for login")
def select_menu_for_login(context):
    mousePress(waitForObject(":_Image"), 211, 164, Qt.LeftButton)    #mouseClick(waitForObject(":INFORMATION_TextShadow
    waitFor("object.exists(':menuElement_TopbarButton')", 20000)
    time.sleep(6)
    test.compare(findObject(":menuElement_TopbarButton").buttonID, 1)
#mouseClick(waitForObject(":menuElement_TopbarButton"), 37, 22, Qt.LeftButton)
    pass
@Then("select the operator and enter password")
@When("select the operator and enter password")
def select_the_operator_and_enter_password(context):
    #mouseClick(waitForObject(":_Image"), 227, 213, Qt.LeftButton)
    time.sleep(10)
    mouseClick(waitForObject(":menuElement_TopbarButton"),20000)
    mouseClick(waitForObject(":menuElement_TopbarButton"), 23, 30, Qt.LeftButton)
    time.sleep(6)
    waitFor("object.exists(':LOGIN_TextShadow')", 20000)
    test.compare(findObject(":LOGIN_TextShadow").enabled, True)
    test.compare(str(findObject(":LOGIN_TextShadow").id), "nameText")
    mouseClick(waitForObject(":LOGIN_TextShadow"))
    time.sleep(10)
    doubleClick(waitForObject(":1_TextShadow"))
    time.sleep(4)
    mouseClick(waitForObject(":keyIcon_Image"), 27, 21, Qt.LeftButton)
    time.sleep(8)
    time.sleep(6)
    waitFor("object.exists(':accessElement_TopbarButton')", 20000)
    test.compare(str(findObject(":accessElement_TopbarButton").id), "accessElement")
    pass
    
@Then("select the operator and invalid password")
def select_the_operator_and_invalid_password(context):
    mouseClick(waitForObject(":menuElement_TopbarButton"), 32, 22, Qt.LeftButton)
    time.sleep(04)
    mouseClick(waitForObject(":LOGIN_TextShadow"))
    time.sleep(3)
    mouseClick(waitForObject(":1_TextShadow"))
    time.sleep(3)
    mouseClick(waitForObject(":keyIcon_Image"), 27, 21, Qt.LeftButton)
    time.sleep(3)
    waitFor("object.exists(':Invalid Password_TextShadow')", 20000)
    #time.sleep(4)
    #test.compare(findObject(":Invalid Password_TextShadow").id)
    #test.compare(str(findObject(":Invalid Password_TextShadow").id), "Invalid Password")
    #waitFor("object.exists(':accessElement_TopbarButton')", 20000)
    #test.compare(str(findObject(":accessElement_TopbarButton").id), "accessElement")
    pass


def accesslevel1(context):
    #mouseClick(waitForObject(":_Image"), 227, 213, Qt.LeftButton)
    time.sleep(10)
    mouseClick(waitForObject(":menuElement_TopbarButton"),20000)
    mouseClick(waitForObject(":menuElement_TopbarButton"), 23, 30, Qt.LeftButton)
    time.sleep(6)
    waitFor("object.exists(':LOGIN_TextShadow')", 20000)
    test.compare(findObject(":LOGIN_TextShadow").enabled, True)
    test.compare(str(findObject(":LOGIN_TextShadow").id), "nameText")
    mouseClick(waitForObject(":LOGIN_TextShadow"))
    time.sleep(10)
    doubleClick(waitForObject(":1_TextShadow"))
    time.sleep(4)
    mouseClick(waitForObject(":keyIcon_Image"), 27, 21, Qt.LeftButton)
    time.sleep(8)
    time.sleep(6)
    waitFor("object.exists(':accessElement_TopbarButton')", 20000)
    test.compare(str(findObject(":accessElement_TopbarButton").id), "accessElement")
    pass 
@When("select menu")
def select_menu(context):
    mouseClick(waitForObject(":_Image"), 211, 164, Qt.LeftButton)
    #mouseClick(waitForObject(":menuElement_TopbarButton"), 41, 23, Qt.LeftButton)
    #mouseClick(waitForObject(":INFORMATION_TextShadow"))
    time.sleep(5)
    waitFor("object.exists(':menuElement_TopbarButton')", 20000)
    test.compare(findObject(":menuElement_TopbarButton").buttonID, 1)
#mouseClick(waitForObject(":menuElement_TopbarButton"), 37, 22, Qt.LeftButton)
    pass 
@Then("ensure all menu items")
def ensure_all_menu_items(context):
    test.warning("TODO implement some action is performed")

@Given("Fire panel_Login as operator")
def Login_as_operator(context):
    startApplication("/home/manikandan/HMI")
    mouseClick(waitForObject(":_Image"), 233, 243, Qt.LeftButton)
    waitFor("object.exists(':homestatus_Rectangle')", 20000)
    test.compare(str(findObject(":homestatus_Rectangle").id), "homestatus")
    mouseClick(waitForObject(":menuElement_TopbarButton"), 48, 30, Qt.LeftButton)
    waitFor("object.exists(':menuElement_TopbarButton')", 20000)
    time.sleep(2)
    test.compare(str(findObject(":menuElement_TopbarButton").id), "menuElement")
    
    #mouseClick(waitForObject(":menuElement_TopbarButton"), 51, 36, Qt.LeftButton)
    waitFor("object.exists(':LOGIN_TextShadow')", 20000)
    time.sleep(2)
    mouseClick(Object(":LOGIN_TextShadow"))
    time.sleep(2)
    mouseClick(waitForObject(":_KeyDelegate"), 34, 53, Qt.LeftButton)
    time.sleep(3)
    mouseClick(waitForObject(":keyIcon_Image"), 27, 21, Qt.LeftButton) 
    time.sleep(2)
    waitFor("object.exists(':Invalid Password_TextShadow')", 20000)
    time.sleep(2)
    test.compare(str(findObject(":Invalid Password_TextShadow").id), "invalidUserNameOrPassword")
    #mouseClick(waitForObject(":menuElement_TopbarButton"), 32, 22, Qt.LeftButton)
    #mouseClick(waitForObject(":LOGIN_TextShadow"))
    #doubleClick(waitForObject(":1_TextShadow"))
    #mouseClick(waitForObject(":keyIcon_Image"), 11, 17, Qt.LeftButton)
    #waitFor("object.exists(':accessElement_TopbarButton')", 20000)
    test.compare(str(findObject(":accessElement_TopbarButton").id), "accessElement")
    pass

@Then("check child items")
def Check_child_items(context):
    mouseClick(waitForObject(":menuElement_TopbarButton"), 35, 28, 134217728, Qt.LeftButton)
    waitFor("object.exists(':_QQuickView')", 20000)
    test.compare(findObject(":_QQuickView").active, True)
    test.compare(findObject(":_QQuickView").status, 1)
    mouseClick(waitForObject(":_Image"), 56, 52, Qt.LeftButton)
    mouseClick(waitForObject(":menuElement_TopbarButton"), 29, 18, Qt.LeftButton)
    mouseClick(waitForObject(":LOGIN_TextShadow"))
    doubleClick(waitForObject(":_KeyDelegate_2"), 70, 39, Qt.LeftButton)
    mouseClick(waitForObject(":keyIcon_Image"), 13, 12, Qt.LeftButton)
    mouseClick(waitForObject(":menuElement_TopbarButton"), 33, 26, Qt.LeftButton)
    mouseClick(waitForObject(":list_MenuDelegate_2"), 75, 12, Qt.LeftButton)
    waitFor("object.exists(':_QQuickView')", 20000)
    test.compare(findObject(":_QQuickView").active, True)
    test.compare(findObject(":_QQuickView").contentItem.enabled, True)
  

    
@When("Fire alarm reported in panel and User selected the SILENCE SOUNDER button")
def Fire_alarm_reported_in_panel_and_User_selected_the_SILENCE_SOUNDER_button(context):
    test.warning("TODO implement Fire alarm reported in panel and User selected the SILENCE SOUNDER button")

@Then("SILENCE SOUNDER Has been performed from SYS no - warning message should appear and stay for 20 seconds")
def SILENCE_SOUNDER_Has_been_performed_from_SYS_no_warning_message_should_appear_and_stay_for_20_seconds(context):
    test.warning("TODO implement SILENCE SOUNDER Has been performed from SYS no - warning message should appear and stay for 20 seconds.")

@When("User selected the SILENCE SOUNDER button")
def step3(context):
    test.warning("TODO implement User selected the SILENCE SOUNDER button")

@Then("SILENCE SOUNDER Has been performed from SYS no - warning message should disappear, Fire alarm event screen should list new alarm")
def step4(context):
    test.warning("TODO implement SILENCE SOUNDER Has been performed from SYS no - warning message should disappear, Fire alarm event screen should list new alarm")

@Given ("simulator running")
def simulator(self):
    client1 = startApplication("/home/manikandan/FlexEsQuad/Quadltib/User/Harisha/build-NetworkInterFace-Desktop_Qt_5_5_1_GCC_32bit-Release/NetworkInterFace")
    #startApplication("NetworkInterFace")
    testSettings.setWrappersForApplication("NetworkInterFace", ("Qt","CanvasWrapper"))
    client2 = startApplication("HMI")
    setApplicationContext(client1)

    mouseClick(waitForObject(":Send event_Text"), 53, 10, 0, Qt.LeftButton)
    openContextMenu(waitForObject(":Send event_Text"), 52, 10, 0)
    waitFor("object.exists(':_QmlApplicationViewer')", 20000)
    test.compare(findObject(":_QmlApplicationViewer").enabled, True)
    test.compare(findObject(":_QmlApplicationViewer").focus, False)


#     mouseClick(waitForObject(":eventTypeSelect_Rectangle"), 215, 20, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":eventTypeList.delegate_Rectangle"), 119, 23, 0, Qt.LeftButton)
#     waitFor("object.exists(':_QmlApplicationViewer')", 20000)
#     test.compare(str(findObject(":_QmlApplicationViewer").accessibleName), "")
#     time.sleep(5)
#     mouseClick(waitForObject(":eventTypeList.delegate_Rectangle"), 76, 14, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":delegate.Pre-Alarm_Text"), 80, 17, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":Pre-Alarm_Text"), 57, 23, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":delegate.Alarm_Text"), 38, 8, 0, Qt.LeftButton)
#     mouseClick(waitForObject(":Send event_Text"), 60, 15, 0, Qt.LeftButton)
#     waitFor("object.exists(':sendEventButton_Rectangle')", 20000)
#     test.compare(str(findObject(":sendEventButton_Rectangle").id), "sendEventButton")
#     test.compare(findObject(":sendEventButton_Rectangle").enabled, True)
    setApplicationContext(client2)
    mouseClick(waitForObject(":firealarmScreen_AlarmScreen"), 303, 279, Qt.LeftButton)
    
@When("fire alarm reported")
def fire_alarm_reported(context):   
    
    time.sleep(10)
    mouseClick(waitForObject(":firealarmScreen_AlarmScreen"), 303, 279, Qt.LeftButton)
    pass
@Then ("the results should be as expected")
def Then_the_results_should_be_as_expected(context):
    test.warning("TODO implement Make sure configuration for the field bus module is present in the system")
    
@Given("Make sure configuration for the field bus module is present in the system")
def Make_sure_configuration_for_the_field_bus_module_is_present_in_the_system(context):
    test.warning("TODO implement Make sure configuration for the field bus module is present in the system")

@Given("connect the field bus to the respective slot")
def connect_the_field_bus_to_the_respective_slot(context):
    test.warning("TODO implement connect the field bus to the respective slot")

@When("start the panel")
def start_the_panel(context):
    test.warning("TODO implement start the panel")

@When("wait for a minute")
def wait_for_a_minute(context):
    test.warning("TODO implement wait for a minute")

@Then("ensure there is new field bus found in slot xx information event registered in event log")
def ensure_there_is_new_field_bus_found_in_slot_xx_information_event_registered_in_event_log(context):
    test.warning("TODO implement ensure there is new field bus found in slot xx information event registered in event log")

@Then("wait for a minute")
def step(context):
    test.warning("TODO implement wait for a minute")

@Then("ensure there is no fault from respective slot field bus in the panel")
def ensure_there_is_no_fault_from_respective_slot_field_bus_in_the_panel(context):
    test.warning("TODO implement ensure there is no fault from respective slot field bus in the panel")

@Given("let panel working with 2 field bus in normal condition")
def let_panel_working_with_2_field_bus_in_normal_condition(context):
    test.warning("TODO implement let panel working with 2 field bus in normal condition")

@When("Disconnect the RJ45 connector from first field bus")
def Disconnect_the_RJ45_connector_from_first_field_bus(context):
    test.warning("TODO implement Disconnect the RJ45 connector from first field bus")

@When("wait for a event from above slot and note the event reported time as performance report")
def wait_for_a_event_from_above_slot_and_note_the_event_reported_time_as_performance_report(context):
    test.warning("TODO implement wait for a event from above slot and note the event reported time as performance report")

@Then("ensure there is a fault in the panel as \"System Sensor module disconnected from slot X in panel Y\"")
def step6(context):
    test.warning("TODO implement ensure there is a fault in the panel as \"System Sensor module disconnected from slot X in panel Y\"")

@When("Perform 'FAULT RESET' from Panel RESET button")
def step7(context):
    test.warning("TODO implement Perform 'FAULT RESET' from Panel RESET button")

@Then("ensure there is a fault is cleared in the panel says System SAFE")
def step8(context):
    test.warning("TODO implement ensure there is a fault is cleared in the panel says System SAFE")

@Given("let panel working with 2 field bus in communication fault condition")
def step9(context):
    test.warning("TODO implement let panel working with 2 field bus in communication fault condition")

@When("Reconnect field bus in the first port")
def Reconnect_field_bus_in_the_first_port(context):
    test.warning("TODO implement Reconnect field bus in the first port")

@When("wait for a minute and don't RESET the panel")
def wait_for_a_minute_and_dont_RESET_the_panel(context):
    test.warning("TODO implement wait for a minute and don't RESET the panel")

@When("ensure in event log as field bus found information event registered")
def step11(context):
    test.warning("TODO implement ensure in event log as field bus found information event registered")

@Then("ensure there is a fault exist in the panel as \"System sensor module disconnected from slot X in panel Y\"")
def step12(context):
    test.warning("TODO implement ensure there is a fault exist in the panel as \"System sensor module disconnected from slot X in panel Y\"")

@Given("let panel working with field bus in communication fault condition")
def step13(context):
    test.warning("TODO implement let panel working with field bus in communication fault condition")

@Then("ensure there is a fault in the panel as \"System sensor module disconnected from slot X in panel Y\"")
def step14(context):
    test.warning("TODO implement ensure there is a fault in the panel as \"System sensor module disconnected from slot X in panel Y\"")

@Then("reconnect the field bus to disconnected port.")
def step15(context):
    test.warning("TODO implement reconnect the field bus to disconnected port.")

@Then("Perform 'FAULT RESET' from Panel RESET button")
def step16(context):
    test.warning("TODO implement Perform 'FAULT RESET' from Panel RESET button")

@Then("ensure field bus communication fault is cleared in the panel says System SAFE")
def step17(context):
    test.warning("TODO implement ensure field bus communication fault is cleared in the panel says System SAFE")

@Given("let panel working with field bus in normal condition")
def step18(context):
    test.warning("TODO implement let panel working with field bus in normal condition")

@When("Disconnect the RJ45 connector from all field bus")
def step19(context):
    test.warning("TODO implement Disconnect the RJ45 connector from all field bus")

@Then("ensure all field bus reports the communication fault in the panel as \"System sensor module disconnected from slot X in panel Y\"")
def step20(context):
    test.warning("TODO implement ensure all field bus reports the communication fault in the panel as \"System sensor module disconnected from slot X in panel Y\"")

@Given("let panel working with all field bus in normal condition")
def step21(context):
    test.warning("TODO implement let panel working with all field bus in normal condition")

@When("Disconnect the RJ45 connector from 3 field bus")
def step22(context):
    test.warning("TODO implement Disconnect the RJ45 connector from 3 field bus")

@Then("ensure multiple fault in the panel dependent upon number of loop module as \"System sensor module disconnected from slot X in panel Y\"")
def step23(context):
    test.warning("TODO implement ensure multiple fault in the panel dependent upon number of loop module as \"System sensor module disconnected from slot X in panel Y\"")
@Then("reconnect one field bus to disconnected port.")
def reconnect_one_field_bus_to_disconnected_port(context):
    test.warning("TODO implement reconnect one field bus to disconnected port.")

@Then("ensure one field bus communication fault is cleared and other two field bus should still report \"System Sensor module disconnected from slot XX in panel Y\"")
def ensure_one_field_bus_communication_fault_is_cleared_and_other_two_field_bus_should_still_report(context):
    test.warning("TODO implement ensure one field bus communication fault is cleared and other two field bus should still report \"System Sensor module disconnected from slot XX in panel Y\"")

@When("After 4 seconds, New Fire Alarm reported in panel")
def step25(context):
    test.warning("TODO implement After 4 seconds, New Fire Alarm reported in panel")
    
@When("Fire alarm reported in panel. User selected the SILENCE SOUNDER button")
def step27(context):
    test.warning("TODO implement Fire alarm reported in panel. User selected the SILENCE SOUNDER button")

@When("After 8 seconds, User selected ALARM RESET button")
def step28(context):
    test.warning("TODO implement After 8 seconds, User selected ALARM RESET button")

@Then("Wait for a moment let SILENCE complete or There should be no actions till 20 seconds over")
def step29(context):
    test.warning("TODO implement Wait for a moment let SILENCE complete or There should be no actions till 20 seconds over")

@When("After 8 seconds, User selected RESOUND SOUNDER button")
def step30(context):
    test.warning("TODO implement After 8 seconds, User selected RESOUND SOUNDER button")
    
@When("After 20 seconds, User selected ALARM RESET button")
def step32(context):
    test.warning("TODO implement After 20 seconds, User selected ALARM RESET button")

@Then("FIRE ALARM RESET Has been performed from SYS no - warning message should appear and stay for 20 seconds.")
def step33(context):
    test.warning("TODO implement ")

@Given("select the operator and provide password")
def select_the_operator_and_provide_password(context):
    test.warning("TODO implement select the operator and provide password")

@Then("alarm details in fire event screen")
def alarm_details_in_fire_event_screen(context):
    waitFor("object.exists(':01_TextShadow')", 20000)
    test.compare(findObject(":01_TextShadow").childrenRect.width, 0)
    test.compare(findObject(":01_TextShadow").lineCount, 1)
    test.compare(findObject(":01_TextShadow").childrenRect.height, 0)
    test.compare(findObject(":01_TextShadow").childrenRect.x, 0)
    test.compare(findObject(":01_TextShadow").childrenRect.y, 0)
    test.compare(str(findObject(":01_TextShadow").id), "textEventCounter")
