import cv2
import numpy as np
import pandas as pd

# image_path = "images\cover2.jpg"
# img_BGR = cv2.imread(image_path, 3)

img_BGR = np.array([
    [[0, 0, 0],     [0, 0, 255],     [0, 255, 0]],
    [[0, 255, 255], [255, 0, 0],     [255, 0, 255]],
    [[255, 255, 0], [255, 255, 255], [75, 75, 75]],
]).astype(np.uint8)

gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)

# get coordinates (y,x) --- alternately see below for (x,y)
yx_coords = np.column_stack(np.where(gray >= 0))
print(yx_coords)

# print(img_BGR)

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
img_YCrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)


dframe = pd.DataFrame(img_HSV.reshape([-1, 3])[:, 0], columns=['H'])

dframe['Y'] = yx_coords[:, 0]
dframe['X'] = yx_coords[:, 1]

dframe['Cr'] = img_YCrCb.reshape([-1, 3])[:, 1]
dframe['Cb'] = img_YCrCb.reshape([-1, 3])[:, 2]

height, width = gray.shape

for i in range(height):
    for j in range(width):
        if((img_HSV.item(i, j, 0) <= 170) and (140 <= img_YCrCb.item(i, j, 1) <= 170) and (90 <= img_YCrCb.item(i, j, 2) <= 120)):
            gray[i, j] = 255
        else:
            gray[i, j] = 0

dframe['I'] = gray.reshape([1, 9])[0]

print(dframe)

# cv2.imshow("HSV", cv2.resize(img_HSV, None, fx=100, fy=100))
# cv2.imshow("YCrCb", cv2.resize(img_YCrCb, None, fx=100, fy=100))
# cv2.imshow("BGR", cv2.resize(img_BGR, None, fx=100, fy=100))
# cv2.imshow("gray", cv2.resize(gray, None, fx=100, fy=100))
# cv2.waitKey()
# cv2.destroyAllWindows()
