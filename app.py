#import section where we imported the flask_wtf library
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
#StringField and Passwordfield ones of standard form Fields to design the form in python script

app= Flask(__name__)
app.config['SECRET_KEY'] = 'asercret'

class LoginForm(FlaskForm):
    """
    class used to design to define the fields need in our form
    
    args:
        username = StringField('username') which will design a text field which allows you to put strings 
        password = PasswordField('password') which will design a text field that allows to change the inputs into password typed
    """
    username = StringField('username')
    password = PasswordField('password')

# in routing the methods argument helps GET and POST to be Recognisable by the send request

@app.route('/form',methods=['GET','POST'])
def form():
    form = LoginForm()
    #form is an object of LoginForm

    if form.validate_on_submit():
        # return 'the form has been submitted'
        return '<h1>The username is {}. The password is {}.</h1?'.format(form.username.data,form.password.data)

    # the if statement is using a validation method from wtforms library to perform action when the submit button is pressed
    # in return of if, the {} is to be replaced by form.username.data and form.password.data values
    # format method which is having two arguments helps to fetch the values passed to those fields   

    return render_template('form.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)