from application.config import DevConfig, ProdConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.static_folder = 'static'
app.templates_folder='templates'

app.config.from_object(DevConfig)

socketio = SocketIO(app)
db = SQLAlchemy(app)

