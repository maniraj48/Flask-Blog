from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        "author" : "Neel",
        "book" : "Salaar",
        "year" : 2023
    },
    {
        "author" : "Deva",
        "book" : "Nibandhana",
        "year" : 2023
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/contact")
def contact():
    return "Contact PAge"


if __name__ == '__main__':
    app.run(debug=True)
