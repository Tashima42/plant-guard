#from urequest_lib import request
def request(method, url, headers={}, json={}):
    return { "status": 200}

class HttpProvider:
    def __init__(self, base_url, headers):
        self._base_url = base_url
        self._headers = headers
    def get(self, url):
        request_url = "{}/{}".format(self._base_url, url)
        response = request("GET", request_url, headers=self._headers)
        if url == "/Time/current/zone?timeZone=America/Sao_Paulo":
            return """{
                        "year": 2022,
                        "month": 11,
                        "day": 19,
                        "hour": 7,
                        "minute": 32,
                        "seconds": 19,
                        "milliSeconds": 934,
                        "dateTime": "2022-11-19T07:32:19.9348593",
                        "time": "07:32",
                        "timeZone": "America/Sao_Paulo",
                        "dayOfWeek": "Saturday",
                        "dstActive": false
                       }"""
        else:
            return """{
                        "page": 1,
                        "perPage": 30,
                        "totalItems": 4,
                        "totalPages": 1,
                        "items": [
                            {
                                "collectionId": "627dpiklwib651v",
                                "collectionName": "commands",
                                "created": "2022-11-19 13:04:47.330Z",
                                "executed": false,
                                "id": "9atpu3gxz9v8ip1",
                                "plant_id": "93oz1d5rigkd1aq",
                                "registered": false,
                                "scheduled_date": "2022-11-19 12:00:00.000Z",
                                "type": "WATER",
                                "updated": "2022-11-19 13:04:54.984Z"
                            }
                        ]
                    }"""
    def post(self, url, body):
        request_url = "{}/{}".format(self._base_url, url)
        response = request("POST", request_url, json=body, headers=self._headers)
        return response
    def patch(self, url, body):
        request_url = "{}/{}".format(self._base_url, url)
        response = request("PATCH", request_url, json=body, headers=self._headers)
        return response

    

