from app import app
from flask import render_template

# import one_for_all

@app.route("/")
@app.route("/index")
def index():
	return render_template('home.html', contents = {})


@app.route("/disease")
def diseases():
	# content = one_for_all.mydict
	return render_template('disease.html', contents = content)


@app.route("/well")
def well():
	return render_template('well.html', contents = {})