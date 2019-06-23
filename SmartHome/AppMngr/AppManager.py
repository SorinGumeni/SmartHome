import sys
sys.path.insert(0, '/home/pi/Desktop/SmartHome/Common')
sys.path.insert(0, '/home/pi/Desktop/SmartHome/SerialCom')
sys.path.insert(0, '/home/pi/Desktop/SmartHome/MqttCom')
from threading import Thread
import SerialSettings
import SerialSub
import SerialPub
import MqttPub
import Settings
import time
import os
import smtplib
from subprocess import call
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders

class AppManager:

    def __init__(self):
        self.m_MC1SerialTx = SerialPub.SerialPub(SerialSettings.MC1_SERIAL_PORT_ADDRESS)
        self.m_MC2SerialTx = SerialPub.SerialPub(SerialSettings.MC2_SERIAL_PORT_ADDRESS)
        self.m_MqttPub     = MqttPub.MqttPub()
        self.m_sendEmailAdress = "gumeni.sorin@yahoo.com"
        self.m_fIsSecurityEnabled = False
        self.m_fIsOutsideAutoLightEnabled = False
        self.m_fIsInsideAutoLightEnabled  = False
        self.m_fUserWarmTempMode = False
        self.m_iUserDesiredTemp = 23

    def sendEmail(self, a_sendEmailAddress, a_sMailSubject):
        print ('sendEmail function ' + a_sendEmailAddress)
        os.system("raspistill -o pic.jpg -t 10 -n -ex auto -awb auto -w 800 -h 600")
        server = smtplib.SMTP('smtp.gmail.com: 587')
        msg = MIMEMultipart()
        msg['Subject'] = a_sMailSubject
        server.ehlo
        server.starttls()
        server.ehlo
        print('sendEmail: login to server')
        server.login("homesecure112", "parola.1234")
        attachment = open("/home/pi/Desktop/SmartHome/pic.jpg", "rb").read()
        image = MIMEImage(attachment, name=os.path.basename("asd.jpg"))
        msg.attach(image)
        print('sendEmail: sending the email')
        text = msg.as_string()
        server.sendmail("homesecure112@gmail.com",a_sendEmailAddress,text)
        print ('email sent')

    def alarmSystemActivated(self):
        
        if True == self.m_fIsSecurityEnabled:
            print('alarmSystemActivated')
            self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_BUZZER_ON)
            self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_MOTION_LED_ON)
            self.m_MqttPub.publish('webOLight','ON')
            sendMailThread = Thread(target = self.sendEmail, args = (self.m_sendEmailAdress, Settings.SENSOR_EMAIL_SUBJECT,))
            sendMailThread.start()
        else:
            print('alarmSystemActivated m_fIsSecurityEnabled false')

    def alarmSystemDeactivated(self):
        
        if True == self.m_fIsSecurityEnabled:
            print('alarmSystemDeactivated')
            self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_BUZZER_OFF)
            self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_MOTION_LED_OFF)
            self.m_MqttPub.publish('webOLight','OFF')
        else:
            print('alarmSystemDeactivated m_fIsSecurityEnabled false')

    def setOutsideLedState(self, a_fLedState):
        print('setOutsideLedState a_fLedState ' + a_fLedState)
        
        if ('ON' == a_fLedState):
            self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_MOTION_LED_ON)
            self.m_MqttPub.publish('webOLight','ON')
            self.m_fIsOutsideAutoLightEnabled = False
        elif ('OFF' == a_fLedState):
            self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_MOTION_LED_OFF)
            self.m_MqttPub.publish('webOLight','OFF')
            self.m_fIsOutsideAutoLightEnabled = False
        elif('AUTO' == a_fLedState):
            self.m_fIsOutsideAutoLightEnabled = True
        else :
            print('setOutsideLedState unknown state received a_fLedState' +a_fLedState)

    def setInsideLedState(self, a_fLedState):
        print('setOutsideLedState a_fLedState ' + a_fLedState)
        
        if ('ON' == a_fLedState):
            self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_LIGHT_LED_ON)
            self.m_MqttPub.publish('webILight','ON')
            self.m_fIsInsideAutoLightEnabled = False
        elif ('OFF' == a_fLedState):
            self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_LIGHT_LED_OFF)
            self.m_MqttPub.publish('webILight','OFF')
            self.m_fIsInsideAutoLightEnabled = False
        elif('AUTO' == a_fLedState):
            self.m_fIsInsideAutoLightEnabled = True
        else :
            print('setOutsideLedState unknown state received a_fLedState' +a_fLedState)            

    def setSecurityState(self, a_fSecurityState):
        if ('ON' == a_fSecurityState):
            self.m_fIsSecurityEnabled = True
        elif ('OFF' == a_fSecurityState):
            self.m_fIsSecurityEnabled = False

    def takeFrontDoorSnap(self):
        sendMailThread = Thread(target = self.sendEmail, args = (self.m_sendEmailAdress,Settings.SNAP_EMAIL_SUBJECT,))
        sendMailThread.start()

    def handleOutsideLightSensor(self, a_fSensorState):

        if( True == self.m_fIsOutsideAutoLightEnabled ):
            print('handleOutsideLightSensor a_fSensorState ' + a_fSensorState)
            if ('HIGH' == a_fSensorState):
                self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_MOTION_LED_ON)
                self.m_MqttPub.publish('webOLight','ON')
            elif ('LOW' == a_fSensorState):
                self.m_MC1SerialTx.send(SerialSettings.O_SSE_TX_MOTION_LED_OFF)
                self.m_MqttPub.publish('webOLight','OFF')
            else:
                print('handleOutsideLightSensor unknown state received a_fSensorState' + a_fSensorState)
        else:
             print('handleOutsideLightSensor m_fIsOutsideAutoLightEnabled false')

    def handleInsideLightSensor(self, a_fSensorState):

        if( True == self.m_fIsInsideAutoLightEnabled ):
            print('handleInsideLightSensor a_fSensorState ' + a_fSensorState)
            if ('HIGH' == a_fSensorState):
                self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_MOTION_LED_ON)
                self.m_MqttPub.publish('webILight','ON')
            elif ('LOW' == a_fSensorState):
                self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_MOTION_LED_OFF)
                self.m_MqttPub.publish('webILight','OFF')
            else:
                print('handleInsideLightSensor unknown state received a_fSensorState' + a_fSensorState)
        else:
             print('handleInsideLightSensor m_fIsInsideAutoLightEnabled false')             

    def handleInsideTempSensor(self, a_iTempValue):
        print('handleInsideTempSensor a_iTempValue = '+ chr(a_iTempValue) )
        print('m_fUserWarmTempMode = ' + chr(self.m_fUserWarmTempMode) )
        
        self.m_MqttPub.publish('iTemperature',a_iTempValue)
        
        if ( False == self.m_fUserWarmTempMode):
            if( self.m_iUserDesiredTemp < a_iTempValue ):
                self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_VENT_ON)
            else:
                self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_VENT_OFF)
        else:
            if( self.m_iUserDesiredTemp > a_iTempValue ):
                self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_HEAT_ON)
            else:
                self.m_MC2SerialTx.send(SerialSettings.I_SSE_TX_HEAT_OFF)

    def setThermostatState(self, a_sThermoState):
        print('setThermostatState a_sThermoState = ' + a_sThermoState)

        if('COOL' == a_sThermoState):
            self.m_fUserWarmTempMode = False
        elif('HEAT' == a_sThermoState):
            self.m_fUserWarmTempMode = True
        else:
            print('setThermostatState invalid state received a_sThermoState = ' + a_sThermoState)
    
    def setUserDesiredTemp(self, tempValue):
        print('setUserDesiredTemp ' + str(tempValue))
        self.m_iUserDesiredTemp = tempValue
