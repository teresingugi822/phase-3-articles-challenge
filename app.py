from flask import Flask, render_template_string
from lib.models import Magazine
from db import CONN, CURSOR

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the Articles App</h1><p>Visit <a href="/magazines">/magazines</a> to see all magazines.</p>'

@app.route('/magazines')
def show_magazines():
    magazines = Magazine.all()
    html = """
    <h1>All Magazines</h1>
    <ul>
    {% for magazine in magazines %}
        <li><strong>{{ magazine.name }}</strong> — Category: {{ magazine.category }}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, magazines=magazines)

if __name__ == '__main__':
    app.run(debug=True)
