# Make sure that you have selenium python and chrome webdriver installed
# Author : Gaurav Bhattacharjee

from pandas.core.arrays import categorical
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

chrome_path = r"C:\Users\chromedriver.exe" # Add your webdriver path
driver = webdriver.Chrome(executable_path = chrome_path)

# Categories
categories = ['face-moisturisers', 'cleanser', 'sunscreen', 'concealer', 'mask-and-peel', 'foundation']


# Specify the number of products from each category
products_from_each_category = 300

# Each page has 50 products
pages = products_from_each_category//50


df = pd.DataFrame(columns=['label', 'url'])

base_url = 'https://www.myntra.com/'
for category in categories:
    i = 1
    while i <= pages:
        try:
            driver.get(f"{base_url}{category}?p={i}")

            # Wait for at most 10 seconds for the products to appear 
            search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "desktopSearchResults")))
            
            # List of divs of all product tiles
            products = search_results.find_elements_by_class_name('product-base')

            dic = {'label':category, 'url':[]}
            temp = []

            # Collect the individual URLs of the first {products_from_each_category} products and put them in the dictionary 
            for product in products:
                product_url = product.find_element_by_tag_name('a').get_attribute('href')
                print(f"{category} : {product_url}")
                temp.append(product_url)
    
            dic['url'] = temp 

            # Append the dictionary to the dataframe, which currently has [label, url] as its columns
            df = df.append(pd.DataFrame(dic), ignore_index = True)
            i += 1
        except:
            print("Failed to load category catalogue, retrying")
            
print(df)

# Set of skin metrics
skin_metrics = set(['brand', 'name', 'price', 'skin type', 'spf', 'concern', 'concern 2', 'concern 3', 'key ingredient', 'formulation'])
df2 = pd.DataFrame(columns=['brand', 'name', 'price', 'skin type', 'spf', 'concern', 'concern 2', 'concern 3', 'key ingredient', 'formulation'])
df = pd.concat([df, df2], axis = 1)

entries = len(df)
print(f"Entries {entries}")

i = 0
for i in range(entries):
    ur = df.url[i]
    try:
        # Head to the web page containing the details of the particular product
        driver.get(ur)

        # Wait for at most 10 seconds specifications table to load
        specifications_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "index-tableContainer")))

        # Obtain the brand, product name and price
        brand_name = driver.find_element_by_class_name("pdp-title").text
        
        product_name = driver.find_element_by_class_name("pdp-name").text
        
        price = driver.find_element_by_class_name("PriceInfo-price").text
        df['brand'][i] = brand_name
        df['name'][i] = product_name
        df['price'][i] = price
        print(f"{brand_name} {product_name} {price}")
        specifications = specifications_table.find_elements_by_class_name("index-row")

        # Loop through the different parameters such as skin type, skin tone, etc and fill in values for them in the dataframe
        for group in specifications:
            parameter = group.find_element_by_class_name("index-rowKey").text
            value = group.find_element_by_class_name("index-rowValue").text
            if parameter.lower() in skin_metrics:
                df[parameter.lower()][i] = value

        print(df.iloc[i]) 
        
    except:
        print("Failed to load data for product")    
        
print(df)

# Export the dataframe as a csv file
df.to_csv('result.csv', encoding = 'utf-8-sig', index = False)



