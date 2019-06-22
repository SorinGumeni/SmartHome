from threading import Thread
from SerialCom import SerialSub
from MqttCom   import MqttSub
from AppMngr.AppManager import AppManager
from Common import SerialSettings

def main():
    appManager = AppManager()
    clientSerialMC1 = SerialSub.SerialSub(SerialSettings.MC1_SERIAL_PORT_ADDRESS, appManager)
    clientSerialMC2 = SerialSu.SerialSub(SerialSettings.MC2_SERIAL_PORT_ADDRESS, appManager)
    clientMQTT      = MqttSub.MqttSub(appManager)

    try:
        serialRcvThreadMC1 = Thread(target = clientSerialMC1.listen)
        serialRcvThreadMC1.start()

        serialRcvThreadMC2 = Thread(target = clientSerialMC2.listen)
        serialRcvThreadMC2.start()

        mqttRcvThread = Thread (target = clientMQTT.listen)
        mqttRcvThread.start()

    except KeyboardInterrupt:
        print ('Keyboard break!')

if __name__ == '__main__':
    main()
