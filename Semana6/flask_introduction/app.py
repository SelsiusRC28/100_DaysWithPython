from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.errorhandler(404)
def error(e):
    return render_template('error.html', e=e), 404

if __name__ == "__main__":
    app.run(debug = True)