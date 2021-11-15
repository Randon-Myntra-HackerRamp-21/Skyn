"""
To classify the input skin into one of the 6 skin tones
"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def skin_tone(mean_values):
    # df = pd.read_csv("public\pre-processing\skin_tone_dataset_RGB.csv")
    df = pd.read_csv("public\skin_tone_dataset.csv")
    y = mean_values
    df['cs'] = [cosine_similarity([X], [y])[0][0]
                for X in df.iloc[:, [1, 2, 3]].values]
    skin_tone = df.sort_values(by=['cs'], ascending=False).iloc[0]['Type']
    return skin_tone
