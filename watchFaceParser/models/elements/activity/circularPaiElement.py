import logging

from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement


class CircularPaiElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = None):
        super(CircularPaiElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(CircularPaiElement, self).draw4(drawer, resources, state.getPai(), 100)
