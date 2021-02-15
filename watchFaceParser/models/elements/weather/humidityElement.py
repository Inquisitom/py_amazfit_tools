from watchFaceParser.models.elements.common.numberElement import NumberElement

class HumidityElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(HumidityElement, self).__init__(parameter, parent, name)

    def getHumidity(self):
        return self._humidity
        
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getHumidity():
            self.draw4(drawer, resources, state.getHumidity())