import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

pd.options.mode.chained_assignment = None  # default='warn'

# main


def skin_detection(img_path):
    original = read_image(img_path)
    images = image_conversions(original)
    height, width = skin_predict(images)
    dframe, dframe_removed = dataframe(images)
    skin_cluster_row, skin_cluster_label = skin_cluster(dframe)
    cluster_label_mat = cluster_matrix(
        dframe, dframe_removed, skin_cluster_label, height, width)
    final_segment(images, cluster_label_mat)
    display_all_images(images)
    # write_all_images(images)
    skin_cluster_row = np.delete(skin_cluster_row, 1)
    skin_cluster_row = np.delete(skin_cluster_row, 2)
    return np.delete(skin_cluster_row, -1)
    # return images["final_segment"]


# Plot Histogram and Threshold values
def plot_histogram(histogram, bin_edges, Totsu, Tmax, Tfinal):
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

# display an image plus label and wait for key press to continue


def display_image(image, name):
    window_name = name
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Display all images


def display_all_images(images):
    for key, value in images.items():
        display_image(value, key)

# write all images


def write_all_images(images):
    for key, value in images.items():
        cv2.imwrite(key+'.jpg', value)

# read in image into openCV


def read_image(dir):
    maxwidth, maxheight = 400, 500
    image_path = dir
    img_BGR = cv2.imread(image_path, 3)
    f1 = maxwidth / img_BGR.shape[1]
    f2 = maxheight / img_BGR.shape[0]
    f = min(f1, f2)  # resizing factor
    dim = (int(img_BGR.shape[1] * f), int(img_BGR.shape[0] * f))
    img_BGR = cv2.resize(img_BGR, dim)
    # img_BGR = cv2.resize(img_BGR, (375, 500))
    return img_BGR

# segment using otsu binarization and thresholding


def thresholding(images):
    histogram, bin_edges = np.histogram(
        images["grayscale"].ravel(), 256, [0, 256])
    Totsu, threshold_image_otsu = cv2.threshold(
        images["grayscale"], 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    Tmax = np.where(histogram[:] == max(histogram[:]))[0][0]
    Tfinal = round((Tmax + Totsu)/2) if Tmax > 10 else round((Tmax + Totsu)/4)

    plot_histogram(histogram, bin_edges, Totsu, Tmax, Tfinal)

    threshold_type = (cv2.THRESH_BINARY if Tmax <
                      220 else cv2.THRESH_BINARY_INV)
    Tfinal, threshold_image = cv2.threshold(
        images["grayscale"], Tfinal, 255, threshold_type)

    masked_img = cv2.bitwise_and(
        images["BGR"], images["BGR"], mask=threshold_image)
    return masked_img


# Grayscle and Thresholding and HSV & YCrCb color space conversions
def image_conversions(img_BGR):
    images = {
        "BGR": img_BGR,
        "grayscale": cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
    }
    images["thresholded"] = thresholding(images)
    images["HSV"] = cv2.cvtColor(
        images["thresholded"], cv2.COLOR_BGR2HSV)
    images["YCrCb"] = cv2.cvtColor(
        images["thresholded"], cv2.COLOR_BGR2YCrCb)
    # display_all_images(images)
    return images


# Predict skin pixels
def skin_predict(images):
    height, width = images["grayscale"].shape
    images["skin_predict"] = np.empty_like(images["grayscale"])
    images["skin_predict"][:] = images["grayscale"]

    for i in range(height):
        for j in range(width):
            if((images["HSV"].item(i, j, 0) <= 170) and (140 <= images["YCrCb"].item(i, j, 1) <= 170) and (90 <= images["YCrCb"].item(i, j, 2) <= 120)):
                images["skin_predict"][i, j] = 255
            else:
                images["skin_predict"][i, j] = 0
    return height, width

# Contruction the dataframe for K-means clustering


def dataframe(images):
    dframe = pd.DataFrame()
    dframe['H'] = images["HSV"].reshape([-1, 3])[:, 0]

    # Getting the y-x coordintated
    gray = cv2.cvtColor(images["thresholded"], cv2.COLOR_BGR2GRAY)
    yx_coords = np.column_stack(np.where(gray >= 0))
    dframe['Y'] = yx_coords[:, 0]
    dframe['X'] = yx_coords[:, 1]

    dframe['Cr'] = images["YCrCb"].reshape([-1, 3])[:, 1]
    dframe['Cb'] = images["YCrCb"].reshape([-1, 3])[:, 2]
    dframe['I'] = images["skin_predict"].reshape(
        [1, images["skin_predict"].size])[0]

    # Remove Black pixels - which are already segmented
    dframe_removed = dframe[dframe['H'] == 0]
    dframe.drop(dframe[dframe['H'] == 0].index, inplace=True)
    return dframe, dframe_removed

# cluster skin pixels using K-means


def skin_cluster(dframe):
    # K-means
    kmeans = KMeans(
        init="random",
        n_clusters=3,
        n_init=5,
        max_iter=100,
        random_state=42
    )
    kmeans.fit(dframe)

    # Get the skin cluster label - which has the highest I value
    km_cc = kmeans.cluster_centers_
    skin_cluster_row = km_cc[km_cc[:, -1] == max(km_cc[:, -1]), :]
    skin_cluster_label = np.where(
        [np.allclose(row, skin_cluster_row) for row in km_cc])[0][0]

    # Add cluster-label column to the dataframe
    dframe['cluster'] = kmeans.labels_
    return skin_cluster_row, skin_cluster_label


# Append removed pixels to the dataframe and get cluster matrix
def cluster_matrix(dframe, dframe_removed, skin_cluster_label, height, width):
    dframe_removed['cluster'] = np.full((len(dframe_removed.index), 1), -1)
    dframe = dframe.append(dframe_removed, ignore_index=False).sort_index()
    dframe['cluster'] = (dframe['cluster'] ==
                         skin_cluster_label).astype(int) * 255
    cluster_label_mat = np.asarray(
        dframe['cluster'].values.reshape(height, width), dtype=np.uint8)
    return cluster_label_mat

# final segmentation


def final_segment(images, cluster_label_mat):
    final_segment_img = cv2.bitwise_and(
        images["BGR"], images["BGR"], mask=cluster_label_mat)
    images["final_segment"] = final_segment_img
    # display_image(final_segment_img, "final segmentation")


# print(skin_detection("images\Optimized-selfieNig-cropped.jpg"))
