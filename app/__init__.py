import redis
from celery import Celery
from rq import Queue
from flask import Flask
from flask_migrate import Migrate

from celeryRunner import make_celery
from settings import USERDB, PASSWORD, HOST, DATABASE

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)
celery = make_celery(app)

print(f"mysql+pymysql://{USERDB}:{PASSWORD}@{HOST}/{DATABASE}")
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERDB}:{PASSWORD}@{HOST}/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Adding Models

from Models import db

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

"""
This part is crucial as it picks up all of the Models thus any
additional changes we make to the schema, they can be update via:

flask db migrate -m 'Put Message HERE'
flask db upgrade 
"""
# Importing models of DB
from Models import asset, tradingHistory, smartContract

# Adding API endpoints
from app import views
