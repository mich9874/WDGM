import cv2
import numpy as np

# Loading source image
src_image = cv2.imread("zw.png")
#"Filtr tożsamościowy":
kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
#"Filtr górnoprzepustowy":
kernel1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#"Filtr dolnoprzepustowy":
kernel2 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])*(1/9)
#"Rozmycie Gaussowskie 3x3":
kernel3 = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])*(1/16)
#"Rozmycie Gaussowskie 5x5":
kernel4 = np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])*(1/256)
#Sobel
kernel5 = np.array([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
])
resulting_image = cv2.filter2D(src_image, -1, kernel5)

cv2.imshow("original image", src_image)
cv2.imshow("filter2d image", resulting_image)
cv2.waitKey()
cv2.destroyAllWindows()