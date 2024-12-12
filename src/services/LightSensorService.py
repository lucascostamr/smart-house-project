from protocols.SensorService import SensorService
from sensors.protocols import Sensor

class LightMovimentSensorService(SensorService):
    def __init__(self, sensor: Sensor, event_emmiter: EventEmmiter):
        self.sensor:Sensor = sensor
        self.event_emmiter:EventEmmiter = event_emmiter

    def start() -> None:
        print("Light sensor started")
        while sensor.alive:
            data = self.sensor.get_data()
            self.event_emmiter.emmit(channel="/sensors", data=data)
        print("Light sensor stop")
    
    def stop() -> None:
        print("Light sensor stoped")
        return