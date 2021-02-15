import logging

from watchFaceParser.models.elements.basic.valueElement import ValueElement

class NoDataUVImageIndexElement(ValueElement):
    def __init__(self, parameter, parent, name = 'None'):
        self._nodatauvimageindex = None
        super(NoDataUVImageIndexElement, self).__init__(parameter, parent, name)


    def getNoDataUVImageIndex(self):
        return self._nodatauvimageindex
