from machine import Pin, ADC, RTC
import utime as time
from http_provider import HttpProvider
from time_api_provider import TimeApiProvider
from temperature_humidity_sensor_provider import TemperatureHumiditySensor
from soil_moisture_sensor_provider import SoilMoistureSensor
from light_sensor_provider import LightSensor
from solenoid_relay_provider import SolenoidRelay
from scheduler_service import SchedulerService
from sensor_logger_service import SensorLoggerService
from command_control_service import CommandControlService

TEMPERATURE_HUMIDITY_SENSOR_PIN_NUMBER = 28
SOIL_MOISTURE_SENSOR_ANALOG_PIN_NUMBER = 26
LIGHT_SENSOR_ANALOG_PIN_NUMBER = 27
SOLENOID_RELAY_PIN_NUMBER = 22

COMMAND_CONTROL_SERVER_TOKEN = ""
COMMAND_CONTROL_SERVER_BASE_URL = ""
COMMAND_CONTROL_SERVER_PLANT_ID = ""
class Main:

    def __init__(self):
        self.check_sensors_interval = 3
        self.check_command_center_interval = 3
        
        temperature_humidity_sensor_pin = Pin(TEMPERATURE_HUMIDITY_SENSOR_PIN_NUMBER, Pin.OUT, Pin.PULL_DOWN)
        soil_moisture_sensor_analog_pin = ADC(SOIL_MOISTURE_SENSOR_ANALOG_PIN_NUMBER)
        light_sensor_analog_pin = ADC(LIGHT_SENSOR_ANALOG_PIN_NUMBER)
        solenoid_relay_pin = Pin(SOLENOID_RELAY_PIN_NUMBER, Pin.OUT, Pin.PULL_DOWN)
        
        self._http = HttpProvider(COMMAND_CONTROL_SERVER_BASE_URL, { "Authorization": COMMAND_CONTROL_SERVER_TOKEN})
        self._rtc = RTC()
        self._time_api_provider = TimeApiProvider(self._http, self._rtc)
        self._temperature_humidity_sensor = TemperatureHumiditySensor(temperature_humidity_sensor_pin)
        self._soil_moisture_sensor = SoilMoistureSensor(soil_moisture_sensor_analog_pin)
        self._light_sensor = LightSensor(light_sensor_analog_pin)
        self._solenoid_relay = SolenoidRelay(solenoid_relay_pin)
        self._sensor_logger_service = SensorLoggerService(self._http, self._temperature_humidity_sensor, self._soil_moisture_sensor, self._light_sensor)
        self._scheduler_service = SchedulerService()
        self._command_control_service = CommandControlService(COMMAND_CONTROL_SERVER_PLANT_ID, self._http, self._scheduler_service, self._solenoid_relay)
        
        self._time_api_provider.update_rtc_remote()
        self._solenoid_relay.on()
                
    def loop(self):
        check_sensors_looper = 0
        check_command_looper = 0
        self.check_sensors_interval = 3
        self.check_command_center_interval = 3
        while True:
            if check_sensors_looper == self.check_sensors_interval:
                check_sensors_looper = 0
                self._sensor_logger_service.register_logs()
                
            if check_command_looper == self.check_command_center_interval:
                check_command_looper = 0
                self._solenoid_relay.toggle()
                #self._command_control_service.check_commands()
            
            self._scheduler_service.check_tasks(time.time())
            
            print("======================")
            check_sensors_looper = check_sensors_looper + 1
            check_command_looper = check_command_looper + 1
            time.sleep(1)
            
main = Main()
main.loop()

