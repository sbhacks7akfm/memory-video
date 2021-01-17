from flask import Flask, render_template, request, redirect, url_for
import os
import datetime
from geo_getter import EXIFExtractor
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/tryourservice")
def tryourservice():
    return render_template('tryourservice.html')


@app.route("/tryourservice", methods=['POST'])
def upload_file():
    for file in os.listdir("./static/original/"):
        os.remove("./static/original/" + file)
    uploaded_file = request.files.getlist("file")
    print(uploaded_file)
    if len(uploaded_file) != 0:
        for file in uploaded_file:
            file.save("./static/original/" + file.filename)
    return redirect(url_for('maps'))


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/maps")
def maps():
    images = os.listdir('./static/original/')
    img_package = []
    counter = 0
    for img in images:
        efe = EXIFExtractor("./static/original/" + img)
        try:
            geotagging = efe.get_geotagging(efe.get_exif()[0])
        except ValueError as e:
            print(img)
            print(e)
            continue
        img_package.append([efe.get_coordinates(geotagging), efe.get_thumbnail(counter), efe.filename, efe.date_time, efe.dt])
        counter += 1
    img_package.sort(key=lambda x: x[-1])
    return render_template('maps.html', data=img_package)


if __name__ == "__main__":
    app.run(debug=True)
