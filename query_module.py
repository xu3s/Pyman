from dbconnect import connection


def tuplejoin(data):
    result = ''.join(str(i) for i in data)
    return result


class manquery2:
    '''
    :@param self:
    :@param myParam1:
    :@param myParam2:
    :@return:
    '''

    def __init__(self,**x):
        '''
        self:
        dbname:
        dbdata:
        '''

        c,conn = connection()

        self.c = c
        self.conn = conn
        self.dbname = x["dbname"]
        self.dbdata = x["dbdata"]
        self.mquery = x["mquery"]
        self.thequery = x["thequery"]
            

    def get_id(self):

        comm = 'SELECT ' + self.dbdata + ' FROM ' + self.dbname + ' WHERE ' + self.mquery + ' = %s'
        data = (self.thequery,)
        self.c.execute(comm,data)
        try:
            result = tuplejoin(self.c.fetchone())
        except:
            result = None
        self.c.close()
        return result

    def get_data(self):
        comm = 'SELECT ' + self.dbdata + ' FROM ' + self.dbname + ' WHERE ' + self.mquery + ' = %s'
        data = (self.thequery,)
        self.c.execute(comm,data)
        result = self.c.fetchall()
        self.c.close()
        return result
    
    def __del__(self):
        self.conn.close()

class postq:

    def __init__(self,dname,qname,qval):
        
        c,conn = connection()

        self.c = c
        self.conn = conn
        self.dname = dname
        self.qname = qname
        self.qval = qval

    def postq(self):
        try:
            
            comm = "INSERT INTO " + self.dname + self.qname + "VALUES" + self.qval
            self.c.execute(comm)
            self.conn.commit()
            self.c.close()
            x = 'commited'
            return x
        except Exception as e:
            return e
            
    def __del__(self):
        self.conn.close()


class kampret:


    def __init__(self,**a):
        self.test1 = a["test1"]
        self.test2 = a["test2"]

    def testlist(self):
        #return self.test1
        return self.test2


#listt = "('l1','l2','l3',)"

#a = kampret(test1='test',test2=listt)
#print(a.testlist())

    #def disconnect(self):
    #    self.disconn = conn.close()













# manslug = 'just-tests'
# artname = 'some artist'
# mantit = 'just tests'
# mdesk = 'somme descriptions'
# mtype = 'mytype'
# mstatus = 'finished'
# chalink = '/some/link'
# chatit = 'chapter title'
# chaslug = 'just-slug'

# manga_id = get_id(dbname='manga_detail',
#                     dbdata='id',
#                     mquery='manga_slug',
#                     thequery=manslug)

# mangaid2 = manquery(dbname='manga_detail',
#                     dbdata='id',
#                     mquery='manga_slug',
#                     thequery = manslug)

# dbnamed = 'manga_detail'
# dbdatad = 'id'
# mqueryd = 'manga_slug'


# mangaid3 =  manquery2(dbname=dbnamed,
#                     dbdata=dbdatad,
#                     mquery=mqueryd,
#                     thequery = manslug)


# print(manga_id)
# print(mangaid2.get_id())
# print(mangaid3.get_id())

# c.close()
# conn.close()
