from services.LightMovementSensorService import LightMovimentSensorService
from sensors.LightMovimentSensor import LightMovimentSensor
from events.LightMovimentSensorEventEmmiter import LightMovimentSensorEventEmmitter

def makeLightMovementSensorServiceFactory():
    light_moviment_sensor = LightMovimentSensor()
    light_moviment_sensor_event_emmiter = LightMovimentSensorEventEmmitter()
    return LightMovimentSensorService(
        sensor=light_moviment_sensor,
        event_emmiter=light_moviment_sensor_event_emmiter
    )