from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def view_index():
    return "<h1> Hey there! </h1> <p> Can you do me a favor and write your name at the end of the url Like this: '/user/yourname'?</p> <p> Or if you want go check out the Welcome Page here:</p>"

@app.route("/user/<username>")
def user_name(username):
    return "<h1> Hey " +username+ "!</h1>"

@app.route("/welcome")
def welcome_page():
    return "<h1> Welcome to the most awesomest page "

if __name__ == "__main__":
    app.run()
