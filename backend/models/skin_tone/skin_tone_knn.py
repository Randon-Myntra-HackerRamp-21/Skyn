"""
To classify the input skin into one of the 6 skin tones
"""
import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier
from models.skin_tone.skin_detection import skin_detection

def identify_skin_tone(image_path, dataset):
    mean_color_values = skin_detection(image_path)
    df = pd.read_csv(dataset)
    X = df.iloc[:, [1, 2, 3]].values
    y = df.iloc[:, 0].values

    classifier = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=2)
    classifier.fit(X, y)

    X_test = [mean_color_values]
    y_pred = classifier.predict(X_test)
    return y_pred[0]
