#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# just for testing
from random import randrange
def lorem(): #DEBUG
    ipsum = lambda: " ".join(["Pack my bag with five dozen liquor jugs."] * randrange(5, 16))
    return "\n\n".join([ ipsum() for _ in range(randrange(5, 16)) ])

def get_art(art_id):
    if art_id != 0: raise FileNotFoundError("No such art!")
    art = {}
    art["text_type"] = "prose"
    art["title"] = "What is art"
    art["text"] = lorem()
    art["author"] = "Nobody at all"
    return art

@app.route('/')
def home():
    # just for testing
    return redirect(url_for('show_prose', art_id=0)) #DEBUG

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

def render_art(art):
    if art["text_type"] == "mono":
        template = "monospaced.html"
    else:
        template = "literary.html"

    try:
        return render_template(template, **art)
    except FileNotFoundError:
        return "No art found with id {}.".format(art_id)

@app.route('/<int:art_id>')
def show_art(art_id):
    return render_art(get_art(art_id))

@app.route('/<int:art_id>/poetry')
def show_poetry(art_id):
    art = get_art(art_id)
    art["text_type"] = "poetry"
    return render_art(art)

@app.route('/<int:art_id>/prose')
def show_prose(art_id):
    art = get_art(art_id)
    art["text_type"] = "prose"
    return render_art(art)

@app.route('/<int:art_id>/mono')
def show_mono(art_id):
    art = get_art(art_id)
    art["text_type"] = "mono"
    return render_art(art)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
