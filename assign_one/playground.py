from flask import Flask, render_template , url_for , redirect

app = Flask(__name__)
#fl tasliha zedt juste redirection ml main route lel /play
@app.route("/")
def home(): 
    return redirect("/play", code=302)

#el route thenya thez lel main page again ama bl url /play
@app.route("/play")
def home_a(): 
    return render_template("index.html" , num = 1)

#el theltha bl url for feha var number louta hatina lvaleur mteeha assigned lel var num bch naaytoulha fjinja

@app.route("/play/<number>")
def play(number):
    return render_template("index.html" , num=number)

#same houni ama avec el var color en plus

@app.route("/play/<number>/<color>")
def changecol(number , color):
    return render_template("index.html" , num=number , myCol=color)

