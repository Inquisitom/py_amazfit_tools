import logging

from watchFaceParser.models.elements.basic.valueElement import ValueElement

# check d:\_SOFTS\AmazFitX_Watchface_Editor\main_AmazfitX\py_amazfit_tools-AmazfitX\py_amazfit_tools-AmazfitX\watchFaceParser\models\elements\weather\weatherIconElement.py
class NoDataSunriseImageIndexElement(ValueElement):
    def __init__(self, parameter, parent, name = 'None'):
        self._nodatasunriseimageindex = None
        super(NoDataSunriseImageIndexElement, self).__init__(parameter, parent, name)


    def getNoDataSunriseImageIndex(self):
        return self._nodatasunriseimageindex
