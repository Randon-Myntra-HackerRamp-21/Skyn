import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df2 = pd.read_csv('./models/recommender/final.csv')
makeup = pd.read_csv('./models/recommender/makeup_final.csv')
entries = len(df2)
LABELS = list(df2.label.unique())
# features

features = ['normal', 'dry', 'oily', 'combination', 'acne', 'sensitive', 'fine lines', 'wrinkles', 'redness',
            'dull', 'pore', 'pigmentation', 'blackheads', 'whiteheads', 'blemishes', 'dark circles', 'eye bags', 'dark spots']


# utility functions

def search_concern(target, i):
    if target in df2.iloc[i]['concern']:
        return True
    return False


def name2index(name):
    return df2[df2["name"] == name].index.tolist()[0]


def index2prod(index):
    return df2.iloc[index]


def wrap(info_arr):
    result = {}
#     print(info_arr)
    result['brand'] = info_arr[0]
    result['name'] = info_arr[1]
    result['price'] = info_arr[2]
    result['url'] = info_arr[3]
    result['img'] = info_arr[4]
    result['skin type'] = info_arr[5]
    result['concern'] = str(info_arr[6]).split(',')
    return result

def wrap_makeup(info_arr):
    result = {}
#     print(info_arr)
    result['brand'] = info_arr[0]
    result['name'] = info_arr[1]
    result['price'] = info_arr[2]
    result['url'] = info_arr[3]
    result['img'] = info_arr[4]
    result['skin type'] = info_arr[5]
    result['skin tone'] = info_arr[6]
    return result

one_hot_encodings = np.zeros([entries, len(features)])


#skin types first
for i in range(entries):
    for j in range(5):
        target = features[j]
        sk_type = df2.iloc[i]['skin type']
        if sk_type == 'all':
            one_hot_encodings[i][0:5] = 1
        elif target == sk_type:
            one_hot_encodings[i][j] = 1

#other features
for i in range(entries):
    for j in range(5, len(features)):
        feature = features[j]
        if feature in df2.iloc[i]['concern']:
            one_hot_encodings[i][j] = 1

# recommend top 5 similar items from a category


def recs_cs(vector = None, name = None, label = None, count = 5):
    products = []
    if name:
        idx = name2index(name)
        fv = one_hot_encodings[idx]
    elif vector:
        fv = vector
    cs_values = cosine_similarity(np.array([fv, ]), one_hot_encodings)
    df2['cs'] = cs_values[0]
    
    if label:
        dff = df2[df2['label'] == label]
    else:
        dff = df2
    
    if name:
        dff = dff[dff['name'] != name]
    recommendations = dff.sort_values('cs', ascending=False).head(count)
    #   print(f"Top {count} matching {label} items")
    data = recommendations[['brand', 'name', 'price', 'url','img','skin type','concern']].to_dict('split')['data']
    for element in data:
        products.append(wrap(element))
    return products

    # overall recommendation


def recs_essentials(vector = None, name = None):
#     print("ESSENTIALS:")
    response = {}
    for label in LABELS:
#         print(f"{label}:")
        if name: 
            r = recs_cs(None, name, label)
        elif vector:
            r = recs_cs(vector, None, label)
        response[label] = r
    return response



def makeup_recommendation(skin_tone, skin_type):
    result = []
    dff = pd.DataFrame()
    dff = dff.append(makeup[(makeup['skin tone'] == skin_tone) & (makeup['skin type'] == skin_type) & (makeup['label'] == 'foundation')].head(2))
    dff = dff.append(makeup[(makeup['skin tone'] == skin_tone) & (makeup['skin type'] == skin_type) & (makeup['label'] == 'concealer')].head(2))
    dff = dff.append(makeup[(makeup['skin tone'] == skin_tone) & (makeup['skin type'] == skin_type) & (makeup['label'] == 'primer')].head(2))
    dff= dff.sample(frac = 1)
    data = dff[['brand', 'name', 'price', 'url', 'img', 'skin type', 'skin tone']].to_dict('split')['data']
    for element in data:
        result.append(wrap_makeup(element))
    return result



