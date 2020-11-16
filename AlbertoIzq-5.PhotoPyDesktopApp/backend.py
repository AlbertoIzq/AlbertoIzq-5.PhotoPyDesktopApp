import cv2

img = cv2.imread('Demon mask.jpg', 1)

print(img)
print(img.shape) # number of pixels
print(img.ndim) # number of dimensions

def RotateRight(img):
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

def RotateLeft(img):
    return cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

def FlipVertical(img):
    return cv2.flip(img, 0)

def FlipHorizontal(img):
    return cv2.flip(img, 1)

img = FlipHorizontal(img)

resized_img = cv2.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4)))

cv2.imshow("Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows() # Method to close the window