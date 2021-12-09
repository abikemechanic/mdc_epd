import paho.mqtt.client as mqtt
import paho.mqtt
import time


class MQTTClient:
    subscriptions = ['MDC/Ovens/+/temp']

    def __init__(self, host, port):
        self.client = mqtt.Client()
        self.message_dict = {}
        self.connected = False

        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        self.create_subscriptions()

        self.client.connect(host=host, port=port)

        if self.connected:
            self.client.loop_start()

    def on_message(self, client, userdata, msg: mqtt.MQTTMessage):
        message = msg.payload
        topic = msg.topic

        self.message_dict[topic] = message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected = True
        else:
            self.connected = False

    def create_subscriptions(self):
        self.client.subscribe(self.subscriptions)

    def end_connection(self):
        self.client.loop_stop()
        self.client.disconnect()
