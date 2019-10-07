from flask import Flask, flash, print, redirect, render_template;
#import from forms.py that was created
from InClass.FlaskWTF.forms import ContactForm

#Flask Object
app = Flask(__name__)

app.config["SECRET_KEY"] = "Teacher Leave Them Kids Alone"

#Set routes for index.html
@app.route('/')
def root():

    forms = ContactForm()

    #Check for submittals

    if forms.validateOnSubmit():
        print("ok")
        flash("A new form has been submitted: Name {}, Phone {}, Message{}" .format(forms.name.data, forms.email.data, forms.phone_number.data, forms.message.data))
    #return index html
    return render_template('index.html', name='Alfred Ortiz Jr', workType='Engineer - National Guard Air Force - Father'), 200

#Run Flask Programmaticcally
if __name__ == '__main__':
    #Debug is true, host is local, and port set to 80
    app.run(debug=True, host='127.0.0.1', port=80)