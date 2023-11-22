from flask import Flask,render_template

app = Flask(__name__)
#declarit el dictionarry
users = [
         {"first_name" : "Micheal","last_name" : "Choi" },
         {"first_name" : "John", "last_name" : "Supsupin"},
         {"first_name" : "Mark", "last_name" : "Guillen"},
         {"first_name" : "KB", "last_name" : "Tonel"}

]
#rendert wbaatht el data lel template
@app.route("/")
def home():
    return render_template('index.html',users=users)