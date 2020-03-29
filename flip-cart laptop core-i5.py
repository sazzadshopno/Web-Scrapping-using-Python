import requests
from bs4 import BeautifulSoup
import pandas as pd

products, prices, ratings = [], [], []

url = 'https://www.flipkart.com/search?sid=6bo%2Cb5g&otracker=CLP_Filters&p%5B%5D=facets.processor%255B%255D%3DCore%2Bi5&page={}'

for page in range(1, 15):
    res = requests.get(url.format(page))
    soup = BeautifulSoup(res.text, features='lxml')
    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'}).get_text()
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'}).get_text()
        products.append(name)
        prices.append(price[1:])

dataframe = pd.DataFrame({'Product Name': products, 'Price': prices})
dataframe.to_csv('products.csv', index=False, encoding='utf-8')