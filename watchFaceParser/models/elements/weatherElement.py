import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class WeatherElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._icon = None
        self._temperature = None
        self._sunrisehour = None
        self._sunriseminute = None
        self._sunsethour = None
        self._sunsetminute = None
        self._nodatasunsetimageindex = None
        self._nodatasunriseimageindex = None
        super(WeatherElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getIcon(self):
        return self._icon

    def getTemperature(self):
        return self._temperature

    def getNoDataSunsetImageIndex(self):
        return self._nodatasunsetimageindex

    def getNoDataSunriseImageIndex(self):
        return self._nodatasunriseimageindex
        
    def getSunriseHour(self):
        return self._sunrisehour

    def getSunriseMinute(self):
        return self._sunriseminute

    def getSunsetHour(self):
        return self._sunsethour

    def getSunsetMinute(self):
        return self._sunsetminute
        
    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.weather.weatherIconElement import WeatherIconElement
            self._icon = WeatherIconElement(parameter = parameter, parent = self, name = '?_icon?')
            return self._icon
        elif parameterId == 2:
            from watchFaceParser.models.elements.weather.temperatureElement import TemperatureElement # temp.
            self._temperature = TemperatureElement(parameter = parameter, parent = self, name = '?_temperature?')
            return self._temperature
        elif parameterId == 10:
            from watchFaceParser.models.elements.weather.sunrisehourElement import SunriseHourElement 
            self._sunrisehour = SunriseHourElement(parameter = parameter, parent = self, name = '?_sunrisehour?')
            return self._sunrisehour
        elif parameterId == 11:
            from watchFaceParser.models.elements.weather.sunriseminuteElement import SunriseMinuteElement 
            self._sunriseminute = SunriseMinuteElement(parameter = parameter, parent = self, name = '?_sunriseminute?')
            return self._sunriseminute
        elif parameterId == 12:
            from watchFaceParser.models.elements.weather.nodatasunriseimageindexElement import NoDataSunriseImageIndexElement
            self._nodatasunriseimageindex = NoDataSunriseImageIndexElement(parameter = parameter, parent = self, name = '?_nodatasunriseimageindex?')
            return self._nodatasunriseimageindex         
        elif parameterId == 14:
            from watchFaceParser.models.elements.weather.sunsethourElement import SunsetHourElement 
            self._sunsethour = SunsetHourElement(parameter = parameter, parent = self, name = '?_sunsethour?')
            return self._sunsethour
        elif parameterId == 15:
            from watchFaceParser.models.elements.weather.sunsetminuteElement import SunsetMinuteElement
            self._sunsetminute = SunsetMinuteElement(parameter = parameter, parent = self, name = '?_sunsetminute?')
            return self._sunsetminute
        elif parameterId == 16:
            from watchFaceParser.models.elements.weather.nodatasunsetimageindexElement import NoDataSunsetImageIndexElement
            self._nodatasunsetimageindex = NoDataSunsetImageIndexElement(parameter = parameter, parent = self, name = '?_nodatasunsetimageindex?')
            return self._nodatasunsetimageindex            
        else:
            print ("Unknown WeatherElement",parameterId)
            return super(WeatherElement, self).createChildForParameter(parameter)