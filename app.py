from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret tars backend lulz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions
db = SQLAlchemy(app)
