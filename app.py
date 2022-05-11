from flask import *
import requests
app = Flask('mars_discovery')

@app.route('/')
@app.route('/main')
def main():
    books = []
    if 'book' in request.args:
        search_word = request.args.get('book')
        response = requests.get("http://gutendex.com/books/?search="+search_word)
        data = json.loads(response.content)
        books = data['results']
        return render_template('results.html', books=books)
    else:
        return render_template('common.html', books=books)


@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bookshelves')
def bookshelves():
    return render_template('bookshelves.html')

app.run(debug= True)

