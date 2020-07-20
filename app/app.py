from flask import Flask, render_template, flash, redirect, jsonify, send_from_directory, url_for 
from .config import Config
from .forms.get_document_details import DocumentDetailsForm
from onshape_client.client import Client
import sys
import json 
from .image_onshape import imageToOnshape
from .image_plot import imageToPlot
from werkzeug.utils import secure_filename
from datetime import datetime
import pathlib
from oauthlib.oauth2 import WebApplicationClient

# from template import 
app = Flask(__name__, static_folder='./static')
app.config.from_object(Config)


ALLOWED_EXTENSIONS = set(['png', 'jpg'])

base_api_url = 'https://rogers.onshape.com'
oauthUrl = 'https://oauth.onshape.com'
authorizationURL = oauthUrl + "/oauth/authorize"
tokenUrl = oauthUrl + "/oauth/token"
userProfileURL = base_api_url + "/api/users/sessioninfo"
callbackUrl = app.config['OAUTH_CALLBACK_URL']


onshape_headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
key = app.config['ONSHAPE_API_KEY']
secret = app.config['ONSHAPE_SECRET_KEY']
client = Client(configuration={"base_url": base_api_url, "access_key": key, "secret_key": secret})
# oauth_client = WebApplicationClient(app.config['OAUTH_CLIENT_ID'])

did = ""
wid = ""
eid = ""
image_path = ""
feature_title = ""

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/query/uploads/<int:year>/<int:month>/<int:day>/<int:second>/<file>/<int:scale>/<int:thresh>', methods= ['GET'])
def plot_data(year, month, day, second, file, scale, thresh):
	file_path = app.config['UPLOAD_FOLDER'] + str(year) + '/' + str(month) + '/' + str(day) + '/' + str(second) + '/' + file 
	html, [x,y] = imageToPlot(file_path, scale, thresh)
	return jsonify({"html": html, "x": x, "y": y})

@app.route('/sketch/<int:scale>/<int:thresh>', methods= ['GET'])
def send_sketch_onshape(scale, thresh):
	global did, wid, eid, image_path, feature_title
	status = imageToOnshape(key, secret, image_path, feature_title, ids=[did,wid,eid], scale=scale, thresh=thresh)
	return jsonify({'status': status})

@app.route("/details")
def home():
	global image_path
	return render_template('base.html', title='Home', value=image_path[4:])

@app.route("/", methods=['GET', 'POST'])
@app.route('/index')
def details():
	form = DocumentDetailsForm()
	global did,wid,eid,image_path, feature_title
	if form.validate_on_submit():
		try: 
			headers = {'Accept': 'application/vnd.onshape.v1+json', 'Content-Type': 'application/json'}
			test_api_call = '/api/featurestudios/d/did/w/wid/e/eid'
			test_api_call = test_api_call.replace("did", str(form.did._value()))
			test_api_call = test_api_call.replace("wid", str(form.wid._value()))
			test_api_call = test_api_call.replace("eid", str(form.eid._value()))
			# print(base_api_url + test_api_call, file=sys.stderr)
			feature_title = str(form.feature_title._value())
			filename = secure_filename(form.image.data.filename)
			if allowed_file(filename):
				_now = datetime.now()
				year, month, day, second = _now.year, _now.month, _now.day, _now.second
				image_upload_path = app.config['UPLOAD_FOLDER'] + str(year) + "/" + str(month) + "/" + str(day) + "/" + str(second) + "/" + filename
				folders = app.config['UPLOAD_FOLDER'] + "/" + str(year) + "/" + str(month) + "/" + str(day) + "/" + str(second) + "/"
				pathlib.Path(folders).mkdir(parents=True, exist_ok=True)
				form.image.data.save(image_upload_path)
			else:
				raise Exception
			r = client.api_client.request('GET', url = base_api_url + test_api_call, query_params={}, headers=headers)
			# x = json.loads(r.data)
			# print(json.dumps(x, indent=2))
		except Exception as e: 
			print(e, file=sys.stderr)
			flash("Incorrect IDs and/or file format. Try again")
			return redirect('/details')
		did, wid, eid, image_path = (str(form.did._value()), str(form.wid._value()), str(form.eid._value()), image_upload_path)
		# flash("DID: %s, WID: %s, EID: %s, IMAGE: %s" % (str(form.did._value()), str(form.wid._value()), str(form.eid._value()), image_path))
		return redirect('/details')
	return render_template('doc.html', title='Details', form=form)

@app.route('/<filename>')
def send_uploaded_file(filename):
	print(filename, file=sys.stderr)
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
	app.run()