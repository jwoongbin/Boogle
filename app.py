from flask import *
import requests
from flask_assets import Environment, Bundle
app = Flask('mars_discovery')
# SCSS
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('sb-admin-2.css',filters='pyscss', output='all.css')
assets.register('scss_all',scss)

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

