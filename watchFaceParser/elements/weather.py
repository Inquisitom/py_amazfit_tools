from watchFaceParser.elements.weatherElements.temperature import Temperature
from watchFaceParser.elements.weatherElements.icon import Icon
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.timeElements.twoDigits import TwoDigits

class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': Icon},
        2: { 'Name': 'Temperature', 'Type': Temperature},
        #humidity ? -> { 'Name': 'Humidity', 'Type': Number}, #skipping suffixImageIndex
        #wind ?     -> { 'Name': 'Wind', 'Type': Number}, #skipping suffixImageIndex
        10: { 'Name': 'SunriseHour', 'Type': Number},
        11: { 'Name': 'SunriseMinute', 'Type': Number},
        12: { 'Name': 'NoDataSunriseImageIndex', 'Type': 'long'},           
        14: { 'Name': 'SunsetHour', 'Type': Number},                   
        15: { 'Name': 'SunsetMinute', 'Type': Number},           
        16: { 'Name': 'NoDataSunsetImageIndex', 'Type': 'long'},
       
    }