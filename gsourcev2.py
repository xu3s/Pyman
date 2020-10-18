import requests as req
from bs4 import BeautifulSoup as bsoup
import query_module as qm

class gsrc:

    def __init__(self,**kwargs):
        
        self.baseurl = kwargs['burl']
        self.srcdata = kwargs

    def get_detail(self):

        
        try:
            err = []
            
            if 'a1' in self.srcdata:
                attr = self.srcdata['a1']['attr']
                atrv = self.srcdata['a1']['atrv']

                if self.srcdat == 'class_':
                    a1 = psoup.find(attr, class_=atrv)

                elif self.srcdata['a1']
                a1 = self.srcdata['a1']
                
            else:
                err.append('a1 is required')
                #raise Exception(err[0])
            if 'a2' in self.srcdata:
                a2 = self.srcdata['a2']
                
            else:
                err.append('a2 is required')

            if err == None:
                pass
            else:
                raise Exception(err[0])
            #else:
            #    pass
            return a1 + a2
        except Exception as e:
            return e

a = gsrc(a1 = 'just test')
print(a.get_detail())

