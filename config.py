import os
from tempfile import mkdtemp

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Ensure templates are auto-reloaded
TEMPLATES_AUTO_RELOAD = True
DEBUG = True

# Configure session to use filesystem (instead of signed cookies)
SESSION_FILE_DIR = mkdtemp()
SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
ENV = 'DEV'
INIT_DATA = True