from GrayScaleTransform import *
from ImageComparison import *
from Thresholding import *

class Image(GrayScaleTransform, ImageComparison, Thresholding):
    def __init__(self, path: str = None) -> None:
        super().__init__(path)