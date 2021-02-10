from watchFaceParser.models.elements.common.numberElement import NumberElement

class PaiElement(NumberElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(PaiElement, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getPai():
            self.draw4(drawer, resources, state.getPai())
