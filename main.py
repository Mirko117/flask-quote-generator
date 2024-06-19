from flask import Flask, render_template, request, send_file, send_from_directory
from functions import *


app = Flask(__name__)

@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename, mimetype='application/javascript')

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api_quote")
def api_quote():
    return render_template('api_quote.html', fonts=fonts)


@app.route("/ai_quote")
def ai_quote():
    return render_template('ai_quote.html')


@app.route('/get_api_quote', methods=['POST'])
def get_api_quote():
    data = request.json

    bg = bool(int(data['background'])) #true or false
    fonts_pick = int(data.get('font')) #int
    tags = data.get('tags')
    image_url = ""

    if bg:
        image_url = get_random_image_url(tags)

    quote_text = get_random_quote()

    return send_file(make_image(image_url, quote_text, fonts_pick, bg), mimetype='image/jpeg')
    

if __name__ == '__main__':
    app.run()