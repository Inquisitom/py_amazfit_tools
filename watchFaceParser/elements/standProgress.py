from watchFaceParser.elements.basicElements.circleScale import CircleScale
from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.basicElements.iconSet import IconSet
from watchFaceParser.elements.basicElements.advanceBar import AdvanceBar

class StandProgress:
    definitions = {
        1: { 'Name': 'Images1', 'Type': ImageSet}, # test
        2: { 'Name': 'Sliced', 'Type': IconSet}, # GTS - Silver - WF
        4: { 'Name': 'AdvanceBar', 'Type': AdvanceBar}, # test
        3: { 'Name': 'Circle', 'Type': CircleScale},
        5: { 'Name': 'Unknown5', 'Type': CircleScale}, # verge
        6: { 'Name': 'ClockHand', 'Type': ClockHand},
    }

