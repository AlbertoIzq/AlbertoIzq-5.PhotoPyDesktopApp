import cv2, numpy

img = cv2.imread('Demon mask.jpg', cv2.IMREAD_UNCHANGED)

# Orientation
def rotateRight(img):
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

def rotateLeft(img):
    return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

def flipVertical(img):
    return cv2.flip(img, 0)

def flipHorizontal(img):
    return cv2.flip(img, 1)


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
    return cv2.bitwise_not(img) #255 - img

def invertBlueChannel(img):
    img[:, :, 0] = 255 - img[:, :, 0] #~img[:, :, 1]
    return img

def invertGreenChannel(img):
    img[:, :, 1] = 255 - img[:, :, 1]
    return img

def invertRedChannel(img):
    img[:, :, 2] = 255 - img[:, :, 2]
    return img


# Other Effects
def effectGray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def effectBlur(img, k):
    return cv2.GaussianBlur(img, ksize=(k, k), sigmaY = 0, sigmaX = 0) #cv2.blur(img, (k, k))

def effectPencilSketch(img, k):
    img_gray = changeToGray(img)
    img_gray_inv = invertAll(img_gray)
    img_blur = blurGaussian(img_gray_inv, k)
    return dodgeV2(img_gray, img_blur) # Blend both images

def effectCharcoal(img, k):
    img = effectGray(img)
    return img - effectBlur(img, k)

def effectSharpen(img):
    kernel = numpy.array([[-1, -1, -1],
                          [-1, 9, -1],
                          [-1, -1, -1]])
    return cv2.filter2D(img, -1, kernel)

def effectSepia(img):
    kernel = numpy.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.filter2D(img, -1, kernel)

def effectEmboss(img):
    kernel = numpy.array([[0,-1,-1],
                       [1,0,-1],
                       [1,1,0]])
    return cv2.filter2D(img, -1, kernel)

def effectEdge(img, k): # High pass filter
   kernel = numpy.array([[0.0, -1.0, 0.0], 
                        [-1.0, k, -1.0],
                        [0.0, -1.0, 0.0]])
   kernel = kernel/(numpy.sum(kernel) if numpy.sum(kernel)!=0 else 1)
   return cv2.filter2D(img, -1, kernel)

def effectPixel(img, p):
    height, width = img.shape[:2] # Get input size
    w, h = (p, p)  # Desired "pixelated" size
    temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR) # Resize input to "pixelated" size
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST) # Initialize output image


# Additional functions
def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def burnV2(image, mask):
  return 255 - cv2.divide(255-image, 255-mask, scale=256)


img = resizeRatioPercent(img, 25)

modified_img = effectCharcoal(img, 31)

cv2.imshow("Image", modified_img)
cv2.waitKey(0)
cv2.destroyAllWindows() # Method to close the window