import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/index")
def view_index():
    return "<h1> Hey user!</h1> <p>Do me a favor will ya? Please add your name to the end of the url in a '/user.yourname format, so I know who I'm talking too!</p>"