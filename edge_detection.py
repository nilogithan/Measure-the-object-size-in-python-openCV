import cv2 as cv

img = cv.imread(r"images/example_03.png", 0)

# cv.imshow('test', Img)
#
# cv.waitKey(0)
# cv.destroyAllWindows()

print('Original Dimensions : ', img.shape)

width = 350
height = 450
dim = (width, height)

# resize image
resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
edges = cv.Canny(resized,100,200)

print('Resized Dimensions : ', resized.shape)

cv.imshow("Edges", edges)
cv.imshow("Resized",resized)
cv.waitKey(0)
cv.destroyAllWindows()