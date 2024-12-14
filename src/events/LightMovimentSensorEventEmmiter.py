from infra.mqtt.MqttManager import MqttManager
from .protocols.EventEmmitter import EventEmmitter

class LightMovimentSensorEventEmmitter(EventEmmitter):
    def __init__(self):
        self.mqtt_manager = MqttManager()

    def emmit(self, topic:str, message: str) -> None:
        self.mqtt_manager.publish(topic=topic, message=message)
        print("Event emmited")