import paho.mqtt.client as mqtt
import MqttSettings
import MqttHandler
class MqttSub:

    def __init__(self, a_oAppMngr):

        self.m_client            = mqtt.Client()      #Create new mqtt client
        self.m_client.on_message = self.on_message    # Assign the on_message local define function

        self.m_client.connect(MqttSettings.MQTT_BROKER_ADDRESS, port = 1883)    #Connect to the broker
        self.m_client.subscribe(MqttSettings.TOPIC)   #Subscribe to the topic

        self.m_oMqttHandler = MqttHandler.MqttHandler(a_oAppMngr) #Create a handler for Mqtt events

        print('MqttSub init finished')

    def listen(self):
        self.m_client.loop_forever()

    def on_message(self, client, userdata, a_message):
        print('New mqtt message received')
        self.m_oMqttHandler.handleEvent(a_message)
