from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.get("/index")
def index():
    return render_template("index.html")

app.run()