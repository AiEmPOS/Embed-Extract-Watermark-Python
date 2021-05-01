import numpy as np
import cv2

def addWatermark(logo_img, original_img, opacity, pos=(100,10)):
    
    opacity = opacity / 100

    image = cv2.cvtColor(original_img, cv2.COLOR_BGR2BGRA)
    print((image.shape[0], image.shape[1]))
    watermark = cv2.cvtColor(logo_img, cv2.COLOR_BGR2BGRA)
    watermark = cv2.resize(watermark, (900, 1300), interpolation=cv2.INTER_LINEAR)
    print((watermark.shape[0], watermark.shape[1]))

    # cv2.imshow('resized', watermark)
    # cv2.imshow('main', image)
    # cv2.waitKey()

    output = image.copy()
    output = cv2.addWeighted(watermark, 0.1, output, 0.9, 0) # output = saturate(src1(I)∗alpha+src2(I)∗beta+gamma)

    cv2.imwrite("./output/addWeight-embed.png", output)

    # cv2.imshow('output', output)
    # cv2.waitKey()

def scaleUpExtractWatermark(img, scale, threshold):

    output = scale * img - threshold # Since most of the watermarks have less opacity than the content of the image, we scale the image up by 2 and decrease the value of the scaled image by the threshold
    output = np.clip(output, 0, 255).astype(np.uint8) # The value < 0 will be set to 0 and the value more than 255 will be set to 255. After that they will be store in the 8 bits int data type

    cv2.imwrite("./output/scale-extract.png", output)

image = cv2.imread("test00.jpg", -1)
watermark = cv2.imread("logoict.png", -1)

print("read successfully")

addWatermark(watermark, image, 100)

# image = cv2.imread("addWeight-embed.png")
# scaleUpExtractWatermark(image, 2, 160)