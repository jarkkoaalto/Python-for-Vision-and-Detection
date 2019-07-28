import cv2

# Read an image
# cv2.imread() second argument is a flag which specifies the way 
# image should be read.
# 
# flag 1. Loads a color image
# flag 0. Loads image in grayscale mode
# flag -1. Loads image as such including alpha channel
#
img = cv2.imread('lena.jpg', -1) 
print(img) # Print matrix

# Display image, show image only millisecond, you must add cv2.waitKey(5000)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k==27;
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('copy_lena.png', img)
    cv2.destroyAllWindows()

# Write image in the file