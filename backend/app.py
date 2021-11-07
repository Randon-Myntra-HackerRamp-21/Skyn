import os
from typing import List
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from models.skin_tone.skin_tone_knn import identify_skin_tone
from flask import Flask, request 
from flask_restful import Api, Resource, reqparse, abort
import werkzeug
from models.recommender.rec import recs_essentials, makeup_recommendation
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
api = Api(app)

class_names1 = ['Dry_skin','Normal_skin','Oil_skin']
class_names2 = ['Low','Moderate','Severe']
skin_tone_dataset = 'models/skin_tone/skin_tone_dataset.csv'
def get_model():
    global model1, model2
    model1 = load_model('./models/skin_model')
    print('Model 1 loaded')
    model2 = load_model('./models/acne_model')
    print("Model 2 loaded!")

def load_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]
    return img_tensor

def prediction_skin(img_path):
    new_image = load_image(img_path)
    pred1 = model1.predict(new_image)
    # print(pred1)
    if len(pred1[0]) > 1:
        pred_class1 = class_names1[tf.argmax(pred1[0])]
    else:
        pred_class1 = class_names1[int(tf.round(pred1[0]))]
    return pred_class1

def prediction_acne(img_path):
    new_image = load_image(img_path)
    pred2 = model2.predict(new_image)
    # print(pred2)
    if len(pred2[0]) > 1:
        pred_class2 = class_names2[tf.argmax(pred2[0])]
    else:
        pred_class2 = class_names2[int(tf.round(pred2[0]))]
    return pred_class2

get_model()













img_put_args = reqparse.RequestParser()
img_put_args.add_argument("file", help="Please provide a valid image file", required = True)


rec_args = reqparse.RequestParser()

rec_args.add_argument("tone", type=int, help="Argument required", required=True)
rec_args.add_argument("type", type=str, help="Argument required", required=True)
rec_args.add_argument("features", type=dict, help="Argument required", required=True)




class Recommendation(Resource):
    def put(self):
        args = rec_args.parse_args()
        print(args)
        features = args['features']
        tone = args['tone']
        skin_type = args['type'].lower()
        skin_tone = 'light to medium'
        if tone <= 2:
            skin_tone = 'fair to light'
        elif tone >= 4:
            skin_tone = 'medium to dark'
        print(f"{skin_tone}, {skin_type}")
        fv = []
        for key, value in features.items():
            # if key == 'skin type':
            #     skin_type = key
            # elif key == 'skin tone':
            #     skin_tone = key
            #     continue
            fv.append(int(value))

        general = recs_essentials(fv, None)
       
        makeup = makeup_recommendation(skin_tone, skin_type)
        return {'general':general, 'makeup':makeup}
        
        
       




class SkinMetrics(Resource):
    def put(self):
        args = img_put_args.parse_args()
        print(args)
        file = args['file']
        starter = file.find(',')
        image_data = file[starter+1:]
        image_data = bytes(image_data, encoding="ascii")
        im = Image.open(BytesIO(base64.b64decode(image_data)))
        
        filename = 'image.png'
        file_path = os.path.join('./static',filename)                       
        im.save(file_path)
        skin_type = prediction_skin(file_path)
        acne_type = prediction_acne(file_path)
        tone = identify_skin_tone(file_path, dataset=skin_tone_dataset)
        print(skin_type)
        print(acne_type)
        print(tone)
       

        return {'type':skin_type, 'tone':tone, 'acne':acne_type}, 200

        


api.add_resource(SkinMetrics, "/upload")
api.add_resource(Recommendation, "/recommend")


# @app.route("/", methods=['GET', 'POST'])
# def home():
#     return render_template('home.html')

# @app.route("/predict", methods = ['GET','POST'])
# def predict():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = file.filename
#         file_path = os.path.join('./static',filename)                       #slashes should be handeled properly
#         file.save(file_path)
#         skin_type = prediction_skin(file_path)
#         acne_type = prediction_acne(file_path)
#         print(skin_type)
#         print(acne_type)
#         return skin_type, acne_type

if __name__ == "__main__":
    app.run(debug = False)
