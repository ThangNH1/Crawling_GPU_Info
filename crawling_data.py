import pandas as pd
from bs4 import BeautifulSoup
import requests

info = []
for n_page in range(1, 101):
    page = 'https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-{}?Tid=7709'.format(n_page)
    result = requests.get(page)
    source = result.text
    soup = BeautifulSoup(source, 'html.parser')

    for i in range (len(soup.find_all('div', class_='item-container'))):
        title = soup.find_all('a', class_='item-title')[i].text
        try:
            brand = soup.find_all('a', class_='item-brand')[i].find_all('img')[0].attrs['title']
        except:
            brand = ''
        if(len(soup.find_all('div', class_='item-branding')[i]) == 2):
            rating = soup.find_all('div', class_='item-branding')[i].find_all('a', class_='item-rating')[0].attrs['title'].split()[-1]
        else:
            rating = ''
        try:
            price = float((list(soup.find_all('li', class_='price-current')[i].stripped_strings)[1]+list(soup.find_all('li', class_='price-current')[i].stripped_strings)[2]).replace(',',''))
        except:
            price = ''
        shipping = soup.find_all('li', class_='price-ship')[i].text
        img_url = soup.find_all('a', class_='item-img')[i].img.attrs['src']
        print('Trang {} - san pham {}'.format(n_page, i))
        info_row = dict(
            title=title,
            brand=brand,
            rating=rating,
            price=price,
            shipping=shipping,
            img_url=img_url
        )
        info.append(info_row)

print(len(info))
df = pd.DataFrame(info)
df.to_csv('info.csv', index=False)