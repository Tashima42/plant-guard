import json
import utime as time

class CommandControlService:
    def __init__(self, plant_id, http, scheduler, solenoid_relay):
        self._plant_id = plant_id
        self._http = http
        self._scheduler = scheduler
        self._solenoid_relay = solenoid_relay
    def check_commands(self):
        now = time.time() # TODO: format time
        print(now)
        filters = "executed=false %26%26 plant_id = '{}' %26%26 scheduled_date >= '{}'".format(self._plant_id, now)
        response = self._http.get("collections/commands/records?filter=({})&sort=scheduled_date".format(filters))
        commands = json.loads(response)
        for command in commands["items"]:
            # TODO: parse time to millis
            # TODO: find the real time in seconds to sleep
            if command["type"] == "WATER":
                print(command)
                #self._scheduler.register_task(1668843159, self._solenoid_relay.on_seconds, 5)
                self.mark_command_registered(command["id"])
    def mark_command_registered(self, command_id):
        self._http.patch("/api/collections/commands/records/{}".format(command_id), "{\"registered\": true}")
    def mark_command_executed(self, command_id):
        self._http.patch("/api/collections/commands/records/{}".format(command_id), "{\"executed\": true}")
        

