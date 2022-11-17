from machine import Pin, ADC, RTC
import utime as time
from temperature_humidity_sensor_provider import TemperatureHumiditySensor
from soil_moisture_sensor_provider import SoilMoistureSensor
from light_sensor_provider import LightSensor
from solenoid_relay_provider import SolenoidRelay

TEMPERATURE_HUMIDITY_SENSOR_PIN_NUMBER = 28
SOIL_MOISTURE_SENSOR_ANALOG_PIN_NUMBER = 26
LIGHT_SENSOR_ANALOG_PIN_NUMBER = 27
SOLENOID_RELAY_PIN_NUMBER = 22

class Main:

    def __init__(self):
        self._rtc = RTC()
        self._rtc.datetime((2022, 11, 17, 0, 0, 0, 0, 0))
        
        temperature_humidity_sensor_pin = Pin(TEMPERATURE_HUMIDITY_SENSOR_PIN_NUMBER, Pin.OUT, Pin.PULL_DOWN)
        self._temperature_humidity_sensor = TemperatureHumiditySensor(temperature_humidity_sensor_pin)

        soil_moisture_sensor_analog_pin = ADC(SOIL_MOISTURE_SENSOR_ANALOG_PIN_NUMBER)
        self._soil_moisture_sensor = SoilMoistureSensor(soil_moisture_sensor_analog_pin)
        
        light_sensor_analog_pin = ADC(LIGHT_SENSOR_ANALOG_PIN_NUMBER)
        self._light_sensor = LightSensor(light_sensor_analog_pin)
        
        solenoid_relay_pin = Pin(SOLENOID_RELAY_PIN_NUMBER, Pin.OUT, Pin.PULL_DOWN)
        self._solenoid_relay = SolenoidRelay(solenoid_relay_pin)

    def loop(self):
        while True:
            room_temperature = self._temperature_humidity_sensor.temperature
            room_humidity = self._temperature_humidity_sensor.humidity
            soil_moisture = self._soil_moisture_sensor.moisture
            room_light = self._light_sensor.light
            now = self._rtc.datetime()
            
            self._solenoid_relay.toggle()
            print("Temperature: {}".format(room_temperature))
            print("Humidity: {}".format(room_humidity))
            print("Soil Moisture: {}".format(soil_moisture))
            print("Light: {}".format(room_light))
            print("Now: {}".format(now))
            print("======================")
            time.sleep(5)
            
main = Main()
main.loop()

