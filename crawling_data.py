import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

info = []
for n_page in range(1, 101):
    page = 'https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48/Page-{}?Tid=7709'.format(n_page)
    result = requests.get(page)
    source = result.text
    soup = BeautifulSoup(source, 'html.parser')

    for i in range (len(soup.find_all('div', class_='item-container'))):
        # if(len(soup.find_all('ul', class_='item-features'))==6):
        id = soup.find_all('div', class_='item-container')[i].attrs['id']
        title = soup.find_all('a', class_='item-title')[i].text
        try:
            brand = soup.find_all('a', class_='item-brand')[i].find_all('img')[0].attrs['title']
        except:
            brand = ''
        if(len(soup.find_all('div', class_='item-branding')[i]) == 2):
            rating = soup.find_all('div', class_='item-branding')[i].find_all('a', class_='item-rating')[0].attrs['title'].split()[-1]
            n_rating = soup.find_all('div', class_='item-branding')[i].text.replace('(','').replace(')','')
        else:
            rating = ''
            n_rating = ''
        try:
            price = float((list(soup.find_all('li', class_='price-current')[i].stripped_strings)[1]+list(soup.find_all('li', class_='price-current')[i].stripped_strings)[2]).replace(',',''))
        except:
            price = ''
        shipping = soup.find_all('li', class_='price-ship')[i].text
        img_url = soup.find_all('a', class_='item-img')[i].img.attrs['src']
        try:
            max_rslt = re.findall('(\d+ x \d+)',soup.find_all('ul', class_='item-features')[i].text)[0]
        except:
            max_rslt = ''
        try:
            dp = re.findall('DisplayPort: (\d+ x \S+ \d+.\d+\S)',soup.find_all('ul', class_='item-features')[i].text)[0]
        except:
            dp = ''
        try:
            hdmi = re.findall('HDMI: (\d+ x \S+ \d+.\d+)',soup.find_all('ul', class_='item-features')[i].text)[0]
        except:
            hdmi = ''
        try:
            dirx = re.findall('DirectX: (\S+ \d+)',soup.find_all('ul', class_='item-features')[i].text)[0]
        except:
            dirx = ''
        try:
            model = re.findall('Model #: (\S+)',soup.find_all('ul', class_='item-features')[i].text)[0]
        except:
            model = ''
        print('Trang {} - san pham {}'.format(n_page, i))
        info_row = dict(
            item_id=id,
            title=title,
            brand=brand,
            rating=rating,
            n_rating=n_rating,
            price=price,
            shipping=shipping,
            img_url=img_url,
            max_rslt=max_rslt,
            dp=dp,
            hdmi=hdmi,
            dirx=dirx,
            model=model,
        )
        info.append(info_row)

print(len(info))
df = pd.DataFrame(info)
df.to_csv('info.csv', index=False)