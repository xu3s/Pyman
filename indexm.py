from dbconnect import connection

def indexm():
    try:
        c, conn = connection()
        return "all good"
    except Exception as e:
        return(str(e))