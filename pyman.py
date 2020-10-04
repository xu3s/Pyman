from flask import Flask, render_template,request, redirect, request, url_for, flash, g, Blueprint

from markupsafe import escape
from datetime import datetime
from dbconnect import connection


app = Flask(__name__)
bp = Blueprint('blog', __name__)



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     try:
#         c, conn = connection()
#         return "all good"
#     except Exception as e:
#         return(str(e))

@app.route('/', methods=['GET', 'POST'])
def index():
    from indexm import indexm
    return indexm()

#@app.route('/list', methods=['GET', 'POST'])
#def lists():

   # c,conn = connection()
   # c.execute('SELECT m_chapter, manga_url '
   # ' FROM manga_chapter' 
    #' WHERE manga_id=1'
   # )
   # posts = c.fetchall()
    # conn.close()
    
  
 

   # return render_template('blog/index.html', posts=posts)

@app.route('/test/<value1>', methods=['GET', 'POST'])
def test(value1):
    value1 = value1
    
    return render_template('blog/index.html', posts= 'value1 : %s ' % value1) 




if __name__ == '__main__':
    app.run(debug=True)
