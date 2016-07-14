API_PORT = 8080
API_BIND_ADDRESS = 'localhost'
API_WORKERS = 2

DEBUG = True
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Database settings
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.sqlite'
