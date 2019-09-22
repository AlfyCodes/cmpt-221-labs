from flask import Flask

app = Flask(__name__)

@app.route("/")
def view_index():
    return "<h1> hi </h1>"

if __name__ == "__main__":
    app.run()