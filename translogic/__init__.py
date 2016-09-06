# Flask
from flask import Flask
from flask_restful import Api
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect

# Create Flask app
app = Flask(__name__, static_url_path='/static')
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


# Flask-WTF CSRF Protection
csrf = CsrfProtect()
csrf.init_app(app)


def csrf_error(reason):
    app.logger.debug("CSRF ERROR: {}".format(reason))
    return render_template('csrf_error.json', reason=reason), 400


# add api views
from views.index import IndexView
api.add_resource(IndexView, '/api/index')


# add template views
@app.route('/')
def index():
    app.logger.debug("Requested index")
    return render_template('index.html')
