class SoilMoistureSensor:
    _moisture: int
    
    def __init__(self, pin):
        self._pin = pin
        self._moisture = -1

    @property
    def moisture(self):
        self._moisture = self._pin.read_u16()
        return self._moisture


