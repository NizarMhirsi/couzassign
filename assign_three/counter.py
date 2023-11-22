from flask import Flask , render_template , session , redirect

app = Flask(__name__)

app.secret_key = '1234'

counter = 0

@app.route("/")
def count():
    global total
    if 'count' in session:
        session['count'] = session.get('count') + 1  
    else:
        session['count'] = 1 
    return render_template("index.html",total =(session.get('count')))

@app.route('/destroy_session')
def delete_visits():
    session.pop('count', None) 
    return redirect("/", code=302)
    
    
