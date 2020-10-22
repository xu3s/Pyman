import requests as req
from bs4 import BeautifulSoup as bsoup
import query_module as qm


class gsrc:

    def __init__(self, burl, mangaid, header={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}):
        self.burl = burl
        self.mangaid = mangaid
        self.header = header

    def get_detail(self):

        slink = self.burl + "/en/detail/" + self.mangaid
        r = req.get(slink, headers=self.header)
        psoup = bsoup(r.content, 'html.parser')
        a1 = psoup.find("div", class_='detail-top')
        a2 = psoup.find("div", class_='selected-detail')

        title = a1.find('h1', class_='comics-title').contents[0]
        artist = a1.find('div', class_='created-by').contents[0]
        description = a2.find('div', class_='description').contents[0]

        ret = {'title': title, 'artist': artist, 'description': description}
        return ret

    def get_ep(a):
        slink = a.burl + "/en/detail/" + a.mangaid + "/episodes"
        r = req.get(slink, headers=a.header)
        psoup = bsoup(r.content, 'html.parser')
        a1 = psoup.find("div", class_='selected-episodes')
        a2 = a1.find_all('a', class_='episode-item')

        ets = (i.find('div',
                      class_='episode-title').contents[0].strip().lstrip() for i in a2)
        els = (a.burl + i['href'] for i in a2)

        result = [{'eptitle': et, 'eplink': el} for et, el in zip(ets, els)]

        return result


class gtest:

    def __init__(a, **acnf):

        if 'a1' in acnf:
            a1 = acnf['a1']
            a.a1 = a1

    def a1(a):
        return a.a1


a1a = 'this a1'
print(gtest(a1=a1a).a1())


a = gsrc("http://localhost:8080", "446")


qval = a.get_detail()['artist']
qval2 = "('", a.get_detail()['artist'], "')"
x = qm.manquery2(dbname='artist_data',
                 dbdata='ar_id',
                 mquery='artistName',
                 thequery=qval)
arid = x.get_id()
b = qm.postq('artist_data', '(artistName)', qval2)

title = a.get_detail()['title']

print(title, arid)

y = qm.manquery2(dbname='artist_data',
                 dbdata='artistName',
                 mquery='ar_id',
                 thequery=arid)
print(y.get_id())

b = a.get_detail()
print(b['title'], b['description'].lstrip())
#c = a.get_ep()
# print(c)
print(a.get_ep2())
