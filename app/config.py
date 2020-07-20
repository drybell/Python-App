import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ONSHAPE_API_KEY = os.environ.get('ONSHAPE_API_KEY')
    ONSHAPE_SECRET_KEY = os.environ.get('ONSHAPE_SECRET_KEY')
    OAUTH_CALLBACK_URL = os.environ.get('OAUTH_CALLBACK_URL')
    OAUTH_CLIENT_ID =  os.environ.get('OAUTH_CLIENT_ID')
    OAUTH_CLIENT_SECRET = os.environ.get('OAUTH_CLIENT_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'app/static/uploads/'