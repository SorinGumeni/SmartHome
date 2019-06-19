import SerialSettings
import serial

class SerialPub:

    def __init__(self, a_sSerialPortAdress):
        self.m_oTransmitter = serial.Serial(a_sSerialPortAdress, baudrate=9600, timeout=2.0) #Create the Serial Sender

    def send(self, a_sMessage):
        print('Serial sending data: ' + a_sMessage)
        self.m_oTransmitter.write(a_sMessage) #Send serial data
