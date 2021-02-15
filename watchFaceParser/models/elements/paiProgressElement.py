import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class PaiProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._images1 = None
        self._images2 = None
        self._images4 = None
        self._paiLinear = None
        super(PaiProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


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
            from watchFaceParser.models.elements.goalProgress.paicircularGoalProgressElement import PaiCircularGoalProgressElement
            self._circular = PaiCircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular')
            return self._circular
        elif parameterId == 1:
            from watchFaceParser.models.elements.goalProgress.paiGaugeElement import PaiGaugeElement # temp.
            self._images1 = PaiGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images1
        elif parameterId == 2:
            from watchFaceParser.models.elements.goalProgress.paiLinearElement import PaiLinearElement
            self._paiLinear = PaiLinearElement(parameter = parameter, parent = self, name = '?paiLinear?')
            return self._paiLinear
        elif parameterId == 4:
            #TODO: change here
            from watchFaceParser.models.elements.goalProgress.paiGaugeElement import PaiGaugeElement # TO CHANGE !!
            self._images4 = PaiGaugeElement(parameter = parameter, parent = self, name = '?_advancebar?')
            return self._images4
        elif parameterId == 6:
            from watchFaceParser.models.elements.goalProgress.paiClockHandElement import PaiClockHandElement 
            self._clockHand = PaiClockHandElement(parameter = parameter, parent = self, name = 'ClockHand')
            return self._clockHand
        elif parameterId == 5:
            from watchFaceParser.models.elements.goalProgress.circularGoalProgressElement import CircularGoalProgressElement
            self._circular2 = CircularGoalProgressElement(parameter = parameter, parent = self, name = 'Circular2')
            return self._circular2
        else:
            print ("Unknown PaiProgressElement",parameterId)
            return super(PaiProgressElement, self).createChildForParameter(parameter)
