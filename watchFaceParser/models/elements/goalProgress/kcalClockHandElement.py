from watchFaceParser.models.elements.common.clockHandElement import ClockHandElement

class KCalClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(KCalClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(KCalClockHandElement, self).draw4(drawer, resources,  state.getKCal(), 800)
