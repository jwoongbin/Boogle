from flask import *
import requests
app = Flask('mars_discovery')

@app.route('/')
@app.route('/home')
def home():
    books = []
    if 'book' in request.args:
        search_word = request.args.get('book')
        response = requests.get("http://gutendex.com/books/?search="+search_word)
        data = json.loads(response.content)
        books = data['results']
        return render_template('results.html', books=books)
    else:
        return render_template('main.html', books=books)

app.run(debug= True)

