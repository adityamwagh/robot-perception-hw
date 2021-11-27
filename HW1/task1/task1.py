import os
import cv2
import numpy as np

CUR_DIR = os.getcwd()

# Reading the image file, in the BGR color space.
image = cv2.imread(os.path.join(CUR_DIR, "for_watson.png"), cv2.IMREAD_COLOR)

# Transforming BGR image to Grayscale - MESSAGE : My Dear Watson,
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("image_gray", image_gray)
cv2.imwrite("for_watson_gray.png", image_gray)

# Sharpening the grayscale image using a kernel of size 3x3.
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
image_gray_sharp = cv2.filter2D(image_gray, -1, kernel)
cv2.imshow("image_gray_sharp", image_gray_sharp)
cv2.imwrite("for_watson_gray_sharp.png", image_gray_sharp)

# Press 0 to destroy all windows.
cv2.waitKey(0)
cv2.destroyAllWindows()
