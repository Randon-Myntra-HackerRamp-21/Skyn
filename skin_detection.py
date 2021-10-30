import cv2
import numpy as np
from numpy.core.numeric import allclose
import pandas as pd
from sklearn.cluster import KMeans

# ---- START FUNCTIONS ----#

# display an image plus label and wait for key press to continue


def display_image(image, name):
    window_name = name
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


# segment using otsu binarization and thresholding
def segment_otsu(image_grayscale, img_BGR):
    threshold_value, threshold_image = cv2.threshold(
        image_grayscale, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    display_image(threshold_image, "otsu")
    threshold_image_binary = 1 - threshold_image/255
    # cv2.imshow("img_binary", threshold_image_binary)
    threshold_image_binary = np.repeat(
        threshold_image_binary[:, :, np.newaxis], 3, axis=2)
    img_face_only = np.multiply(threshold_image_binary, img_BGR)
    # cv2.imshow("bgr", img_BGR)
    if(img_face_only.all() == threshold_image_binary.all()):
        print("Is the same brudda\n")
    else:
        print("No brudda! not same\n")
    return img_face_only

# ---- MAIN ----#


# read in image into openCV BGR and grayscale
image_path = "images\cover2.jpg"

img_BGR = cv2.imread(image_path, 3)
display_image(img_BGR, "BGR")

img_grayscale = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
display_image(img_grayscale, "grayscale")

# foreground and background segmentation (otsu)
img_face_only = segment_otsu(img_grayscale, img_BGR)
display_image(img_face_only, "segmented BGR")

# convert to HSV and YCrCb color spaces and detect potential pixels
img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
display_image(img_HSV, "HSV")
img_YCrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)
display_image(img_YCrCb, "YCrCb")

# aggregate skin pixels
# blue = []
# green = []
# red = []

height, width = img_grayscale.shape

for i in range(height):
    for j in range(width):
        if((img_HSV.item(i, j, 0) <= 170) and (140 <= img_YCrCb.item(i, j, 1) <= 170) and (90 <= img_YCrCb.item(i, j, 2) <= 120)):
            img_grayscale[i, j] = 255
        else:
            img_grayscale[i, j] = 0


display_image(img_grayscale, "final segmentation")

# Contruction the dataframe for K-means clustering
gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
yx_coords = np.column_stack(np.where(gray >= 0))

dframe = pd.DataFrame(img_HSV.reshape([-1, 3])[:, 0], columns=['H'])

dframe['Y'] = yx_coords[:, 0]
dframe['X'] = yx_coords[:, 1]

dframe['Cr'] = img_YCrCb.reshape([-1, 3])[:, 1]
dframe['Cb'] = img_YCrCb.reshape([-1, 3])[:, 2]

dframe['I'] = img_grayscale.reshape([1, img_grayscale.size])[0]


kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=5,
    max_iter=100,
    random_state=42
)
kmeans.fit(dframe)

dframe['cluster'] = kmeans.labels_
print(dframe)
km_cc = kmeans.cluster_centers_
skin_cluster_row = km_cc[km_cc[:, -1] == max(km_cc[:, -1]), :]
skin_cluster = np.where([np.allclose(row, skin_cluster_row)
                        for row in km_cc])[0][0]


print(km_cc)
print(skin_cluster_row)
print(skin_cluster)
for i in range(height):
    for j in range(width):
        # This conditional is taking almost eternity for this loops to process
        if (not dframe.loc[(dframe['Y'] == i) & (dframe['X'] == j)]['cluster'].values[0] == skin_cluster):
            img_BGR[i, j] = [0, 0, 0]

display_image(img_BGR, "final segmentation")
# print(dframe.loc[(dframe['Y'] == 0) & (dframe['X'] == 0)]['cluster'].values[0])

# for i in range (height):
#     for j in range (width):
#         if((img_HSV.item(i, j, 0) <= 170) and (140 <= img_YCrCb.item(i, j, 1) <= 170) and (90 <= img_YCrCb.item(i, j, 2) <= 120)):
#             blue.append(img_face_only[i, j].item(0))
#             green.append(img_face_only[i, j].item(1))
#             red.append(img_face_only[i, j].item(2))
#         else:
#             img_face_only[i, j] = [0, 0, 0]
#             img_BGR[i, j] = [0, 0, 0]

# display_image(img_face_only, "final segmentation")

# determine mean skin tone estimate
# skin_tone_estimate_BGR = [np.mean(blue), np.mean(green), np.mean(red)]
# print ("mean skin tone estimate (BGR)", skin_tone_estimate_BGR[0], skin_tone_estimate_BGR[1], skin_tone_estimate_BGR[2], "]")
