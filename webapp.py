#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("issues.html")

@app.route('/issues')
def issues():
    return render_template("issues.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")  

@app.route('/mixtapes')
def mixtapes():
    return render_template("mixtapes.html")  

@app.route('/events')
def events():
    return render_template("events.html")  

@app.route('/files')
def files():
    return render_template("files.html") 

@app.route('/mixtape17')
def mixtape17():
	return render_template("mixtape17.html")

@app.route('/mixtape16')
def mixtape16():
	return render_template("mixtape16.html")

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

# @app.route('/documnt1-index')
# def documnt1index():
# 	return render_template("documnt1-index.html")

@app.route('/documnt-wants-to-be-free')
def documntwantstobefree():
	return render_template("documnt-wants-to-be-free.html")

@app.route('/mirjam-kroker-concept-nr-05-music-as-organisatorial-principle')
def conceptnr05():
	return render_template("mirjam-kroker-concept-nr-05-music-as-organisatorial-principle.html")

@app.route('/simon-roloff-how-to-do-things-with-docs')
def howtodothingswithdocs():
	return render_template("simon-roloff-how-to-do-things-with-docs.html")

@app.route('/diana-ludzay-gefühlt-aphrodite-mit-soße')
def gefuehltaphroditemitsosse():
	return render_template("diana-ludzay-gefühlt-aphrodite-mit-soße.html")

@app.route('/joeun-aatchim-your-poetry-reader')
def yourpoetryreader():
	return render_template("joeun-aatchim-your-poetry-reader.html")

@app.route('/karl-holmqvist-untitled-half-man-half-beast')
def halfmanhalfbeast():
	return render_template("karl-holmqvist-untitled-half-man-half-beast.html")

@app.route('/karl-holmqvist-ill-make-the-world-explode')
def illmaketheworldexplode():
	return render_template("karl-holmqvist-ill-make-the-world-explode.html")

@app.route('/tcf-3C-93-53-27-E4-E1-13-63-92-08-49-40-A4-E2-E4-35-E2-49-EF-2D-3D-E9-54-37-D3-C9-04-64-BF-3E-34')
def holdhusuntitled():
	return render_template("tcf-3C-93-53-27-E4-E1-13-63-92-08-49-40-A4-E2-E4-35-E2-49-EF-2D-3D-E9-54-37-D3-C9-04-64-BF-3E-34.html")

@app.route('/n-katherine-hayles-how-we-became-posthuman')
def howwebecameposthuman():
	return render_template("n-katherine-hayles-how-we-became-posthuman.html")

@app.route('/bisera-krckovska-on-transmissions')
def ontransmissions():
	return render_template("bisera-krckovska-on-transmissions.html")

@app.route('/herve-all-memorial-numerique')
def memorialnumerique():
	return render_template("herve-all-memorial-numerique.html")

@app.route('/jacques-ranciere-flesh-of-words')
def fleshofwords():
	return render_template("jacques-ranciere-flesh-of-words.html")

@app.route('/steve-rosenthal-berlin-boy')
def berlinboy():
	return render_template("steve-rosenthal-berlin-boy.html")

@app.route('/adrien-da-silva-with-the-book-my-body')
def withthebookmybody():
	return render_template("adrien-da-silva-with-the-book-my-body.html")

@app.route('/tinna-siradze-hello-world-dinosaurs-after-apocalypse')
def helloworlddinosaursafterapocalypse():
	return render_template("tinna-siradze-hello-world-dinosaurs-after-apocalypse.html")

@app.route('/kurt-eidsvig-mixed-messages')
def mixedmessages():
	return render_template("kurt-eidsvig-mixed-messages.html")

@app.route('/katarina-sylvan-et-in-arcadia-ego')
def etinarcadiaego():
	return render_template("katarina-sylvan-et-in-arcadia-ego.html")

@app.route('/wislawa-szymborska-tower-of-babel')
def towerofbabel():
	return render_template("wislawa-szymborska-tower-of-babel.html")

@app.route('/bryony-gillard-an-exploration-of-verbivocovisual-borders-and-margins')
def verbivocovisual():
	return render_template("bryony-gillard-an-exploration-of-verbivocovisual-borders-and-margins.html")

@app.route('/r-prost-enchiridions')
def enchiridions():
	return render_template("r-prost-enchiridions.html")

# @app.route('/documnt2-contents')
# def documnt2contents():
# 	return render_template("documnt2-contents.html")

@app.route('/documnt2')
def documnt2():
	return render_template("documnt2.html")

# @app.route('/documnt2-info')
# def documnt2info():
# 	return render_template("documnt2-info.html")

@app.route('/antigone')
def antigone():
	return render_template("antigone.html")

@app.route('/ana-under-god-2')
def anaundergod2():
	return render_template("ana-under-god-2.html")

# @app.route('/giant-sad-steps')
# def giantsadsteps():
# 	return render_template("giant-sad-steps.html")

# @app.route('/food-order')
# def foodorder():
# 	return render_template("food-order.html")


# @app.route('/accounting')
# def accouting():
# 	return render_template("accounting.html")

# @app.route('/anja-kaiser-sexed-realities')
# def sexedrealities():
# 	return render_template("anja-kaiser-sexed-realities.html")

# @app.route('/in-other-worlds')
# def inotherworlds():
# 	return render_template("in-other-worlds.html")

@app.route('/hanne-lippard-keywords-scans')
def keywordsscans():
	return render_template("hanne-lippard-keywords-scans.html")

@app.route('/ella-coon-digitized-archives-digital-archives')
def digitizedarchivesdigitalarchives():
	return render_template("ella-coon-digitized-archives-digital-archives.html")

@app.route('/experimental-jetset-two-or-three-things-i-know-about-provo')
def twoorthreethingsiknowaboutprovo():
	return render_template("experimental-jetset-two-or-three-things-i-know-about-provo.html")

@app.route('/anna-erdmann-the-dark-room-as-a-spiritual-path')
def darkroom():
	return render_template("anna-erdmann-the-dark-room-as-a-spiritual-path.html")

@app.route('/lynne-huffer-foucaults-fossils')
def foucaultsfossils():
	return render_template("lynne-huffer-foucaults-fossils.html")

@app.route('/hito-steyerl-politics-of-the-archive')
def politicsofthearchive():
	return render_template("hito-steyerl-politics-of-the-archive.html")

# @app.route('/demo')
# def show_demo():
#     return render_template("demo.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
