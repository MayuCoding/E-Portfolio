from application.config import DevConfig, ProdConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
app = Flask(__name__)
app.static_folder = 'static'
app.templates_folder='templates'

app.config.from_object(DevConfig)

socketio = SocketIO(app)
db.init_app(app)

