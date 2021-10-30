import os
import cv2 as cv
import numpy as np
import mahotas as mt
import glob
import re
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

## HARALICK ##


def haralick(img):
    feat = mt.features.haralick(
        img, distance=1, ignore_zeros=True).reshape(1, -1)
    return feat


def huMoments(img):
    features = cv.HuMoments(cv.moments(img)).reshape(1, -1)
    return features


def colorHistogram(img):
    bins = 256
    # compute the color histogram
    hist = cv.calcHist([img], [0], None, [bins], [0, 256])
    # normalize the histogram
    cv.normalize(hist, hist)
    # return the histogram
    return hist.reshape(1, -1)


# load the training dataset
train_path = "C:\\dataset2\\train"
train_names = os.listdir(train_path)

# empty list to hold feature vectors and train labels
train_features = None
train_labels = []
test_features = None
test_labels = []
predicted_labels = []

print("[STATUS] Started extracting haralick textures..")
for train_name in train_names:
    cur_path = train_path + "\\" + train_name
    print(cur_path)
    cur_label = train_name
    i = 1

    for file in glob.glob(cur_path + "\*.jpg"):
        print("Processing Image - {} in {}".format(i, cur_label))
        # read the training image
        image = cv.imread(file)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # extract haralick texture from the image
        haralick_features = haralick(gray)
        huMoments_features = huMoments(gray)
        histogram_features = colorHistogram(gray)
        global_features = np.hstack(
            [haralick_features, huMoments_features, histogram_features])
        # append the feature vector and label
        if train_features is None:
            train_features = global_features.copy()
        else:
            train_features = np.vstack((train_features, global_features))

        train_labels = np.append(train_labels, cur_label)
        # show loop update
        i += 1

# have a look at the size of our feature vector and labels
print("Training features:", train_features.shape)
print("Training labels:", train_labels.shape)

scaler = StandardScaler()
train_features_sc = scaler.fit_transform(train_features, train_labels)

# %%

# create the classifier
print("[STATUS] Creating the classifier..")
#clf_svm = LinearSVC(random_state = 9, dual = False)
clf_knn = KNeighborsClassifier(n_neighbors=10)

# fit the training data and labels
print("[STATUS] Fitting data/label to model..")
# print(train_features)
#clf_svm.fit(train_features_sc, train_labels)
clf_knn.fit(train_features_sc, train_labels)

# loop over the test images
test_path = "C:\\dataset2\\test"

for file in glob.glob(test_path + "\*.jpg"):
    test_name = re.findall(r'\w+', file)
    # read the input image
    image = cv.imread(file)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # extract haralick texture from the image
    haralick_features = haralick(gray)
    huMoments_features = huMoments(gray)
    histogram_features = colorHistogram(gray)
    global_features = np.hstack(
        [haralick_features, huMoments_features, histogram_features])

    test_features_sc = scaler.transform(global_features)

    # evaluate the model and predict label
    #prediction = clf_svm.predict(test_features_sc)[0]
    prediction = clf_knn.predict(test_features_sc)[0]
    predicted_labels = np.append(predicted_labels, prediction)
    test_labels = np.append(test_labels, test_name[3])

    if test_features is None:
        test_features = test_features_sc.copy()
    else:
        test_features = np.vstack((test_features, test_features_sc))

    # show the label
    cv.putText(image, str(prediction), (20, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 3)
    print("Prediction - {}".format(prediction))

    # display the output image
    cv.imshow("Test_Image", image)
    cv.waitKey(0)
cv.destroyAllWindows()

print(test_features)
print(test_labels)
print("Test features:", test_features.shape)
print("Test labels:", test_labels.shape)

cf = confusion_matrix(test_labels, predicted_labels)
tn, fp, fn, tp = confusion_matrix(test_labels, predicted_labels).ravel()
specificity = tn / (tn + fp)
sensibility = tp / (tp + fn)
precision = tp / (tp + fp)
f1_score = 2 * ((precision * specificity) / (precision + specificity))
error_rate = (fp + fn) / (tp + tn + fp + fn)
accuracy = (tp + tn) / (tp + fp + tn + fn)

print("Especificidad: ", specificity)
print("Sensibilidad: ", sensibility)
print("Precisión: ", precision)
print("F1-score: ", f1_score)
print("Error: ", error_rate)
print("Exactitud: ", accuracy)
print(cf)
