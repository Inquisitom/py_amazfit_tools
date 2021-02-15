import logging

from watchFaceParser.models.elements.basic.valueElement import ValueElement

class HumiditySuffixImageIndexElement(ValueElement):
    def __init__(self, parameter, parent, name = 'None'):
        self._humiditysuffiximageindex = None
        super(HumiditySuffixImageIndexElement, self).__init__(parameter, parent, name)


    def getHumiditySuffixImageIndex(self):
        return self._humiditysuffiximageindex
