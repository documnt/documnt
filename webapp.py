from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This would show a bunch of art entries."

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

@app.route('/<int:art_id>/mono')
def show_mono(art_id):
    return "This would show art #{} in monospace text.".format(art_id)

@app.route('/<int:art_id>/text')
def show_text(art_id):
    return "This would show art #{} in variable-width text.".format(art_id)

@app.route('/<int:art_id>/prose')
def show_prose(art_id):
    return "This would show art #{} in justified variable-width text.".format(art_id)
