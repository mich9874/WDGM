from BaseImage import *
from Histogram import *


class ImageDiffMethod(Enum):
    mse = 0
    rmse = 1


class ImageComparison(BaseImage):
    def histogram(self) -> Histogram:
        return Histogram(values=self.data)

    def compare_to(self, other: 'Image', method: ImageDiffMethod) -> float:
        x = self.histogram().values
        y = other.histogram().values

        wynik = 0
        for i in range(256):
            wynik += ((x[i]-y[i])**2)

        wynik = wynik/256

        if method.name == 'mse':
            return wynik
        elif method.name == 'rmse':
            return sqrt(wynik)
