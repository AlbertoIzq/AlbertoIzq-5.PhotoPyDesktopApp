import cv2, numpy

img = cv2.imread('Demon mask.jpg', cv2.IMREAD_UNCHANGED)

print(img)
print(img.shape) # number of pixels
print(img.ndim) # number of dimensions

# Orientation
def rotateRight(img):
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

def rotateLeft(img):
    return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

def flipVertical(img):
    return cv2.flip(img, 0)

def flipHorizontal(img):
    return cv2.flip(img, 1)


# Remove color
def removeBlueChannel(img):
    img[:,:,0] = 0 #numpy.zeros([img.shape[0], img.shape[1]])
    return img

def removeGreenChannel(img):
    img[:,:,1] = 0
    return img

def removeRedChannel(img):
    img[:,:,2] = 0
    return img


# Extract color
def extractBlueChannel(img):
    img[:, :, 1] = 0
    img[:, :, 2] = 0
    return img

def extractGreenChannel(img):
    img[:, :, 0] = 0
    img[:, :, 2] = 0
    return img

def extractRedChannel(img):
    img[:, :, 0] = 0
    img[:, :, 1] = 0
    return img


# Invert color
def invertAll(img):
    return cv2.bitwise_not(img)

def invertBlueChannel(img):
    img[:, :, 0] = 255 - img[:, :, 0] #~img[:, :, 1]
    return img

def invertGreenChannel(img):
    img[:, :, 1] = 255 - img[:, :, 1]
    return img

def invertRedChannel(img):
    img[:, :, 2] = 255 - img[:, :, 2]
    return img


# Resize
def resizeRatioPercent(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    return cv2.resize(img, (width, height))

def resizeRatioWidth(img, width):
    height = int( width * img.shape[0] / img.shape[1])
    print(height)
    return cv2.resize(img, (width, height))

def resizeRatioHeight(img, height):
    width = int(height * img.shape[1] / img.shape[0])
    print(width)
    return cv2.resize(img, (width, height))

def resizeWidthHeight(img, width, height):
    return cv2.resize(img, (width, height))


img = resizeRatioPercent(img, 25)
modified_img = invertRedChannel(img)

cv2.imshow("Image", modified_img)
cv2.waitKey(0)
cv2.destroyAllWindows() # Method to close the window