from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.secret_key = "my_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# Initialize Database
db = SQLAlchemy(app)

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique = True)
    password = Column(String, nullable=False, unique = True)
    
with app.app_context():
    db.create_all()
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        password = generate_password_hash(request.form['password'])
        
        if not username or not email or not password:
            flash("Required all data", 'error')
            return redirect(url_for('register'))
        
        try:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
        except:
            db.session.rollback()
            flash('Username or Email already exists!', 'error')
            
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)