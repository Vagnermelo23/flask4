from flask import Flask
from app.routes import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/index')
