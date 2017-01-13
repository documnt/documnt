#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")  

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/issues')
def issues():
    return render_template("issues.html") 

@app.route('/mixtapes')
def mixtapes():
    return render_template("mixtapes.html") 

@app.route('/art')
def art():
    return render_template("art.html") 

@app.route('/texts')
def texts():
    return render_template("texts.html")

@app.route('/videos')
def videos():
	return render_template("videos.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")  

@app.route('/demo')
def show_demo():
    return render_template("demo_content.html")

@app.route('/demo2')
def show_demo2():
    return render_template("demo_content2.html")

@app.route('/demo3')
def show_demo3():
    return render_template("demo_content3.html")

@app.route('/demo4')
def show_demo4():
    return render_template("demo_content4.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
