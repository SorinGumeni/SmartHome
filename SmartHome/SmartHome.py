from threading import Thread
from SerialCom import SerialSub
from MqttCom   import MqttSub
from AppMngr.AppManager import AppManager
from Common import SerialSettings

def main():
    appManager = AppManager()
    clientSerial = SerialSub.SerialSub(SerialSettings.MC1_SERIAL_PORT_ADDRESS, appManager)
    clientMQTT   = MqttSub.MqttSub(appManager)

    try:
        serialRcvThread = Thread(target = clientSerial.listen)
        serialRcvThread.start()

        mqttRcvThread = Thread (target = clientMQTT.listen)
        mqttRcvThread.start()

    except KeyboardInterrupt:
        print ('Keyboard break!')

if __name__ == '__main__':
    main()
