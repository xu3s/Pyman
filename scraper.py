from bs4 import BeautifulSoup as bsoup
from dbconnect import connection
import requests as req
import time
import query_module as qm 


def gsource(burl,mangaid):
    header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}
    slink = burl + '/en/detail/' + mangaid
    reql = req.get(slink, headers = header)
    return reql.content

c, conn = connection()

baseurl = "http://localhost:8080"

slink = "https://mangatoon.mobi/en/detail/446/episodes"

header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}
reql = req.get(slink, headers=header)
pres = reql.content
psoup = bsoup(pres, 'html.parser')
# print(psoup)
?!?jedi=0, ?!?               (name=None, attrs={}, recursive=True, text=None, *_***kwargs*_*) ?!?jedi?!?
a1 = psoup.find('div', class_='episodes-wrap')
a2 = a1.find_all('a', class_='episode-item')

b1 = psoup.find('div', class_='detail-top-wrap')
title = b1.find('h1', class_='comics-title').contents[0]





manslug = title.lower().replace(' ','-')

try:
    manid = c.execute('SELECT manga_id FROM manga_detail WHERE manga_slug = %s ') % manslug
except:
    c.execute('INSERT INTO ')
# print(a2)
for ax in a2:
    chaptname = ax.find('div', class_='episode-title').contents[0]
    chaslug = chaptname.lower().replace(' ','-')

    urlink= ax['href']
    # print(ab + ac)
    try:
        xe = "INSERT INTO manga_chapter (manga_id, chapter_link, chapt_title) VALUES (%s,%s,%s)"
        val = (1, urlink, chaptname)
        c.execute(xe,val)
        conn.commit()
        print(chaptname + 'committed!')

    except:
        conn.rollback()
        print('some error occured')

    finally:
        c.close()
        conn.close()
        print('done')


    
    
    # print(chaptname)
# c.close()    
# conn.close()
