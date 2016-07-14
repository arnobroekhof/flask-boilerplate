# Flask
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging

# Create Flask app
app = Flask(__name__)
app.config.from_envvar('TRANSLOGIC_CONFIG')
# add Flask RestFUL Api
api = Api(app)
# Add SQLAlchemy
db = SQLAlchemy(app)


# load balancer checks
@app.route('/health')
def healthcheck():
    app.logger.debug('Health requested')
    return 'ok'

# add api views
