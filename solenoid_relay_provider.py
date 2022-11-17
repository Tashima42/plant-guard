class SolenoidRelay:
    _state = False
    
    def __init__(self, pin):
        self._pin = pin

    def on(self):
        if self._state != True:
            self._pin.value(1)
            self._state = True
            
    def off(self):
        if self._state != False:
            self._pin.value(0)
            self._state = False
            
    def toggle(self):
        if self._state == False:
            self.on()
        elif self._state == True:
            self.off()


