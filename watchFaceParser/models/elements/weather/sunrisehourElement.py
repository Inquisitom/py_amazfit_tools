from watchFaceParser.models.elements.common.numberElement import NumberElement

class SunriseHourElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(SunriseHourElement, self).__init__(parameter, parent, name)

    def getSunriseHour(self):
        return self._sunrisehour

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getSunriseHour():
            self.draw4(drawer, resources, state.getSunriseHour())
