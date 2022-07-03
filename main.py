from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/resource-catalog')
def rCatalog():
	return "Hi"

@app.route("/connect")
def connect():
	return "Hi"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
