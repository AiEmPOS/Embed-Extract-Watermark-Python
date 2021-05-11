import numpy as np
import cv2
from PIL import Image

def addWatermarkImBlend(logo_img, original_img):
    
    image = cv2.cvtColor(original_img, cv2.COLOR_BGR2BGRA)
    print((image.shape[0], image.shape[1]))
    watermark = cv2.cvtColor(logo_img, cv2.COLOR_BGR2BGRA)
    watermark = cv2.resize(watermark, ( image.shape[1], image.shape[0]), interpolation=cv2.INTER_LINEAR)
    print((watermark.shape[0], watermark.shape[1]))

    # cv2.imshow('resized', watermark)
    # cv2.imshow('main', image)
    # cv2.waitKey()

    output = image.copy()
    output = cv2.addWeighted(watermark, 0.1, output, 0.9, 0) # output = saturate(src1(I)∗alpha+src2(I)∗beta+gamma)

    cv2.imwrite("./output/addWeight-embed.png", output)

    # cv2.imshow('output', output)
    # cv2.waitKey()

def addWatermarkPaste(logo_img, original_img):
    
    width, height = original_img.size 
    logo_img = logo_img.resize((int(width), int(height/2)))
    output = Image.new(mode = "RGBA", size = (width, height), color = (0, 0, 0, 0))

    output.paste(original_img, (0, 0), mask = original_img)
    output.paste(logo_img, (0, int(height/4)), mask = logo_img)
    # output.paste(original_img, (0, 0), mask = original_img)
    output.show()

    output.save("./output/paste-embed.png")

    # Pasting logo_img image on top of original_img 
    # starting at coordinates (0, 0)
    
    # original_img.paste(logo_img, (0, int(height/4)), mask = logo_img)
    
    # Displaying the image
    
    # original_img.show()


def scaleUpExtractWatermark(img, scale, threshold):
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    output = (scale * img) - threshold # Since most of the watermarks have less opacity than the content of the image, we scale the image up by 2 and decrease the value of the scaled image by the threshold
    output = np.clip(output, 0, 255).astype(np.uint8) # The value < 0 will be set to 0 and the value more than 255 will be set to 255. After that they will be store in the 8 bits int data type

    cv2.imwrite("./output/scale-extract.png", output)

image = cv2.imread("test00.jpg", -1)
watermark = cv2.imread("logoict.png", -1)

print("read successfully")

# addWatermarkImBlend(watermark, image)

image = cv2.imread("./sample-watermark-img.jpg")
scaleUpExtractWatermark(image, 2.0, 160)

# Opening the primary image (used in background)
image = Image.open(r"test00.png")
# Opening the secondary image (overlay image)
watermark = Image.open(r"logoict40opa.png")

# addWatermarkPaste(watermark, image)

