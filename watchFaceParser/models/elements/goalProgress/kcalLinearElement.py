﻿import logging

from watchFaceParser.models.elements.common.iconSetElement import IconSetElement

class KCalLinearElement(IconSetElement):

    def __init__(self, parameter, parent, name = None):
        self._ar = []
        #self._slices = 0
        super(KCalLinearElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def getCoordinatesArray(self):
        return self._ar

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        val = int(len(self._ar) * state.getKCal() / 800) 
        if val >= len(self._ar):
            val = len(self._ar) -1
        super(KCalLinearElement, self).draw3(drawer, resources, val)


    def createChildForParameter(self, parameter):
        if parameter.getId() == 1:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        elif parameter.getId() == 2:
            from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter = parameter, parent = self, name = 'CenterOffset')
            self._ar.append(self._coordinates)
        else:
            super(IconSetElement, self).createChildForParameter(parameter)
