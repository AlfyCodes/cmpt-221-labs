from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "<h1> Welcome! </h1>"\
            "<p> My name is Alfred Ortiz Jr. I grew up in the Bronx for 16 years then moved to Walden,Ny. I've lived " \
           "in Middletown, Newburgh, and now reside in Montgomery. I'm 29 years old with a wife and a son. "



if __name__ == "__main__":
    app.run()
