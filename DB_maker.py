import requests
from bs4 import BeautifulSoup as bs


url = 'https://famouspeople.astro-seek.com/filter_death/?umrti_den=nezalezi&umrti_mesic=nezalezi&umrti_rok=&pricina_umrti=&pohlavi=&razeni='
page = requests.get(url)
html = page.text
soup = bs(html, 'lxml')

name_full_list = []
url_full_list = []

name_list = soup.select('td.w300_p5 > a > span > strong')
url_list = soup.select('td.w300_p5 > a')

for name in name_list:
    name_full_list.append(name.text)

for url in url_list:
    url_full_list.append(url.get('href'))

