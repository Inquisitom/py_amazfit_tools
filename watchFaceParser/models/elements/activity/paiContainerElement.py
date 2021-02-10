import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement


#ALL STUFF TO BE DONE HERE !
class PaiContainerElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._pai = None
        self._circularPai = None
        self._clockHandPai = None
        super(PaiContainerElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getPai(self):
        return self._pai

    def getCircularPai(self):
        return self._circularPai

    def getClockHandPai(self):
        return self._clockHandPai

    def draw3(self, drawer, resources, state):

        if self.getCircularPai():
            self.getCircularPai().draw3(drawer, resources, state)

        if self.getClockHandPai():
            self.getClockHandPai().draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.elements.activity.circularPaiElement import CircularPaiElement
            self._circularPai = CircularPaiElement(parameter = parameter, parent = self, name = '_circularPai')
        elif parameterId == 3:
            from watchFaceParser.models.elements.activity.paiClockHandElement import PaiClockHandElement
            self._clockHandPai = PaiClockHandElement(parameter = parameter, parent = self, name = '_clockHandPai')
        else:
            super(PaiContainerElement, self).createChildForParameter(parameter)
