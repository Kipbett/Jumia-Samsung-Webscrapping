# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 07:57:52 2023

@author: Wolf
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = 'https://www.jumia.co.ke/mlp-samsung-shop/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product items on the page
product_items = soup.find_all('article', {'class': 'prd _fb col c-prd'})

product_names = []
product_discount = []
product_prices = []

# Loop through each product item and extract the seller name
for item in product_items:
    product_name = item.find('h3', {'class': 'name'}).text.strip()
    product_names.append(product_name)
    prod_disc = item.find('div', {'class': 'bdg _dsct _sm'}).text.strip()
    product_discount.append(prod_disc)
    product_price = item.find('div', {'class': 'prc'}).text.strip()
    product_prices.append(product_price)
    print(product_name, " ", product_price, " ", prod_disc)
    
df = pd.DataFrame({'Product': product_names, 'Discount': product_discount, "Price": product_prices})

df.to_excel("JumiaSamsung2.xlsx", index=False)