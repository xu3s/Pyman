import requests as req
from bs4 import BeautifulSoup as bsoup
import query_module as qm


class gsrc:
    
    def __init__(a,burl,mangaid,header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}):
        a.burl = burl
        a.mangaid = mangaid
        a.header = header

    def get_detail(a):

        slink = a.burl + "/en/detail/" + a.mangaid 
        r = req.get(slink, headers = a.header)
        psoup = bsoup(r.content, 'html.parser')
        a1 = psoup.find("div", class_= 'detail-top')
        a2 = psoup.find("div", class_='selected-detail')

        title = a1.find('h1', class_= 'comics-title').contents[0]
        artist = a1.find('div', class_= 'created-by').contents[0]
        description = a2.find('div', class_='description').contents[0]

        ret = {'title' : title, 'artist' : artist, 'description' : description}
        return ret

    def get_ep(a):
        slink = a.burl + "/en/detail/" + a.mangaid + "/episodes"
        r = req.get(slink, headers = a.header)
        psoup = bsoup(r.content, 'html.parser')
        a1 = psoup.find("div", class_='selected-episodes')
        a2 = a1.find_all('a', class_= 'episode-item')

        ets = (i.find('div',
            class_= 'episode-title').contents[0].strip().lstrip() for i in a2)
        els = (a.burl + i['href'] for i in a2)

        
        result = [{'eptitle': et,'eplink': el} for et,el in zip(ets,els)]
        
        return result


a = gsrc("http://localhost:8080","446")

try:
    qval = a.get_detail()['artist']
    qval2 = "('" + a.get_detail()['artist'] + "')"
    x = qm.manquery2(dbname='artist_data',
            dbdata='ar_id',
            mquery='artistName',
            thequery=qval)
    
    b = qm.postq('artist_data','(artistName)',qval2)
    
    if x.get_id() == None:
        print(b.postq())

    else:
        print(qval + qval2)
        print("already exist")
except Exception as e:
    print(e)

   


#b = a.get_detail()
#print(b['title'])
#c = a.get_ep()
#print(c)

