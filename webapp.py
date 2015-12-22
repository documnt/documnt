#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# just for testing
oben_poem = "oben " * 20 + '\n'
oben_poem += ("links" + (69 * ' ') + "rechts\n") * 20
oben_poem += "unten " * 20 + '\n'


docs = {'punishment': 'https://docs.google.com/document/d/1jLnJRkie9RqdV_5-9M7mkque_w17ZS8fWwQGWZKtATM/pub?embedded=true',
         'mixtape-01': 'https://docs.google.com/document/d/1ro-zU4bXFsAq8kh4BYJnYxsBTUmPyCbKHzdxx7KIUBI/pub?embedded=true',
         'smooth-jazz': 'https://docs.google.com/document/d/16W2hYGWG6L3GuVq_Hv8RW8OaLBSnPxJoFQY23L8g8Hg/pub?embedded=true',
         'other': 'about:blank'}

doc_heights = {'punishment': 1400,
               'mixtape-01': 500,
               'smooth-jazz': 4400,
               'other': 1000}


mixes = {'mixtape-01': 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/236993486&amp;color=000000&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false'}


# just for testing
from random import randrange
def lorem(): #DEBUG
    #ipsum = lambda: " ".join(["Pack my box with five dozen liquor jugs."] * randrange(5, 16))
    #return "\n\n".join([ ipsum() for _ in range(randrange(5, 16)) ])
    poem = "\n"+"\n"+"\n"
    poem += "This is just to say" + '\n'
    poem += "by William Carlos Williams" + '\n'
    poem += "\n"+"\n"+"\n"
    poem += "I have eaten" + '\n'
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
        art["author"] = "author"
    else:
        art["text_type"] = "mono" if art_id else "prose"
        art["title"] = "1" if art_id else "0"
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

#added by Matt:
@app.route('/submit')
def submit():
    return "This would show a submit page."

#added by Matt:
@app.route('/essay')
@app.route('/essay/<essay_title>')
def essay(essay_title='smooth-jazz'):
    if essay_title:
        doc = {}
        doc["title"] = essay_title
        doc["googledoc_url"] = docs[essay_title]
        doc["height"] = doc_heights[essay_title]
        return render_googledoc(doc)
    else:
        return render_template("base.html")

#added by Matt:
@app.route('/poem')
@app.route('/poem/<poem_title>')
def poem(poem_title='punishment'):
    if poem_title:
        doc = {}
        doc["title"] = poem_title
        doc["googledoc_url"] = docs[poem_title]
        doc["height"] = doc_heights[poem_title]
        return render_googledoc(doc)
    else:
        return render_template("base.html")


#added by Matt:
@app.route('/mix')
@app.route('/mix/<mix_title>')
def mix(mix_title='mixtape-01'):
    if mix_title:
        mix = {}
        mix['mix_url'] = mixes[mix_title]
        doc = {}
        doc["title"] = mix_title
        doc["googledoc_url"] = docs[mix_title]
        doc["height"] = doc_heights[mix_title]
        return render_mix(mix, doc)
    else:
        return render_template("base.html")


#@app.route('/contact')
#def contact():
#    return "This would show a contact page."

@app.route('/<int:art_id>/meta')
def about_art(art_id):
    return "This would show an overview of art #{}.".format(art_id)

def render_mix(mix, doc):
    return render_template("base.html", **mix, **doc)

def render_googledoc(doc):
    return render_template("base.html", **doc)

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
