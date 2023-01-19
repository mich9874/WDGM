from BaseImage import *
class GrayScaleTransform(BaseImage):
    def to_gray(self) -> BaseImage:
        pixels = np.empty(shape=(self.data.shape[0], self.data.shape[1]))
        for x in range(self.data.shape[0]):
            for y in range(self.data.shape[1]):
                red = self.data[x,y][0]
                green = self.data[x,y][1]
                blue = self.data[x,y][2]
                value = 0.30*red + \
                        .59*green + 0.11*blue
                pixels[x, y] = value

        gray = BaseImage()
        gray.data = pixels
        return gray

    def to_sepia(self, alpha_beta = (None, None), w: int = None) -> BaseImage:
        self = self.to_gray()
        self.data = np.dstack((self.data, self.data, self.data))
        self.data = (self.data).astype(np.float16)

        alfa = alpha_beta[0]
        beta = alpha_beta[1]

        if (alpha_beta != (None, None) and alfa > 1 and beta < 1 and alfa + beta == 2):
            self.data[:, :, 0] *= alfa
            self.data[:, :, 2] *= beta
        elif (w != None and w >= 20 and w <= 40):
            self.data[:, :, 0] += 2 * w
            self.data[:, :, 1] += w

        self.data[self.data > 255] = 255
        self.data[self.data < 0] = 0
        self.data = (self.data).astype(np.uint8)

        return self