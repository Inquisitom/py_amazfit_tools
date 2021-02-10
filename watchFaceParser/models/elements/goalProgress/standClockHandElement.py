from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class StandClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(StandClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(StandClockHandElement, self).draw4(drawer, resources,  state.getStand(), 12)
