from watchFaceParser.models.elements.common.numberElement import NumberElement

class SunsetMinuteElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(SunsetMinuteElement, self).__init__(parameter, parent, name)

    def getSunsetMinute(self):
        return self._sunsetminute
        
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getSunsetMinute():
            self.draw4(drawer, resources, state.getSunsetMinute())