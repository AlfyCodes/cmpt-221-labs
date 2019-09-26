from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def view_index():
    return "<h1> Welcome to the Site! </h1> <p> If you want me to display your name, you can do so by typing: " \
           "'/user/yourname' into the url</p> <p> You can visit " \
           "the About " \
           "Me Page here: <a href='http://127.0.0.1:5000/about'>About Page</a> </p>"


@app.route("/user/<username>")
def user_name(username):
    return "<h1> AHHH HaHAhAHAha You're Trapped " +username +"!.. <br>It Puts The Lotion On It's Skin Or Else It Gets Hose AGAIN!</br></h1>"
            



@app.route("/about")
def about_page():
    return "<h1> Welcome to the most awesomest page! </h1> " \
           "<p> Why is this the most awesomest page?!? </p> " \
           "<ul> " \
           "<li> Because </li>  " \
           "<li>I </li> " \
           "<li> Said </li> " \
           "<li> So... </li> " \
           "<li>"\
           "<li> dot dot DOT!!!</li> " \
           "</ul>"\
           "<br>"\
           "<p> On a serious note, I made this website by using Flask. With Flask you can set up routes and also create dynamic routes.</p>" \
           "<ul>" \
           "<li> <b>Routes</b> are set by using @flaskname.route('/destination'). Look in your URL and you'll see there is an /about at the end. Thats the route to this AMAZING PAGE!</li>" \
           "<li> <b>Dynamic Routes</b> are just like routes but differ in that it takes in a response from the user. Depending on what kind of response it's looking for it will act accordingly. For example go back to the /index page and follow the instructions there about telling me your name by adding a route in the url. It's FUN!.... DO EEET!!!!</li>"
           

if __name__ == "__main__":
    app.run()
