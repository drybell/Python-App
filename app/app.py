from flask import Flask, render_template, flash, redirect
from .config import Config
from .forms.get_document_details import DocumentDetailsForm
from onshape_client.client import Client
import sys
import json 

# from template import 
app = Flask(__name__)
app.config.from_object(Config)

base_api_url = 'https://rogers.onshape.com'
onshape_headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
client = Client(configuration={"base_url": base_api_url, "access_key": key, "secret_key": secret})

@app.route("/")
def home():
	return render_template('base.html', title='Home')

@app.route("/details", methods=['GET', 'POST'])
def details(client):
	form = DocumentDetailsForm()
	if form.validate_on_submit():
		key = app.config['ONSHAPE_API_KEY']
		secret = app.config['ONSHAPE_SECRET_KEY']
		headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
		test_api_call = '/api/elements/d/did/w/wid/e/eid/configuration'
		test_api_call = test_api_call.replace("did", str(form.did._value()))
		test_api_call = test_api_call.replace("wid", str(form.wid._value()))
		test_api_call = test_api_call.replace("eid", str(form.eid._value()))
		print(base_api_url + test_api_call, file=sys.stderr)
		r = client.api_client.request('GET', url = base_api_url + test_api_call, query_params={}, headers=headers)
		x = json.loads(r.data)
		print(json.dumps(x, indent=2))
		flash(json.dumps(x, indent=2))
		return redirect('/')
	return render_template('doc.html', title='Details', form=form)

@app.route("/api-calls1")
def part_studio_contents():
	return ("<h1> This Page Will Give You Part Studio Details</h1>")

@app.route("/api-calls2")
def feature_studio_contents():
	return ("<h1> This Page Will Return Feature Studio Scripts</h1>")

# @app.route("/api-calls3")
# def 