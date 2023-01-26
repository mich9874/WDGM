from BaseImage import *
from Image import *
from GrayScaleTransform import *
from BaseImage import *
from Histogram import *
from ImageComparison import *
import copy

class Image(GrayScaleTransform, ImageComparison):
    def __init__(self, path: str = None) -> None:
        super().__init__(path)


class Thresholding(BaseImage):
    def threshold(self, value: int) -> Image:
        # metoda dokonujaca operacji segmentacji za pomoca binaryzacji
        img = copy.deepcopy(self)
        img.data[img.data < value] = 0
        img.data[img.data >= value] = 255
        
        return img
