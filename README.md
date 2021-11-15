
# Team Name : Randon
**Project Name** : CV-skin-care-recommendation

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

This is the initial page, the user is prompted to take a selfie. Once the user grants permission to use their device's camera, a realtime video of their camera (profile : user) runs in 4:3 aspect ratio.

`/form` - [Form](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/frontend/src/views/Form.jsx) 

`/recs` - [Recommendations](https://github.com/Randon-Myntra-HackerRamp-21/CV-skin-care-recommendation/blob/main/frontend/src/views/Recommendations.jsx) 

### Backend Routes

`/upload`

`/recommend`

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

### Recommendation System

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
