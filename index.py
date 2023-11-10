from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/name")
def name():
    a = """
    演員：{'name': '陳宥廷', 'birth': 2001, 'role': '靜宜大學資管四B學生'}
    <br/>
    演員：{'name': '王淨', 'birth': 1998, 'role': '公正黨文宣部黨工'}
    <br/>
    演員：{'name': '黃健瑋', 'birth': 1981, 'role': '公正黨文宣部主任'}
    <br/>
    演員：{'name': '謝盈萱', 'birth': 1979, 'role': '公正黨文宣部副主任兼發言人'}
    <br/>
    演員：{'name': '戴立忍', 'birth': 1966, 'role': '民和黨籍現任立法院院長'}
    """
    return a

