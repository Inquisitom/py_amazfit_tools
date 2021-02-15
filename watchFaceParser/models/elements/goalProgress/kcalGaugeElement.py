import logging

from watchFaceParser.models.elements.common.imageSetElement import ImageSetElement

class KCalGaugeElement(ImageSetElement):
    def __init__(self, parameter, parent, name = None):
        super(KCalGaugeElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        print ("KCalGaugeElement-self.getImagesCount()",self.getImagesCount())
