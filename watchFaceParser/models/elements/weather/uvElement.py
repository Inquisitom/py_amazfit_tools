from watchFaceParser.models.elements.common.numberElement import NumberElement

class UVElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(UVElement, self).__init__(parameter, parent, name)

    def getUV(self):
        return self._uv
        
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getUV():
            self.draw4(drawer, resources, state.getUV())