from infra.mqtt.MqttManager import MqttManager

class LightMovimentSensorEventEmmitter(EventEmmitter):
    def emmit(self) -> None:
        mqtt_manager = MqttManager()
        mqtt_manager.connect()
        print("event emmited")