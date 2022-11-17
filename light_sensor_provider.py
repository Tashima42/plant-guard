class LightSensor:
    _light: int
    
    def __init__(self, pin):
        self._pin = pin
        self._light = -1

    @property
    def light(self):
        self._light = self._pin.read_u16()
        return self._light


