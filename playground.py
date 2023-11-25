from bs4 import BeautifulSoup
import requests

########### One Page #########
# URL = 'https://subslikescript.com/movie/Titanic-120338'
# response = requests.get(URL)
# content = response.text

# soup = BeautifulSoup(content, 'lxml')
# box = soup.find('article', class_='main-article')
# title = box.find('h1').get_text()
# tanscrip = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# with open(f'beautiful-soup/{title}.txt', 'w') as file:
#     file.write(tanscrip)

########### Multiple Pages #########

ROOT = 'https://subslikescript.com/'
URL = f'{ROOT}movies'
response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, 'lxml')

a_tags = soup.select('li.page-item a')
link_page = a_tags[0].attrs.get('href').split('=')[0]
for i in range(1, 101):
    print(f'{link_page}={i}')

titles = soup.select('ul.scripts-list a')
links = []

# for title in titles:
#     links.append(f'{ROOT}{title.attrs.get('href')}')

# for link in links:
#     content = requests.get(link).text
#     soup = BeautifulSoup(content, 'lxml')
#     box = soup.find('article', class_='main-article')
#     title = box.find('h1').get_text()
#     tanscrip = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#     with open(f'movies-scripts/{title}.txt', 'w') as file:
#         file.write(tanscrip)



