import requests
from bs4 import BeautifulSoup as bs

'''
# 웹사이트에서 이름, URL 가져오기
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


#for url in url_full_list:
'''
# 세부 사이트로 들어가서 행성 정보 받아오기
url2 = 'https://birthcharts.astro-seek.com/birth-chart/bela-lugosi-horoscope'
horoscope = requests.get(url2)
html = horoscope.text
soup = bs(html, 'lxml')

data = [] #name, birthdate, death, cause, occupation, sun, moon, mercury, venus, mars, jupiter, saturn
name = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > h2')[0].text
birthdate = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(2) > div:nth-of-type(5)')[0].text.strip().replace("\n", '')
death = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(7) > div:nth-of-type(2) > a')[0].text
cause = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(7) > div:nth-of-type(2) > span > a')[0].text
occupation = soup.select('body > div.main-nad-envelope > div.main-envelope > div.main-web > div.stredni-menu > div.obsah > div.obsah-uvod > div.obsah-vnitrek > div.detail-info > div:nth-of-type(11) > div:nth-of-type(2)')[0].text.strip()




#행성별 숫자 가져오기 : 행성에 따라 확인할 필요 있음

sun_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(5) > span')[2].text
sun_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(5) > span')[3].text

moon_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(11) > span:nth-of-type(1)')[0].text
moon_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(11) > span:nth-of-type(2)')[0].text

merc_degree1 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(17) > span')[2].text
merc_degree2 = soup.select('div.right-sedy-banner-svetlejsi > div > div:nth-of-type(17) > span')[3].text



'''
ven_degree1 =
ven_degree2 =

mars_degree1 =
mars_degree2 =

jup_degree1 =
jup_degree2 =

sat_degree1 =
sat_degree2 =

#문자열 수정 및 숫자로 변환
sun = float((sun_degree1 + '.' + sun_degree2).replace("’",""))
moon = float((moon_degree1 + '.' + moon_degree2).replace("’",""))
merc = float((merc_degree1 + '.' + merc_degree2).replace("’",""))
'''
