from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def view_index():
    return render_template("index.html")           

@app.route("/user/<username>")
def user_name(username):
    return render_template("user.html",username=username)
            
@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()