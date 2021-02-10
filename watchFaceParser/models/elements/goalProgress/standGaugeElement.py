import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class StandGaugeElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(StandGaugeElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        print ("StandGaugeElement-self.getImagesCount()",self.getImagesCount())
        #super(StandGaugeElement, self).draw3(drawer, resources, int(state.getStand() / state.getGoal() * self.getImagesCount()))

