import numpy as np
import cv2

img = cv2.imread("./sample-watermark-img.jpg")

output = 2.0 * img - 160 # Since most of the watermarks have less opacity than the content of the image, we scale the image up by 2 and decrease the value of the scaled image by the threshold
output = np.clip(output, 0, 255).astype(np.uint8) # The value < 0 will be set to 0 and the value more than 255 will be set to 255. After that they will be store in the 8 bits int data type

cv2.imwrite("./output/scale-extract.png", output)
