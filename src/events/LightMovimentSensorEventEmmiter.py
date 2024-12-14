from infra.mqtt.MqttManager import MqttManager
from .protocols.EventEmmitter import EventEmmitter

class LightMovimentSensorEventEmmitter(EventEmmitter):
    def __init__(self, topic:str):
        self.mqtt_manager = MqttManager(topic)

    def emmit(self, message: str) -> None:
        self.mqtt_manager.publish(message)
        print("Event emmited")