from flask import Flask, render_template;

#Flask Object
app = Flask(__name__)

#Set routes for index.html
@app.route('/')
@app.route('/root')
def root():
    #return index html
    return render_template('index.html'), 200

#Run Flask Programmaticcally
if __name__ == 'main':
    #Debug is true, host is local, and port set to 80
    app.run(debug=true,host='127.0.01', port=80)