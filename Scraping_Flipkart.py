from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2&as-pos=0&as-type=RECENT&as-searchtext=ip'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "_1UoZlX"})
# print(len(containers))
# print(soup.prettify(containers[0]))
container = containers[0]

name = container.findAll("div", {"class": "_3SQWE6"})
print(name[0].div.div.div.img["alt"])


