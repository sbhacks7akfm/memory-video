from flask import Flask, render_template, request, redirect, url_for
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
    uploaded_file = request.files.getlist("file")
    print(uploaded_file)
    if len(uploaded_file) == 0:
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('tryourservice'))


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/maps")
def maps():
    return render_template('maps.html')


if __name__ == "__main__":
    app.run(debug=True)
