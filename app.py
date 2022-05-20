from webbrowser import get
from flask import *
import requests
import json
from models import db
import os
from models import Fcuser
from form import RegisterForm
import secrets

app = Flask('mars_discovery')
app.config["SECRET_KEY"] = secrets.token_hex(16)

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
    form = RegisterForm()
  
    genre_data=[{'genre': 'Literature'}, {'genre': 'History'}, {'genre': 'Philosophy'}]
    author_data=[{'author': 'Spinoza'}, {'author': 'Karl Marx'}, {'author': 'Nietzsche'}]  
    if request.method == 'POST':
        #회원정보 생성
        if form.validate_on_submit():
            username = form.data.get('username')
            email = form.data.get('email') 
            password = form.data.get('password')

            genre = request.form.get('genre')
            author = request.form.get('author')
            
            fcuser = Fcuser()         
            fcuser.username = username      
            fcuser.useremail = email
            fcuser.password = password #models의 FCuser 클래스를 이용해 db에 입력
            fcuser.author = author
            fcuser.genre = genre
            way = request.form.get('way')
            if(way == 'Audio'):
                fcuser.way = way
            db.session.add(fcuser)
            db.session.commit()
            flash('회원 가입이 완료되었습니다.', 'success')
        else:
            flash('Please check the entered value.', 'danger')
    return render_template("register.html", form=form, genre_data=genre_data, author_data=author_data)

    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bookshelves')
def bookshelves():
    return render_template('bookshelves.html')

@app.route('/details')
def details():
    
    topic = 'buddhism'
    response = requests.get("http://gutendex.com/books/?topic="+topic)
    data = json.loads(response.content)
    books = []
    books = data['results']
    
    author = 'nietzsche'
    response = requests.get("http://gutendex.com/books/?search="+author)
    data = json.loads(response.content)
    books2 = []
    books2 = data['results']   
        
    return render_template('details.html', books=books, books2=books2)


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

