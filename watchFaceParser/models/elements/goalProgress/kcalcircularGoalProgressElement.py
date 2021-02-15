import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class KCalCircularGoalProgressElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(KCalCircularGoalProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        super(KCalCircularGoalProgressElement, self).draw4(drawer, resources, state.getKCal(), 800)
