from skimage import io
import numpy as np

image = io.imread("test00.jpg")
watermark = io.imread("logoict60ops.png")

imgArr = np.array(image)
waterArr = np.array(watermark)
# for i in imgs:
#     for j in i:
#         print(j)




    