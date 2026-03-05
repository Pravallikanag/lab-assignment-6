from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to Flask!</h1>"

# Dynamic route
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", name=name)

# Form page
@app.route("/form")
def form():
    return render_template("form.html")

# Form submission
@app.route("/greet", methods=["POST"])
def greet():
    name = request.form["name"]
    return redirect(url_for("hello", name=name))

if __name__ == "__main__":
    app.run(debug=True)
