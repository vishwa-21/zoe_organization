from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/resource-catalog')
def rCatalog():
	return render_template("rCatalog.html")

@app.route("/connect")
def connect():
	return render_template("connect.html");

@app.route("/contribute")
def contribute():
	return render_template("contribute.html");

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
