import cv2, numpy

img = cv2.imread('Demon mask.jpg', 1)

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

def invertAll(img):
    return cv2.bitwise_not(img)


# Remove color
def removeBlueChannel(img):
    img[:,:,0] = numpy.zeros([img.shape[0], img.shape[1]])
    return img

def removeGreenChannel(img):
    img[:,:,1] = numpy.zeros([img.shape[0], img.shape[1]])
    return img

def removeRedChannel(img):
    img[:,:,2] = numpy.zeros([img.shape[0], img.shape[1]])
    return img



cv2.imshow("Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() # Method to close the window