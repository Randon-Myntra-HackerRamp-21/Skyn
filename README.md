


# Team Name : Randon
**Project Name** : Skyn 

**Chosen Theme** : Beautify

**Myntra HackerRamp: Campus Edition 2021**


## Tagline
A virtual **skincare advisor** that uses **Machine Learning** to analyse user's selfie and offer personalised products **recommendation** based on the skin metrics inferred.

## Team Members
[Sri Sylamsh Amrutakavi](https://github.com/Sylamsh) 

[Gaurav Bhattacharjee](https://github.com/guilefoylegaurav)

[Prachurya Nath](https://github.com/prachuryanath)

[Mondeep Prakash](https://github.com/legitmxn)

## Problem Statement
How can we provide seamless and personalised skincare shopping experience on an e-commerce platform?

Most customers are aware of the time consuming in-store experience, accumulated with **uncertainty** of which products suit their skin, chatting with busy store assistants to get more details on products or deals or trying multiple products before buying one.

Everyone's skin is different. Even though the structure of everyone's skin is similar, specific skin metrics - such as skin tone/type, wrinkles, acne severity and so forth - vary largely from person to person. If a moisturiser ‘works’ for someone, it might not for someone else. Also, the use of inappropriate skincare products can exacerbate skin conditions in the worst case.  

**To summarize, before the user shops for skincare products, they need to know their skin, and based on that, purchase products that are appropriate.**

## Our solution
Our solution is a virtual skincare advisor that uses Machine Learning to analyse user's selfie and offer personalised products recommendation based on the skin metrics inferred.

The solution is a two step process, inferring the data required from the user for recommendation, and the recommendation system itself. Data required from the user are skin metrics like

-   skin type (oily, dry, sensitive, combination)
    
-   skin tone
    
-   acne, wrinkles, and other concerns
    
**Workflow:** The image will be taken with precautions such as proper luminance and that the majority of the image is populated by the user’s face. Then, skin metrics are extracted from the image provided by the user, using multiple ML and DL models. With those data points, the recommendation system will provide us the skin products that is most efficient to those skin data in the order of relevance.

## Web Application

### Frontend Routes

`/` - [ImageInput](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/frontend/src/views/imageInput.jsx) 

This is the initial page, the user is prompted to take a selfie. Once the user grants permission to use their device's camera, a realtime video of their camera (profile : user) runs in 4:3 aspect ratio. To ensure that the image is taken with precautions such as _only one face is there in the image_, _proper luminance_ and that the _majority of the image is populated by the user’s face_, **Face recogniton** was implemented using [face-api.js](https://github.com/justadudewhohacks/face-api.js/). The user is given text prompts as directions. When the user takes a selfie, is then redirected to `/form`.  

`/form` - [Form](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/frontend/src/views/Form.jsx) 

The results of the skin metrics inferred from the user's selfie are presented as prefilled form elements. User can alter these values, along with selecting their other skin concerns from the given list. Once the form is submitted, the page is redirected to `/recs`.

`/recs` - [Recommendations](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/frontend/src/views/Recommendations.jsx) 

Here the recommended products are presented in the form of cards, with their details. The cards when clicked redirect to their appropriate product page.

### Backend Routes
**[PUT]**`/upload`

Accepts a base64 image, converts it into png and feeds that into the pipeline yielding predictions for skin tone, type and acne, and returns these attributes in JSON format. 


**[PUT]**`/recommend`

Accepts request body containing details about the user's skin type, tone, and concerns, and returns top 5 recommended skincare products from each category in JSON format. 

## Models

### Skin Tone
Obtaining skin tone consists of :
- Detecting and extracting skin pixels
- Classifying those color values into the appropriate skin tone class

[This paper](http://www.eleco.org.tr/openconf_2017/modules/request.php?module=oc_proceedings&action=view.php&id=248&file=1/248.pdf&a=Accept+as+Lecture) was followed in extracting the skin pixels. [Skin detection](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/ML/Skin_metrics/Skin_tone/skin_detection.py) has three major steps i.e.., **initial segmentation, prediction of skin pixels and k-means clustering**. 
Initial segmentation is applied with the threshold value &#8594; average of [T<sub>OTSU</sub>](https://learnopencv.com/otsu-thresholding-with-opencv/) and T<sub>MAX</sub>. These values are aquired from the image histogram of the grayscale image

![Image Histogram](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/images/skin_tone/image_histogram.png)

The thresholded image is then converted to, **HSV** and **YCrCb** color spaces. These colorspaces are less sensitive to light conditions. Potential skin color pixels are selected with : 
`(Hue <= 170) and (140 <= Cr <= 170) and (90 <= Cb <= 120)`.
A binary image is formed with the selected pixels. 

We defined special dataset made of input features in order to cluster pixels on an image. This dataset contains some components of two color spaces _(Hue, Cr, Cb)_, positions of pixels on the image _(Xp, Yp)_ and  rough estimation of skin pixels _(I)_. Since all information is contained in a dataframe, we converted all six aforementioned components _**(Cr, Cb, Hue, Xp, Yp and I)**_ into appropriate vectors.

Image pixels are clustered into three clusters: **background, foreground and skin pixels**. We used square Euclidean measure as a distance. Aproximated skin pixels _(I)_, determine which cluster represents skin.

![Skin_detection](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/images/skin_tone/skintone_images_fs.png)

The mean color values obtained from the cluster are then used for classifying the tone into [Fitzpatrick scale](https://en.wikipedia.org/wiki/Fitzpatrick_scale) using a **KNN model**. The model was trained using the [color values dataset](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/ML/Skin_metrics/Skin_tone/public/skin_tone_dataset.csv) gotten from the [image dataset](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/tree/main/ML/Skin_metrics/Skin_tone/public/skin%20tone%20values) of [Von Luschan's chromatic scale](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/ML/Skin_metrics/Skin_tone/public/test%20images/Felix_von_Luschan_Skin_Color_chart.svg.png).

### Skin Type

### Acne

### Recommender System
Given the user's skin metrics and concerns, how do we fetch **relevant** skincare products that shall possibly address his/her skin concerns?

Since the dataset that has been used contains data straight from the **Myntra Beauty Section** itself, each product in the dataset is associated with skin tone and one/more skin concerns (acne, blemishes, redness, etc). 

A good strategy would be to fetch those products whose product attributes (skin tone + concerns) is **similar** to the user's skin metrics and concerns. Mathematically, this similarity can be quantified in the form of **cosine similarity** between product feature vector and user skin attribute vector.
![enter image description here](https://neo4j.com/docs/graph-data-science/current/_images/cosine-similarity.png)

**The key idea is:** To find **relevant** skincare products from a particular category, given the user's skin features, we simply obtain the top **n**  values of **similarity(skin vector, product vector)** for the products in dataset belonging to that said category, and return the products corresponding to those values. 
 

## How to run 
Clone this repo, head to the root directory and create a [virtual env](https://www.geeksforgeeks.org/python-virtual-environment/).
`$ pip install -r requirements.txt`

Then, 

    $ cd backend
    $ python app.py

After that, 

    $ cd frontend
    $ npm install
    $ npm start

The web app can be accessed at [localhost:3000](http://localhost:3000)
    

## Tech Stack 
**Frontend** : React

**Backend** : Flask, OpenCV, Tensorflow
