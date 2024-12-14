from asyncio import create_task, sleep
from .protocols.Sensor import Sensor

class LightMovimentSensor(Sensor):
    def __init__(self):
        self.alive: bool = True
        self.data: str = None
        self.loop_task = None

    async def start(self) -> None:
        self.alive = True
        self.loop_task = create_task(self._collect_data())
    
    async def _collect_data(self) -> None:
        while self.alive:
            await sleep(5)
            self.data = "turn-off" if self.data == "turn-on" else "turn-on"

    def stop(self) -> None:
        self.alive = False
        self.loop_task.cancel()

    def get_data(self) -> str:
        return self.data