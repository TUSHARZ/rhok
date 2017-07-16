from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html', contents = {})


@app.route("/disease")
def diseases():
	content = {
	'disease' : 'cardiovascular',
	}
	return render_template('disease.html', contents = content)
