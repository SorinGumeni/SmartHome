import paho.mqtt.client as mqtt
import sys
sys.path.insert(0, '/home/pi/Desktop/SmartHome/AppMngr')
sys.path.insert(0, '/home/pi/Desktop/SmartHome/Common')
import AppManager

class MqttHandler:
    def __init__(self, a_oAppMngr):
        self.m_oAppMngr = a_oAppMngr #Init class member

    def handleEvent(self, a_sEvent):
        print('Handle mqtt event on topic: '+ a_sEvent.topic + ' with message: ' + a_sEvent.payload)
        if a_sEvent.topic == 'outside/light':
            receivedLedState = a_sEvent.payload
            self.m_oAppMngr.setOutsideLedState(receivedLedState)
        elif a_sEvent.topic == 'outside/security':
            receivedSecurityState = a_sEvent.payload
            self.m_oAppMngr.setSecurityState(receivedSecurityState)
        elif a_sEvent.topic == 'outside/screenshot':
            self.m_oAppMngr.takeFrontDoorSnap()
        elif a_sEvent.topic == 'inside/light':
            receivedLedState = a_sEvent.payload
            self.m_oAppMngr.setInsideLedState(receivedLedState)
        elif a_sEvent.topic == 'inside/thermostat':
            thermostatState = a_sEvent.payload
            self.m_oAppMngr.setThermostatState(thermostatState)
        elif a_sEvent.topic == 'inside/thermostat/desiredTemp':
            tempValue = a_sEvent.payload
            self.m_oAppMngr.setUserDesiredTemp(tempValue)
        elif a_sEvent.topic == 'addEmailAddress':
            emailAddr = a_sEvent.payload
            self.m_oAppMngr.addEmailAddress(emailAddr)
        elif a_sEvent.topic == 'removeEmailAddress':
            emailAddr = a_sEvent.payload
            self.m_oAppMngr.removeEmailAddress(emailAddr)                  
                          
        else:
            print('invalid topic received')


