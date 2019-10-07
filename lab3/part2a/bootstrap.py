from flask import Flask, flash, redirect, render_template;
#import from forms.py that was created
from forms import ContactForm

#Flask Object
app = Flask(__name__)

app.config["SECRET_KEY"] = "Teacher Leave Them Kids Alone"

#Set routes for index.html
@app.route('/', methods=["GET", "POST"])
def root():

    forms = ContactForm()

    #Check for submittals

    if forms.validate_on_submit():
        print("Test")
        flash("A new form has been submitted: Name {}, Phone {}, Message{}" .format(forms.name.data, forms.email.data, forms.phone_number.data, forms.message.data))
    #return index html
    return render_template('index.html', name='Alfred Ortiz Jr', workType='Engineer - National Guard Air Force - Father', forms=forms), 200

#Run Flask Programmaticcally
if __name__ == '__main__':
    #Debug is true, host is local, and port set to 80
    app.run(debug=True, host='127.0.0.1', port=80)