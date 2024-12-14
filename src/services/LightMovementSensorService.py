from asyncio import run, sleep

from .protocols.SensorService import SensorService
from sensors.protocols.Sensor import Sensor
from events.protocols.EventEmmitter import EventEmmitter

class LightMovimentSensorService(SensorService):
    def __init__(self, sensor: Sensor, event_emmiter: EventEmmitter):
        self.sensor: Sensor = sensor
        self.event_emmiter: EventEmmitter = event_emmiter

    async def fetchAndEmmit(self, topic:str) -> None:
        print("\nLight sensor started")

        # Start Sensor collect
        await self.sensor.start()

        while self.sensor.alive:
            data = self.sensor.get_data()
            self.event_emmiter.emmit(message=data, topic=topic)
            await sleep(1)