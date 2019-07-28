import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DSamsung&otracker=nmenu_sub_TVs+%26+Appliances_0_Samsung&page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        print("Total Data Collected : ", len(soup.findAll('a', {'class': '_31qSD5'})))
        for link in soup.findAll('a', {'class': '_31qSD5'}):
            href = 'https://www.flipkart.com'+link.get('href')
            title = link.findAll('div', {'class': '_3wU53n'})
            print(href)
            print(title)
            get_item_data(href)
        page += 1


def get_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for item_name in soup.findAll('span', {'class': '_35KyD6'}):
        print(item_name.text)

trade_spider(1)

