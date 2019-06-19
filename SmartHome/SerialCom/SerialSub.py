import sys
sys.path.insert(0, '/home/pi/Desktop/SmartHome/AppMngr')
sys.path.insert(0, '/home/pi/Desktop/SmartHome/Common')
import serial
import SerialSettings
import SerialHandler

class SerialSub:

    def __init__(self, a_sSerialPortAdress, a_oAppMngr):
            self.m_oReceiver = serial.Serial(a_sSerialPortAdress ,baudrate=9600, timeout=2.0) #Create the Serial Receiver
            self.m_oSerialHandler = SerialHandler.SerialHandler(a_oAppMngr) #Create the Serial Event Handler
            print('Serial Sub init finished')

    def listen(self):
        print('Serial listener started on port ')
        while True:
            while self.m_oReceiver.inWaiting():
                data = self.m_oReceiver.readline()      #Receive serial data
                self.m_oSerialHandler.handleEvent(data) #Handle the received data
