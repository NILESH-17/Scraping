from bs4 import BeautifulSoup
import requests
import pandas as pd

books_data = []
for i in range(1,6):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    ol = soup.find('ol')
    articles = ol.find_all('article',class_='product_pod')
    
    for article in articles:
        image  = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p',class_ = 'price_color').text
        price = float(price[1:])
        books_data.append([title,star,price])

df = pd.DataFrame(books_data, columns=['Title','Rating','Price'])
df.to_csv('C:/Users/user/Desktop/books.csv')