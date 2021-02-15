from watchFaceParser.elements.weatherElements.temperature import Temperature
from watchFaceParser.elements.weatherElements.icon import Icon
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.timeElements.twoDigits import TwoDigits

class Weather:
    definitions = {
        1: { 'Name': 'Icon', 'Type': Icon},
        2: { 'Name': 'Temperature', 'Type': Temperature},
        #6: { 'Name': 'Humidity', 'Type': Number},
        #4: { 'Name': 'HumiditySuffixImageIndex', 'Type': 'long'}, #-> not tested
        #5: { 'Name': 'UV', 'Type': Number}, -> CANNOT FIND WHAT IT IS !!!!!!!!!!!!!!!!!!!!!!!!
        #6: { 'Name': 'NoDataUVImageIndex', 'Type': 'long'}, #-> not tested
        #humidity ? -> { 'Name': 'Humidity', 'Type': Number}, #skipping HumiditySuffixImageIndex
        #wind ?     -> { 'Name': 'Wind', 'Type': Number}, #skipping suffixImageIndex
        10: { 'Name': 'SunriseHour', 'Type': Number},
        11: { 'Name': 'SunriseMinute', 'Type': Number},
        12: { 'Name': 'NoDataSunriseImageIndex', 'Type': 'long'},           
        14: { 'Name': 'SunsetHour', 'Type': Number},                   
        15: { 'Name': 'SunsetMinute', 'Type': Number},           
        16: { 'Name': 'NoDataSunsetImageIndex', 'Type': 'long'},
    }

#HUMIDITY - Moisture value
#"Humidity": { 
        #"TopLeftX": 73, 
        #"TopLeftY": 94, 
        #"BottomRightX": 109, 
        #"BottomRightY": 110, 
        #"Alignment": "TopRight", 
        #"SpacingX": 1, 
        #"SpacingY": 0, #not valid for X ?
        #"ImageIndex": 100, 
        #"ImagesCount": 10 
      #}, 
      #"HumiditySuffixImageIndex": 110 #Humidity designation

#WIND - Wind speed
#"Text": { 
#        "TopLeftX": 11, 
#        "TopLeftY": 94, 
#        "BottomRightX": 61, 
#        "BottomRightY": 110, 
#        "Alignment": "BottomLeft", 
#        "SpacingX": 1, 
#        "SpacingY": 0, 
#        " ImageIndex ": 100, 
#        " ImagesCount ": 10 
#      }, 
#      " ImageSuffixEN ": 111, #Non-Chinese wind speed notation
#      " ImageSuffixCN1 ": 112, #Chinese wind speed notation
#      " ImageSuffixCN2 ": 113 #Chinese wind speed notation