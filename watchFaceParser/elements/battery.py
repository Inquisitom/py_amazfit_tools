from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.batteryElements.iconSet import IconSet

class Battery:
    definitions = {
        1: { 'Name': 'Text', 'Type': Number},
        2: { 'Name': 'Images', 'Type': ImageSet}, # gtr
		3: { 'Name': 'Icons', 'Type': IconSet},   # gtr
        6: { 'Name': 'Percent', 'Type': Image},
        7: { 'Name': 'Scale', 'Type': CircleScale}, # verge
    }

