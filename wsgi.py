import sys
import os

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/location-share'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['FLASK_SECRET_KEY'] = 'your-secret-key-here'  # You'll change this in PythonAnywhere
os.environ['ADMIN_USERNAME'] = 'admin'  # You'll change this in PythonAnywhere
os.environ['ADMIN_PASSWORD'] = 'your-password-here'  # You'll change this in PythonAnywhere

# Import your Flask app
from app import app as application 