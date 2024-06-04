from flask import Flask, render_template
from functions import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api_quote")
def api_quote():
    return render_template('api_quote.html')


@app.route("/ai_quote")
def api_quote():
    return render_template('ai_quote.html')


if __name__ == '__main__':
    app.run(debug=True)