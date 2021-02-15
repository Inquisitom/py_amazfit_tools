import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class KCalProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._images1 = None
        self._images2 = None
        self._images4 = None
        self._kcalLinear = None
        super(KCalProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


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
            from watchFaceParser.models.elements.goalProgress.kcalcircularGoalProgressElement import KCalCircularGoalProgressElement
            self._circular = KCalCircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular')
            return self._circular
        elif parameterId == 1:
            from watchFaceParser.models.elements.goalProgress.kcalGaugeElement import KCalGaugeElement # temp.
            self._images1 = KCalGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images1
        elif parameterId == 2:
            from watchFaceParser.models.elements.goalProgress.kcalLinearElement import KCalLinearElement
            self._kcalLinear = KCalLinearElement(parameter = parameter, parent = self, name = '?kcalLinear?')
            return self._kcalLinear
        elif parameterId == 4:
            from watchFaceParser.models.elements.goalProgress.kcalGaugeElement import KCalGaugeElement # temp.
            self._images4 = KCalGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images4
        elif parameterId == 6:
            from watchFaceParser.models.elements.goalProgress.kcalClockHandElement import KCalClockHandElement 
            self._clockHand = KCalClockHandElement(parameter = parameter, parent = self, name = 'ClockHand')
            return self._clockHand
        elif parameterId == 5:
            from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement
            self._circular2 = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular2')
            return self._circular2
        else:
            print ("Unknown KCalProgressElement",parameterId)
            return super(KCalProgressElement, self).createChildForParameter(parameter)
