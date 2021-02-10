import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class PaiCircularGoalProgressElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(PaiCircularGoalProgressElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        super(PaiCircularGoalProgressElement, self).draw4(drawer, resources, state.getPai(), 100)
