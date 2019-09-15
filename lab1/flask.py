import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/index")

def view_index():
    return "<h1>Hello World!</h1>"

@app.route("/user/<username>")
def view_user(username):
    return "<h1>Hello World! " +username + " </h1>"


if __name__ == "__main__":
    app.run()
