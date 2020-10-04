from bs4 import BeautifulSoup as bsoup
import requests as req


slink = "https://mangatoon.mobi/en/detail/446/episodes"

header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}
reql = req.get(slink, headers=header)
pres = reql.content
psoup = bsoup(pres, 'html.parser')
# print(psoup)

a1 = psoup.find('div', class_='episodes-wrap')
a2 = a1.find_all('a', class_='episode-item')
b1 = psoup.find('div', class_='detail-top-wrap')

title = b1.find('h1', class_='comics-title').contents[0]
chaslug = title.lower().replace(' ','-')




# print(a2)
# for ax in a2:
#     ab = ax.find('div', class_='episode-title').contents[0]
#     ac = ax['href']
#     print(ab + ac)








# from dbconnect import connection

# try:
#     c, conn = connection()
#     print("all good")
# except Exception as e:
#     print(e)

# c,conn = connection()
# c.execute('SELECT m_chapter, manga_url FROM manga_chapter WHERE manga_id=1')
# posts = c.fetchall()
# conn.close()
# for x in posts:
#     print(x)

# import urllib.request
# 
# try:
#     with urllib.request.urlopen(slink) as response:

#         html = response.read().decode('utf-8')#use whatever encoding as per the webpage

#         print(html)
# except urllib.request.HTTPError as e:
#     if e.code==404:
#         print(f"{slink} is not found")
#     elif e.code==503:
#         print(f'{slink} base webservices are not available')
#         ## can add authentication here 
#     else:
#         print('http error',e)