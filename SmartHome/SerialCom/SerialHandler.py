import sys
sys.path.insert(0, '/home/pi/Desktop/SmartHome/AppMngr')
sys.path.insert(0, '/home/pi/Desktop/SmartHome/Common')
import AppManager
import SerialSettings

class SerialHandler:

    def __init__(self, a_oAppMngr):
        self.m_oAppMngr = a_oAppMngr #Init class member

    def removeDigits(self, a_sString):
        stringWODigits = ''.join(i for i in a_sString if not i.isdigit())
        return stringWODigits

    def keepOnlyDigits(self, a_sString):
        onlyDigitString = ''.join(i for i in a_sString if i.isdigit())
        return onlyDigitString    

    def handleEvent(self, a_sEvent):
        print('Handle serial event: ' + a_sEvent)
        
        a_sEvent = a_sEvent.strip()
        temp = a_sEvent
        a_sEvent = self.removeDigits(a_sEvent)
        print('Handle serial event: ' + a_sEvent)
        if a_sEvent == SerialSettings.SSE_RX_OUTSIDE_SENSOR_ON:
            print('SSE_RX_OUTSIDE_SENSOR_ON event received')
            self.m_oAppMngr.alarmSystemActivated()

        elif a_sEvent == SerialSettings.SSE_RX_OUTSIDE_SENSOR_OFF:
            print('SSE_RX_OUTSIDE_SENSOR_OFF event received')
            self.m_oAppMngr.alarmSystemDeactivated()

        elif a_sEvent == SerialSettings.SSE_RX_OUTSIDE_LIGHT_SENSOR_ON:
            print('SSE_RX_OUTSIDE_LIGHT_SENSOR_ON event received')
            self.m_oAppMngr.handleOutsideLightSensor('HIGH')

        elif a_sEvent == SerialSettings.SSE_RX_OUTSIDE_LIGHT_SENSOR_OFF:
            print('SSE_RX_OUTSIDE_LIGHT_SENSOR_OFF event received')
            self.m_oAppMngr.handleOutsideLightSensor('LOW')

        elif a_sEvent == SerialSettings.SSE_RX_INSIDE_TEMP_VAL:
            #print('SSE_RX_INSIDE_TEMP_VAL event received')
            temp = self.keepOnlyDigits(temp)
            value = int(temp)            
            self.m_oAppMngr.handleInsideTempSensor(value)
        
        elif a_sEvent == SerialSettings.SSE_RX_INSIDE_LIGHT_SENSOR_ON:
            print('SSE_RX_INSIDE_LIGHT_SENSOR_ON event received')
            self.m_oAppMngr.handleInsideLightSensor('HIGH')
        
        elif a_sEvent == SerialSettings.SSE_RX_INSIDE_LIGHT_SENSOR_OFF:
            print('SSE_RX_INSIDE_LIGHT_SENSOR_OFF event received')
            self.m_oAppMngr.handleInsideLightSensor('LOW')

        elif a_sEvent == SerialSettings.SSE_RX_INSIDE_FLAME_SENSOR_ON:
            print('SSE_RX_INSIDE_FLAME_SENSOR_ON event received')
            self.m_oAppMngr.handleInsideFlameSensor('HIGH')   
            
        elif a_sEvent == SerialSettings.SSE_RX_INSIDE_FLAME_SENSOR_OFF:
            print('SSE_RX_INSIDE_FLAME_SENSOR_OFF event received')
            self.m_oAppMngr.handleInsideFlameSensor('LOW')

        elif a_sEvent  == SerialSettings.SSE_RX_OUTSIDE_HALL_SENSOR_ON: 
            print('SSE_RX_OUTSIDE_HALL_SENSOR_ON event received')
            self.m_oAppMngr.handleOutsideHallSensor('HIGH')             

        elif a_sEvent  == SerialSettings.SSE_RX_OUTSIDE_HALL_SENSOR_OFF: 
            print('SSE_RX_OUTSIDE_HALL_SENSOR_OFF event received')
            self.m_oAppMngr.handleOutsideHallSensor('LOW')  

        elif a_sEvent  == SerialSettings.SSE_RX_INSIDE_MOTION_SENSOR_ON: 
            print('SSE_RX_INSIDE_MOTION_SENSOR_ON event received')
            self.m_oAppMngr.handleOutsideHallSensor('LOW')  

        elif a_sEvent  == SerialSettings.SSE_RX_INSIDE_MOTION_SENSOR_OFF: 
            print('SSE_RX_INSIDE_MOTION_SENSOR_OFF event received')
            self.m_oAppMngr.handleOutsideHallSensor('LOW')  

        else:
            print('Unknown serial event received' + a_sEvent)
