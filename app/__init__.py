from flask import Flask
from app.apis import blueprint as api

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/")