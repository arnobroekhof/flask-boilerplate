#!/usr/bin/env python


from flask_script import Manager, Option, Command
from translogic import app, db
from gunicorn.app.base import Application
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def drop_db():
    db.drop_all()


class GunicornServer(Command):
    def __init__(self, host=app.config.get('API_BIND_ADDRESS', '127.0.0.1'), port=app.config.get('API_PORT', 8080),
                 workers=app.config.get('API_WORKERS', 4)):
        self.address = "{}:{}".format(host, port)
        self.workers = workers

    def get_options(self):
        return (
            Option('-b', '--bind',
                   dest='address',
                   type=str,
                   default=self.address),
            Option('-w', '--workers',
                   dest='workers',
                   type=int,
                   default=self.workers),
        )

    def __call__(self, *args, **kwargs):
        workers = kwargs['workers']
        address = kwargs['address']

        class FlaskApplication(Application):
            def init(self, parser, opts, args):
                return {
                    'bind': address,
                    'workers': workers
                }

            def load(self):
                return app

        FlaskApplication().run()


if __name__ == "__main__":
    manager.add_command('gunicorn_server', GunicornServer())
    manager.run()
