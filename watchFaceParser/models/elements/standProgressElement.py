import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class StandProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._images1 = None
        self._images2 = None
        self._images4 = None
        self._standLinear = None
        super(StandProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getCircular(self):
        return self._circular


    def getImages1(self):
        return self._images1

    def getImages2(self):
        return self._images2

    def getImages4(self):
        return self._images4


    # def getCircular2(self):
    #     return self._circular2


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 3:
            from watchFaceParser.models.elements.goalProgress.standcircularGoalProgressElement import StandCircularGoalProgressElement
            self._circular = StandCircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular')
            return self._circular
        elif parameterId == 1:
            from watchFaceParser.models.elements.goalProgress.standGaugeElement import StandGaugeElement # temp.
            self._images1 = StandGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images1
        elif parameterId == 2:
            from watchFaceParser.models.elements.goalProgress.standLinearElement import StandLinearElement
            self._standLinear = StandLinearElement(parameter = parameter, parent = self, name = '?standLinear?')
            return self._standLinear
        elif parameterId == 4:
            from watchFaceParser.models.elements.goalProgress.standGaugeElement import StandGaugeElement # temp.
            self._images4 = StandGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images4
        elif parameterId == 6:
            from watchFaceParser.models.elements.goalProgress.standClockHandElement import StandClockHandElement # must must be own. fix it!!
            self._clockHand = StandClockHandElement(parameter = parameter, parent = self, name = 'ClockHand')
            return self._clockHand
        elif parameterId == 5:
            from watchFaceParser.models.elements.goalProgress.standcircularGoalProgressElement import StandCircularGoalProgressElement
            self._circular2 = StandCircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular2')
            return self._circular2
        else:
            print ("Unknown StandProgressElement",parameterId)
            return super(StandProgressElement, self).createChildForParameter(parameter)
