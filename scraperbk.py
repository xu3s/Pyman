from bs4 import BeautifulSoup as bsoup
from dbconnect import connection
import requests as req
from wtforms import form, StringField

# from datetime import datetime as dt
c, conn = connection()

def scraper():



# def get_timestamp():
#     return dt.now().strftime(("%Y-%m-%d %H:%M:%S"))




slink = "https://astrallibrary.net/manga/against-the-gods/"
header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}
reql = req.get(slink, headers=header)
pres = reql.content
psoup = bsoup(pres, 'html.parser')

content = psoup.find('div', class_='page-content-listing')
scontent = content.find_all('li', class_='wp-manga-chapter')


for a in scontent:
    urlink = a.find('a')['href']
    chaptname = a.find('a').contents[0]
    
 
    

    xe = "INSERT INTO manga_chapter (manga_id, m_chapter, manga_url) VALUES (%s,%s,%s)"
    val = ("1", chaptname, urlink)
    c.execute(xe,val)
    conn.commit()

    
    
    # print(chaptname)
c.close()    
conn.close()