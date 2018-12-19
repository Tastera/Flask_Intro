from flask import Flask, render_template
app = Flask(__name__)
import random



@app.route("/") # @는 def 실행하기 전에 선수행되는 것이라고만 일단 알아두세요.
def hello():
    return "<h1>서버가 html도 보내주나?</h1>"
    
@app.route("/html_tag") # 경로 설정
def html_tag():
    return """
    <h1>첫 번째 줄</h1>
    <h2>두 번째 줄</h2>
    <h3>세 번째 줄</h3>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):  #url 코드로 요청받은 name이라는 코드,,
    return render_template("welcome.html", people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    return render_template("calculater.html", num_1=num, result=num**3)
    
@app.route('/lunch')
def lunch():
    menu = ["된장찌개", "두루치기", "닭근위", "김치볶음밥"]
    pick = random.choice(menu)
    return render_template("lunch.html", pick=pick)
    
@app.route('/lotto')
def lotto():
    list = []
    material = random.randint(1, 45)
    for i in range(6):
        while material in list:
            material = random.randint(1, 45)
        list.append(material)
        list.sort()
    return render_template("lotto.html", list=list)
    
@app.route('/naver')
def naver():
    return render_template("naver.html")