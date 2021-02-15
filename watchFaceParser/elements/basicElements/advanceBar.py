from watchFaceParser.models.color import Color
from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.elements.basicElements.image import Image

class AdvanceBar:
    definitions = {
        1: { 'Name': 'TopX', 'Type': Coordinates},
        2: { 'Name': 'BottomY', 'Type': Coordinates},
        3: { 'Name': 'Width', 'Type': 'long'},
        4: { 'Name': 'Flatness', 'Type': 'long'}, #0=round, 90=triangular, 180=flat
        6: { 'Name': 'Color', 'Type': Color}
    }
