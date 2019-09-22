import flask

app = flask.Flask(__name__)

@app.route("/")
def view_index():
    return "<h1> Hello </h2>"

if __name__ == __main__:
    app.run()