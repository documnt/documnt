#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")  

@app.route('/issues')
def issues():
    return render_template("issues.html") 

@app.route('/mixtapes')
def mixtapes():
    return render_template("mixtapes.html") 

@app.route('/contact')
def contact():
    return render_template("contact.html")  

@app.route('/demo')
def show_demo():
    return render_template("demo_content.html")

@app.route('/demo2')
def show_demo2():
    return render_template("demo_content2.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
