from flask import Flask

'''
First, we create an instance of the Flask class, 
which will be our WSGI (Web Server Gateway Interface) application.
''' 

app = Flask(__name__)  

@app.route('/') # This is a decorator that creates a route.
def welcome():
    return "Welcome to this amazing Flask app home page!"

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__ == '__main__':
    app.run(debug=True)
    
    
