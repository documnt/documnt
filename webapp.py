#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/issues')
def issues():
    return render_template("issues.html")

@app.route('/about')
def about():
    return render_template("about.html")  

@app.route('/mixtapes')
def mixtapes():
    return render_template("mixtapes.html")  

# @app.route('/mixtapes/01')
# def mixtape01():
#     return render_template("01.html") 

@app.route('/files')
def files():
    return render_template("files.html") 

@app.route('/mixtape15')
def mixtape15():
	return render_template("mixtape15.html")

@app.route('/mixtape14')
def mixtape14():
	return render_template("mixtape14.html")

@app.route('/mixtape13')
def mixtape13():
	return render_template("mixtape13.html")

@app.route('/mixtape12')
def mixtape12():
	return render_template("mixtape12.html")

@app.route('/mixtape11')
def mixtape11():
	return render_template("mixtape11.html")

@app.route('/mixtape10')
def mixtape10():
	return render_template("mixtape10.html")

@app.route('/mixtape09')
def mixtape09():
	return render_template("mixtape09.html")

@app.route('/mixtape08')
def mixtape08():
	return render_template("mixtape08.html")

@app.route('/mixtape07')
def mixtape07():
	return render_template("mixtape07.html")

@app.route('/mixtape06')
def mixtape06():
	return render_template("mixtape06.html")

@app.route('/mixtape05')
def mixtape05():
	return render_template("mixtape05.html")

@app.route('/mixtape04')
def mixtape04():
	return render_template("mixtape04.html")

@app.route('/mixtape03')
def mixtape03():
	return render_template("mixtape03.html")

@app.route('/mixtape02')
def mixtape02():
	return render_template("mixtape02.html")

@app.route('/mixtape01')
def mixtape01():
	return render_template("mixtape01.html")

@app.route('/documnt1-index')
def documnt1index():
	return render_template("documnt1-index.html")


# @app.route('/demo')
# def show_demo():
#     return render_template("demo.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
