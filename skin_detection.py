import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    Totsu, threshold_image_otsu = cv2.threshold(
        image_grayscale, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print("Totsu : ", Totsu)
    # display_image(threshold_image_otsu, "otsu")

    histogram, bin_edges = np.histogram(image_grayscale.ravel(), 256, [0, 256])
    Tmax = np.where(histogram[:] == max(histogram[:]))[0][0]
    print("Tmax :", Tmax)

    Tfinal = round((Tmax + Totsu)/2) if Tmax > 10 else round((Tmax + Totsu)/4)

    # print("Histogram : \n", histogram)
    # print("bin_edges : \n", bin_edges)
    plt.figure()
    plt.title("Image Histogram")
    plt.xlabel("pixel value")
    plt.ylabel("pixel frequency")
    plt.xlim([0, 256])
    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.axvline(x=Tmax, label="Tmax", color='red', linestyle="--")
    plt.axvline(x=Totsu, label="Totsu", color='green', linestyle="--")
    plt.axvline(x=Tfinal, label="Tfinal", color='yellow', linestyle="-")
    plt.legend()
    plt.show()

    threshold_type = cv2.THRESH_BINARY if Tmax < 200 else cv2.THRESH_BINARY_INV
    Totsu, threshold_image = cv2.threshold(
        image_grayscale, Tfinal, 255, threshold_type)
    display_image(threshold_image, "threshold_image")
    masked_img = cv2.bitwise_and(img_BGR, img_BGR, mask=threshold_image)
    display_image(masked_img, "masked_img")
    # threshold_image_binary = 1 - threshold_image_otsu/255
    # cv2.imshow("img_binary", threshold_image_binary)
    # threshold_image_otsuage_binary = npthreshold_image_otsu(
    #     threshold_image_binary[:, :, np.newaxis], 3, axis=2)
    # img_face_only = np.multiply(threshold_image_binary, img_BGR)
    # # cv2.imshow("bgr", img_BGR)
    # if(img_face_only.all() == threshold_image_binary.all()):
    #     print("Is the same brudda\n")
    # else:
    #     print("No brudda! not same\n")
    return masked_img

# ---- MAIN ----#


# read in image into openCV
image_path = "D:\My Stuff\Pictures\phonephotos\\20200604_070026.jpg"
img_BGR = cv2.imread(image_path, 3)
img_BGR = cv2.resize(img_BGR, (375, 500))

# Grayscle and Thresholding and HSV & YCrCb color space conversions
img_grayscale = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
# foreground and background segmentation
img_no_background = segment_otsu(img_grayscale, img_BGR)
img_HSV = cv2.cvtColor(img_no_background, cv2.COLOR_BGR2HSV)
img_YCrCb = cv2.cvtColor(img_no_background, cv2.COLOR_BGR2YCrCb)

# Display all images
display_image(img_BGR, "BGR")
display_image(img_grayscale, "grayscale")
display_image(img_no_background, "segmented BGR")
display_image(img_HSV, "HSV")
display_image(img_YCrCb, "YCrCb")

height, width = img_grayscale.shape
img_skin_predict = img_grayscale

# Predict skin pixels
for i in range(height):
    for j in range(width):
        if((img_HSV.item(i, j, 0) <= 170) and (140 <= img_YCrCb.item(i, j, 1) <= 170) and (90 <= img_YCrCb.item(i, j, 2) <= 120)):
            img_skin_predict[i, j] = 1
        else:
            img_skin_predict[i, j] = 0
display_image(cv2.bitwise_and(img_BGR, img_BGR,
              mask=img_skin_predict), "skin prediction")

# Contruction the dataframe for K-means clustering
dframe = pd.DataFrame()
dframe['H'] = img_HSV.reshape([-1, 3])[:, 0]

# Getting the y-x coordintated
gray = cv2.cvtColor(img_no_background, cv2.COLOR_BGR2GRAY)
yx_coords = np.column_stack(np.where(gray >= 0))
dframe['Y'] = yx_coords[:, 0]
dframe['X'] = yx_coords[:, 1]

dframe['Cr'] = img_YCrCb.reshape([-1, 3])[:, 1]
dframe['Cb'] = img_YCrCb.reshape([-1, 3])[:, 2]
dframe['I'] = img_skin_predict.reshape([1, img_skin_predict.size])[0]
print("initial dframe : \n", dframe)

# Remove Black pixels - which are already segmented
dframe_removed = dframe[dframe['H'] == 0]
dframe.drop(dframe[dframe['H'] == 0].index, inplace=True)
print("filtered dframe : \n", dframe)

# K-means
kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=5,
    max_iter=100,
    random_state=42
)
kmeans.fit(dframe)

# Add cluster-label column to the dataframe
dframe_removed['cluster'] = np.full((dframe_removed.shape[0], 1), -1)
dframe['cluster'] = kmeans.labels_

# Get the skin cluster label - which has the highest I value
km_cc = kmeans.cluster_centers_
skin_cluster_row = km_cc[km_cc[:, -1] == max(km_cc[:, -1]), :]
skin_cluster_label = np.where(
    [np.allclose(row, skin_cluster_row) for row in km_cc])[0][0]

# Append removed pixels to the dataframe and get cluster matrix
dframe = dframe.append(dframe_removed, ignore_index=False).sort_index()
dframe['cluster'] = (dframe['cluster'] == skin_cluster_label).astype(int) * 255
cluster_label_mat = np.asarray(
    dframe['cluster'].values.reshape(height, width), dtype=np.uint8)

# Print obtained
print("kmeans.cluster_centers_", km_cc)
print("skin_cluster_row", skin_cluster_row)
print("skin_cluster_label", skin_cluster_label)
print("skin_cluster_label", cluster_label_mat)
print("complete dframe : \n", dframe)

# final segmentation
final_segment_img = cv2.bitwise_and(img_BGR, img_BGR, mask=cluster_label_mat)
display_image(final_segment_img, "final segmentation")
