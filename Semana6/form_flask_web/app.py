from flask import Flask, render_template, request

from form import UserForm

app = Flask(__name__)

@app.route('/')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    form = UserForm(request.form)
    if form.validate():
        username = request.form['username']
        email = request.form['email']
        form  = [username, email]
        return render_template('success.html', form=form)
    else:
        return "Invalidate form"

app.run(debug=True)