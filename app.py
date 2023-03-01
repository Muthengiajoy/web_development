from flask import Flask,render_template


app = Flask(__name__)

@app.route("/about")
def  about():
    return render_template("indx.htm")
