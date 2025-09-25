from flask import Flask, render_template # type: ignore

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "titulo": "Hola Flask",
        "contenido": "Este es mi primer post en Flask.",
    },
    {
        "id": 2,
        "titulo": "Jinja Tips",
        "contenido": "Unos truquitos útiles para Jinja y templates.",
    },
    {
        "id": 3,
        "titulo": "Deploy rápido",
        "contenido": "Cómo desplegar una app Flask en minutos.",
    },
]


@app.route('/')
def home():
    return render_template('index.html', posts = posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post_id == post['id']),None)
    if post:
        return render_template('post.html', post = post)
    else:
        return "Page not found", 404

if __name__ == "__main__":
    app.run(debug=True)