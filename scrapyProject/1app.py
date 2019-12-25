from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pymysql
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='19960120', db='scrapymysql', charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * FROM zhaopin"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('index.html',u=u)
if __name__ == '__main__':
    app.run()