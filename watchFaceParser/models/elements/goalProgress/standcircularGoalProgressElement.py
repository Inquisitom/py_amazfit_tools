import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class StandCircularGoalProgressElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(StandCircularGoalProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        super(StandCircularGoalProgressElement, self).draw4(drawer, resources, state.getStand(), 12)
