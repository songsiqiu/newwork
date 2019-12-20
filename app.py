from flask import Flask,request,url_for,render_template,redirect
import pymysql
conn =pymysql.connect('127.0.0.1','root','123456','market',charset='utf8')

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/',methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/',methods=['POST'])
def logincheck():
    username = request.form["username"]
    password = request.form["password"]
    cur = conn.cursor()
    sql = "select * from count where username = '%s' and password='%s'" % (username, password)
    cur.execute(sql)
    user = cur.fetchone()
    print(user)
    if user:
        return redirect(url_for('maingoods'))
    else:
        return render_template('login.html')


@app.route('/maingoods')
def maingoods():
    cur =conn.cursor()
    sql = "select wares,RMB,sums from goods"
    cur.execute(sql)
    result = cur.fetchall()
    listgoods = []
    for item in result:
        dicfruit = {}
        dicfruit['id'] = item[0]
        dicfruit['wares'] = item[1]
        dicfruit["RMB"] = item[2]
        dicfruit["sums"] = item[3]
        listgoods.append(dicfruit)
    if listgoods:
        return render_template('index.html',listgoods=listgoods)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()