<<<<<<< HEAD
Test
=======
import MySQLdb
import config

host = config.mysql["host"]
user = config.mysql["user"]
passwd = config.mysql["passwd"]
db = config.mysql["db"]
"""
connect to MySQLdb


"""

def connection():
    conn = MySQLdb.connect(host = host,
                           user = user,
                           passwd = passwd,
                           db = db)
    c = conn.cursor()

    return c, conn
>>>>>>> aaffeff... shhh
