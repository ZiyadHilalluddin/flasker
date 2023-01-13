from flask import Flask, render_template


#Create a Flask Instance

app = Flask(__name__)

@app.route('/')

#def index():
#    return "</h1>Hello World!!!<h1>"

def index():  
    first_name = "ziyad"
    favourite_pizza = ["pepperoni", "cheese", "Mushroom", 41]
    return render_template('index.html', 
    first_name=first_name,
    favourite_pizza=favourite_pizza
    )

@app.route('/user/<name>')

#def user(name):
#    return "</h1>Hello {}!!!<h1>".format(name)

def user(name):
    return render_template('user.html', user_name = name)


#Create custom Error Page

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
     return render_template("404.html"), 404

#Internal Server Error 
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
