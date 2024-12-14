from typing import Callable

import paho.mqtt.client as mqtt

class  MqttManager:
    def __init__(self):
        self.broker = "mqtt"
        self.port = 1883
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(self.broker, self.port)

    def setPublishHandler(self, publishHandler: Callable):
        self.client.on_publish = publishHandler

    def setOnConnectHandler(self, onConnectHandler: Callable):
        self.client.on_connect = onConnectHandler

    def setOnMessageHandler(self, onMessageHandler: Callable):
        self.client.on_message = onMessageHandler

    def publish(self, message: str, topic: str):
        self.client.publish(topic, message)

    def subscribe(self, topic: str):
        self.client.subscribe(topic)

    def loop_start(self):
        self.client.loop_start()