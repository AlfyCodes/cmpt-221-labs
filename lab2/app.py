from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def view_index():
    return "<h1> Welcome! </h1> <p> You can tell me your name by: '/user/yourname'</p> <p> You can visit the About " \
           "Me Page here: <a href='http://127.0.0.1:5000/about'>About Page</a> </p>"


@app.route("/user/<username>")
def user_name(username):
    return "<h1> Hey " + username + "!</h1>"


@app.route("/about")
def about_page():
    return "<h1> Welcome to the most awesomest page! <p> Why is this the most awesomest page?!? </p> <ul> "

if __name__ == "__main__":
    app.run()
