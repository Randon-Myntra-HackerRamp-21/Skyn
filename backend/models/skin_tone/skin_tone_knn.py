"""
To classify the input skin into one of the 6 skin tones
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from skin_detection import skin_detection


def skin_tone_knn(image_path):
    mean_color_values = skin_detection(image_path)
    df = pd.read_csv("skin_tone_dataset.csv")
    X = df.iloc[:, [1, 2, 3]].values
    y = df.iloc[:, 0].values

    classifier = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=2)
    classifier.fit(X, y)

    X_test = [mean_color_values]
    y_pred = classifier.predict(X_test)
    return y_pred[0]


print(skin_tone_knn("D:\Mynthra-hack\skintone\simple-skin-detection\ML\Skin metrics\Skin tone\public\\test images\Optimized-DynamicRange_SamsungGalaxyS10Plus.jpg"))
