import requests as req
from bs4 import BeautifulSoup as bsoup
import query_module as qm
import dictsample as ds


class gsrc:

    def __init__(self, **kwargs):
        """
         burl is baseurl
        """

        self.srcdata = kwargs

    def get_detail(self, mangaid):

        slink = self.srcdata['burl'] + self.srcdata['dturl'] + mangaid
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}
        r = req.get(slink, headers=header)
        psoup = bsoup(r.content, 'html.parser')

        try:
            srcdata = self.srcdata
            dedata = {}
            err = [None]

            if 'w1' in srcdata:
                attr = srcdata['w1']['attr']
                atrv = srcdata['w1']['atrv']
                atr = srcdata['w1']['atr']

                if atr == 'class_':
                    w1 = psoup.find(attr, class_=atrv)

                elif atr == 'id':
                    w1 = psoup.find(attr, id=atrv)

                else:
                    err.append(
                        'w1 atr is not found please fix the "config.py" or edit "gsource.py"')

            else:
                err.append('w1 is required')

            if 'w2' in srcdata:

                attr = srcdata['w2']['attr']
                atrv = srcdata['w2']['atrv']
                atr = srcdata['w2']['atr']

                if atr == 'class_':
                    w2 = psoup.find(attr, class_=atrv)

                elif atr == 'id':
                    w2 = psoup.find(attr, id=atrv)

                else:
                    err.append(
                        'w2 atr is not found please fix the "config.py" or edit "gsource.py"')

            else:
                err.append('w2 is required')
            if 'tw' in srcdata:

                attr = srcdata['tw']['attr']
                atrv = srcdata['tw']['atrv']
                atr = srcdata['tw']['atr']

                if atr == 'class_':
                    title = w1.find(attr, class_=atrv).contents[0]
                    dedata.update(title=title)

                elif atr == 'id':
                    title = w1.find(attr, id=atrv).contents[0]
                    dedata.update(title=title)
                else:
                    err.append('tw atr is not found please fix it')
            else:
                err.append('tw atr is required')

            if 'arw' in srcdata:

                attr = srcdata['arw']['attr']
                atrv = srcdata['arw']['atrv']
                atr = srcdata['arw']['atr']

                if atr == 'class_':
                    artist = w1.find(attr, class_=atrv).contents[0]
                    dedata.update(artist=artist)

                elif atr == 'id':
                    artist = w1.find(attr, id=atrv).contents[0]
                    dedata.update(artist=artist)
                else:
                    err.append('arw atr is not found please fix it')
            else:
                err.append('arw atr is required')

            if 'desw' in srcdata:

                attr = srcdata['desw']['attr']
                atrv = srcdata['desw']['atrv']
                atr = srcdata['desw']['atr']

                if atr == 'class_':
                    description = w2.find(attr, class_=atrv).contents[0]
                    dedata.update(description=description)

                elif atr == 'id':
                    description = w2.find(attr, id=atrv).contents[0]
                    dedata.update(description=description)
                else:
                    err.append('desw atr is not found please fix it')
            else:
                err.append('desw atr is required')

            if err[0] == None:
                pass
            else:
                raise Exception(err[0])
            # else:
            #    pass
            return dedata
        except Exception as e:
            return e

    def get_ep(self,mangaid):
        #

        srcdata = self.srcdata
        slink = srcdata['burl'] + srcdata['epurl'] + mangaid + srcdata['extraep']
        header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:73.0) Gecko/20100101 Firefox/73.0"}
        r = req.get(slink, headers=header)
        psoup = bsoup(r.content, 'html.parser')

        try:
            epdata = {}
            if 'w3' in srcdata:
                atr = srcdata['w3']['atr']
                attr = srcdata['w3']['attr']
                attrv = srcdata['w3']['attrv']

                if atr == 'class_':
                    w3 = psoup.find(attr, class_=attrv)

                elif atr == 'id':
                    w3 = psoup.find(attr, id=attrv)

                else:
                    raise Exception('error on w3')
            else:
                raise Exception('error w3 not found')

            if 'w4' in srcdata:
                atr = srcdata['w4']['atr']
                attr = srcdata['w4']['attr']
                attrv = srcdata['w4']['attrv']

                if atr == 'class_':
                    w4 = w3.find_all(attr, class_=attrv)

                elif atr == 'id':
                    w4 = w3.find_all(attr, id=attrv)

                else:
                    raise Exception('error on w4')
            else:
                raise Exception('error: w4 not found')

            if 'ets' in srcdata:
                atr = srcdata['ets']['atr']
                attr = srcdata['ets']['attr']
                attrv = srcdata['ets']['attrv']

                if atr == 'class_':
                    ets = (i.find(attr, class_=attrv).contents[0].strip().lstrip() for i in w4)

                elif atr == 'id':
                    ets = (i.find(attr, id=attrv).contents[0].strip().lstrip() for i in w4)

                else:
                    raise Exception('error on ets')
            else:
                raise Exception('error: ets not found')

            if 'els' in srcdata:
                #atr = srcdata['els']['atr']
                #attr = srcdata['els']['attr']
                #attrv = srcdata['els']['attrv']
                try:

                    els = (srcdata['burl'] + i['href'] for i in w4)
                except Exception as e:
                    return e
            else:
                raise Exception('els not found')

            result = [{'eptitle': et, 'eplink': el} for et, el in zip(ets, els)]
            return result
        except Exception as e:
            return e



##########


dsi = ds.dict1

x = gsrc(**dsi)
y = gsrc(**dsi).get_detail('446')
print(x.get_detail(mangaid='446')['title'])

print('artist: '+y['artist'])
print('description: ' + y['description'])

print(x.get_ep('446'))
