
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
