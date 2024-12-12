from protocols.Sensor import Sensor

class LightMovimentSensor(Sensor):
    def __init__(self):
        self.alive: bool = True

    def start(self) -> None:
        self.alive = True
    
    def stop(self) -> None:
        self.alive = False

    def get_data(self) -> String:
        return "data"