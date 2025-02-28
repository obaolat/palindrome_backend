from app import app, db  # Import app and db from your app module
from flask_migrate import MigrateCommand
from flask_script import Manager

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
