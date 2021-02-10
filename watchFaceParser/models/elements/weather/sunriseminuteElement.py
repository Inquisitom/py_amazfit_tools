from watchFaceParser.models.elements.common.numberElement import NumberElement

class SunriseMinuteElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(SunriseMinuteElement, self).__init__(parameter, parent, name)

    def getSunriseMinute(self):
        return self._sunriseminute
        
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getSunriseMinute():
            self.draw4(drawer, resources, state.getSunriseMinute())