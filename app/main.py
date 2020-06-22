from flask import Flask, render_template
# from template import 
app = Flask(__name__)

@app.route("/")
def home_view():
	return render_template('base.html', title='Home')

@app.route("/api-calls1")
def part_studio_contents():
	return ("<h1> This Page Will Give You Part Studio Details</h1>")

@app.route("/api-calls2")
def feature_studio_contents():
	return ("<h1> This Page Will Return Feature Studio Scripts</h1>")

# @app.route("/api-calls3")
# def 