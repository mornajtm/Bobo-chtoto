from flask import Flask, render_template, request, send_from_directory
import random
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    number = 0
    if request.method == "POST":
        number = request.form.get("num", type=int)
    if number is not None and number != 0:
        lvl = number
        number = lvl**2 + (6 * lvl)
    return render_template('index.html', num=number)


def get_image_files():
    path = os.path.join('static', 'images')
    return os.listdir(path)


@app.route('/mem', methods=['GET', 'POST'])
def index():
    image_name = request.form.get('image_name', '')
    top_text = request.form.get('top_text', '')

    image_list = get_image_files()
    return render_template('mem.html',
                           image_name=image_name,
                           image_list=image_list,
                           top_text=top_text)


@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)