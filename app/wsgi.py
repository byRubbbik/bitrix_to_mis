import sys
import os

# Add your project directory to the sys.path
project_home = os.path.dirname(__file__)
if project_home not in sys.path:
    sys.path.append(project_home)

# Import the Flask app, but name it "application" for WSGI to work
from app import app as application