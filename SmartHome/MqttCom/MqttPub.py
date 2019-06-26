import paho.mqtt.client as mqtt
import MqttSettings
import MqttHandler
class MqttPub:

    def __init__(self):

        self.m_client            = mqtt.Client()      #Create new mqtt client
        self.m_client.connect(MqttSettings.MQTT_BROKER_ADDRESS, port = 1883)    #Connect to the broker
        self.m_client.on_disconnect = self.on_disconnect
        print('MqttPub init finished')

    def publish(self, topic, a_message):
        print('mqttPublish topic: '+topic+' message: '+ str(a_message))
        self.m_client.publish(topic,a_message)

    def on_disconnect(self):
            print('Mqtt Pub disconnected')
            self.m_client.connect(MqttSettings.MQTT_BROKER_ADDRESS, port = 1883)
