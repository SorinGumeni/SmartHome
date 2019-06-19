import sys
sys.path.insert(0, '/home/pi/Desktop/SmartHome/AppMngr')
sys.path.insert(0, '/home/pi/Desktop/SmartHome/Common')
import AppManager
import SerialSettings

class SerialHandler:

    def __init__(self, a_oAppMngr):
        self.m_oAppMngr = a_oAppMngr #Init class member

    def handleEvent(self, a_sEvent):
        print('Handle serial event: ' + a_sEvent)
        a_sEvent = a_sEvent.strip()

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

        else:
            print('Unknown serial event received' + a_sEvent)
