from asyncio import sleep, create_task
from fastapi import FastAPI
from contextlib import asynccontextmanager

from infra.mqtt.MqttManager import MqttManager
from factories.LightMovementSensorServiceFactory import makeLightMovementSensorServiceFactory

light_movement_sensor_service = makeLightMovementSensorServiceFactory()

sensor_message = {}
actuator_message_log = []

def on_message(client, userdata, msg):
    global sensor_message
    message = msg.payload.decode()
    print(f"Received from sensors: {message}")
    sensor_message["last_message"] = message
    print(message)

    processed_message = f"Processed: {message}"
    print(f"Forwarding to actuators: {processed_message}")
    client.publish("actuator", processed_message)
    actuator_message_log.append(processed_message)

mqtt_manager = MqttManager()
mqtt_manager.subscribe("/sensors")

mqtt_manager.setOnMessageHandler(on_message)

async def mqtt_loop():
    mqtt_manager.loop_start()
    while True:
        await sleep(1)

async def lifespan(app: FastAPI):
    create_task(light_movement_sensor_service.fetchAndEmmit(topic="/sensors"))
    create_task(mqtt_loop())
    yield

app = FastAPI(lifespan=lifespan)


# --- REST API Endpoints ---
@app.get("/sensor")
def get_last_sensor_message():
    """Retrieve the last sensor message."""
    return {"last_sensor_message": sensor_message.get("last_message", "No message yet.")}

@app.get("/actuator/logs")
def get_actuator_logs():
    """Retrieve the actuator message logs."""
    return {"actuator_logs": actuator_message_log}

@app.post("/actuator/publish")
def manual_actuator_message(message: str):
    """Manually send a message to the actuator."""
    mqtt_manager.publish("actuators", message)
    actuator_message_log.append(message)
    return {"status": "Message sent to actuator", "message": message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
