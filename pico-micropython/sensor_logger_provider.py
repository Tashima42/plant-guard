import utime as time
import json

class SensorLoggerService:
    def __init__(self, http, temperature_humidity_sensor, soil_moisture_sensor, light_sensor):
        self._http = http
        self._temperature_humidity_sensor = temperature_humidity_sensor
        self._soil_moisture_sensor = soil_moisture_sensor
        self._light_sensor = light_sensor  

    def register_logs(self):
        sensor_logs = { 
            "room_temperature": self._temperature_humidity_sensor.temperature,
            "room_humidity": self._temperature_humidity_sensor.humidity,
            "soil_moisture": self._soil_moisture_sensor.moisture,
            "room_light": self._light_sensor.light,
            "now": time.time()
        }
        
        self._http.post("etc", sensor_logs)


