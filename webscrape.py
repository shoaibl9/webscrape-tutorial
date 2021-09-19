#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:52:27 2021

@author: shoaiblaghari
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=graphics+card"

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

# making the csv
filename = "products.csv"
f = open(filename, "w")

headers = "product_name, price\n"

f.write(headers)

# loop through each product
for container in containers:
    title_container = container.find("a", {"class": "item-title"})    
    price_container = container.find("li", {"class": "price-current"})
        
    if hasattr(title_container, "text") & hasattr(price_container, "text"):
        product_name = title_container.text
        print("name: " + product_name)
        
        price = price_container.text
        print("price: " + price)
        
        f.write(product_name.replace(",", "|") + "," + price.replace(",", "") + "\n")

    print()
    
f.close()
    