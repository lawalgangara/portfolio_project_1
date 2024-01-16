# __init__.py

from app.create_app import create_app

app = create_app()

# Import routes or other components here if needed
from app.routes.root import *
