﻿import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class StepsProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._images1 = None
        self._images2 = None
        self._images4 = None
        self._stepsLinear = None
        super(StepsProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


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
        if parameterId == 1:
            from watchFaceParser.models.elements.goalProgress.stepGaugeElement import StepGaugeElement # temp.
            self._images1 = StepGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images1
        elif parameterId == 2:
            from watchFaceParser.models.elements.goalProgress.stepsLinearElement import StepsLinearElement
            self._stepsLinear = StepsLinearElement(parameter = parameter, parent = self, name = '?stepsLinear?')
            return self._stepsLinear
        elif parameterId == 3:
            from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement
            self._circular = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular')
            return self._circular
        elif parameterId == 4:
            from watchFaceParser.models.elements.goalProgress.stepGaugeElement import StepGaugeElement # temp.
            self._images4 = StepGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images4
        elif parameterId == 5:
            from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement
            self._circular2 = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular2')
            return self._circular2
        elif parameterId == 6:
            from watchFaceParser.models.elements.goalProgress.stepsClockHandElement import StepsClockHandElement # must must be own. fix it!!
            self._clockHand = StepsClockHandElement(parameter = parameter, parent = self, name = 'ClockHand')
            return self._clockHand
        else:
            print ("Unknown StepsProgressElement",parameterId)
            return super(StepsProgressElement, self).createChildForParameter(parameter)
