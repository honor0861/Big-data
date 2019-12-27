# 파일명 : flask01.py

from flask import Flask, render_template, request, redirect # 모듈 가져오기
# 폴더명이 templates인 경우에만 적용됨

import cx_Oracle as oci 
# pip install cx_oracle (cx_Oracle 패키지 모듈들은 Import, Anaconda Prompt에서 설치)

# 아이디/암호@ 서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
# Oracle 서버와 연결
cursor = conn.cursor() 
# cursor 객체 얻어오기

app = Flask(__name__)

@app.route("/")
def index():
    # SQL문 실행
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql) # SQL 문장을 DB 서버에 보냄
    data = cursor.fetchall() # [(   ),(   ),(   )] : Fetch all the rows
    return render_template('list.html', list = data) # list는 임시변수
    # Flask는 templates 폴더에서 'list.html'이라는 파일을 찾음

@app.route("/join", methods=['GET']) # 화면 페이지를 만드는 방법
def join():
    return render_template('join.html')

@app.route("/join", methods=['POST'])
def join_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    # print("{}:{}:{}:{}".format(a,b,c,d))
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"
    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()

    # 오라클 DB 접속
    # 추가하는 SQL문 작성 => Insert, Select, Update, Delete
    # SQL문 수행

    return redirect('/') # 127.0.0.1:5000/
    #127.0.0.1/          # 크롬에서 입력한 것처럼 동작

@app.route("/login", methods=['GET']) # GET은 가져오는 것
def login():
    return render_template('login.html')

@app.route("/login", methods=['POST']) # POST는 수행하는 것
def login_post():
    print("login-post")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) # 소스가 바뀔 때마다 재구동
    # 해당 모듈이 주 프로그램이라는 소리, 해당 모듈을 실행시키지 않고 
    # import 했을 때 모듈 이름이 __name__으로 들어가게 됨