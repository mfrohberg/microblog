# Setting The Path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

# Turns on debugger and reloader by default
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = '29770')
)

if __name__ == '__main__':
    manager.run()
