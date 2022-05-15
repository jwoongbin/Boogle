from webbrowser import get
from flask import *
import requests
import json
from models import db
import os
from models import Fcuser

app = Flask('mars_discovery')

@app.route('/')
@app.route('/main')
def main():
    books = []
    # if 'book' in request.args:
    #     search_word = request.args.get('book')
    #     response = requests.get("http://gutendex.com/books/?search="+search_word)
    #     data = json.loads(response.content)
    #     books = data['results']
    #     return render_template('results.html', books=books)
    # else:
    #     topic = 'children'
    #     response = request.get("http://gutendex.com/books/?topic="+topic)
    #     data = json.loads(response.content)
    #     books = data['results']
    #     return render_template('main.html', books=books)
    topic = 'buddhism'
    response = requests.get("http://gutendex.com/books/?topic="+topic)
    data = json.loads(response.content)
    books = data['results']
    
    author = 'nietzsche'
    response = requests.get("http://gutendex.com/books/?search="+author)
    data = json.loads(response.content)
    books2 = []
    books2 = data['results']
    
    sort = 'popular'
    response = requests.get("https://gutendex.com/books/?sort="+sort)
    data = json.loads(response.content)
    books3 = []
    books3 = data['results']    
    
    return render_template('main.html', books=books, books2=books2, books3=books3)
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        #회원정보 생성
        userid = request.form.get('userid') 
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        author = request.form.get('author')
        user_genre = request.form.get('user_genre')
        print(user_genre)
        
        if not (userid and username and password and re_password  and user_genre) :
            return "모두 입력해주세요"
        elif password != re_password:
            return "비밀번호를 확인해주세요"
        else:
            fcuser = Fcuser()         
            fcuser.password = password #models의 FCuser 클래스를 이용해 db에 입력
            fcuser.userid = userid
            fcuser.username = username      
            fcuser.author = author
            fcuser.genre = user_genre
            db.session.add(fcuser)
            db.session.commit()
            return "회원가입 완료"

        return redirect('/')

    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bookshelves')
def bookshelves():
    return render_template('bookshelves.html')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))  # database 경로를 절대경로로 설정함
    dbfile = os.path.join(basedir, 'db.sqlite') # 데이터베이스 이름과 경로
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True     # 사용자에게 원하는 정보를 전달완료했을때가 TEARDOWN, 그 순간마다 COMMIT 하도록 설정
    #여러가지 쌓아져있던 동작들을 Commit을 해주어야 데이터베이스에 반영됨. 이러한 단위들은 트렌젝션이라고함.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # True하면 warrnig메시지 유발, 

    db.init_app(app) #초기화 후 db.app에 app으로 명시적으로 넣어줌
    db.app = app
    db.create_all()   # 이 명령이 있어야 생성됨. DB가


    app.run(host='127.0.0.1', port=5000, debug=True) 

