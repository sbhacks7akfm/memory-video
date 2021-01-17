from flask import Flask, render_template
import os, datetime
from geo_getter import EXIFExtractor
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/tryourservice")
def tryourservice():
    return render_template('tryourservice.html')


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/maps")
def maps():
    images = os.listdir('./static/original/')
    img_package = []
    counter = 0
    for img in images:
        img_package.append(EXIFExtractor("./static/original/" + img).get_coors_n_thumb(counter))
        counter += 1
    img_package.sort(key = lambda x: x[-1])
    return render_template('maps.html', data=img_package)

if __name__ == "__main__":
    app.run(debug=True)
