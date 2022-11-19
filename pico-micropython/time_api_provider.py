import json
from http_provider import HttpProvider

class TimeApiProvider:
    def __init__(self, http, rtc):
        self._http = HttpProvider("https://www.timeapi.io/api", {})
        self._rtc = rtc 
    def update_rtc_remote(self):
        time_data = json.loads(self._http.get("/Time/current/zone?timeZone=America/Sao_Paulo"))
        self._rtc.datetime((int(time_data["year"]), int(time_data["month"]), int(time_data["day"]), self.parse_day_of_week(time_data["dayOfWeek"]), int(time_data["hour"]), int(time_data["minute"]), int(time_data["seconds"]), 0))
    def parse_day_of_week(self, day):
        if day == "Monday":
            return 1
        elif day == "Tuesday":
            return 2
        elif day == "Wednesday":
            return 3
        elif day == "Thursday":
            return 4
        elif day == "Friday":
            return 5
        elif day == "Saturday":
            return 6
        elif day == "Sunday":
            return 7


