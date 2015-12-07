#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# just for testing
oben_poem = "oben " * 20 + '\n'
oben_poem += ("links" + (69 * ' ') + "rechts\n") * 20
oben_poem += "unten " * 20 + '\n'

# just for testing
from random import randrange
def lorem(): #DEBUG
    #ipsum = lambda: " ".join(["Pack my box with five dozen liquor jugs."] * randrange(5, 16))
    #return "\n\n".join([ ipsum() for _ in range(randrange(5, 16)) ])
    poem = "I have eaten" + '\n'
    poem += "the plums" + '\n'
    poem += "that were in" + '\n'
    poem += "the icebox" + '\n' + '\n'

    poem += "and which" + '\n'
    poem += "you were probably" + '\n'
    poem += "saving" + '\n'
    poem += "for breakfast" + '\n' + '\n'

    poem += "Forgive me" + '\n'
    poem += "they were delicious" + '\n'
    poem += "so sweet" + '\n'
    poem += "and so cold" + '\n'

    return poem


def get_art(art_id):
    art = {}
    if art_id > 1:
        f = open("static/documnts/{}.txt".format(art_id), "r")
        art["text_type"] = "mono"
        art["title"] = art_id
        art["text"] = f.read()
        art["author"] = "documnt"
    else:
        art["text_type"] = "mono" if art_id else "prose"
        art["title"] = "schon dagewesen" if art_id else "THIS IS JUST TO SAY"
        art["text"] = oben_poem if art_id else lorem()
        art["author"] = "documnt"

    return art

@app.route('/')
def home():
    # just for testing
    return redirect(url_for('show_art', art_id=0)) #DEBUG

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
