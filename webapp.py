#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# DEBUG
from random import randrange
def lorem():
    ipsum = lambda: " ".join(["Pack my bag with five dozen liquor jugs."] * randrange(5, 16))
    return "\n\n".join([ ipsum() for _ in range(randrange(5, 16)) ])

@app.route('/')
def home():
    return redirect(url_for('show_prose', art_id=28))

@app.route('/authors')
def authors():
    return "This would show a page about those authors who have content on the site."

@app.route('/about')
def about():
    return "This would show an about page."

@app.route('/contact')
def contact():
    return "This would show a contact page."

@app.route('/<int:art_id>/meta')
def about_art(art_id):
    return "This would show an overview of art #{}.".format(art_id)

@app.route('/<int:art_id>')
def show_art(art_id):
    return "This would show art #{} in the artist-chosen format/s.".format(art_id)

@app.route('/<int:art_id>/poetry')
def show_poetry(art_id):
    return render_template('literary.html', text_type="poetry", title=art_id, author="Nobody", text=lorem())

@app.route('/<int:art_id>/prose')
def show_prose(art_id):
    return render_template('literary.html', text_type="prose", title=art_id, author="Nobody", text=lorem())

@app.route('/<int:art_id>/mono')
def show_mono(art_id):
    return render_template('monospaced.html', title=art_id, author="Nobody", text=lorem())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
