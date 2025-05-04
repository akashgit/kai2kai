from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
import json
import secrets
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', secrets.token_hex(16))
# Configure Socket.IO for production
socketio = SocketIO(app, 
                   cors_allowed_origins="*",
                   async_mode='eventlet',
                   logger=True,
                   engineio_logger=True,
                   ping_timeout=60,
                   ping_interval=25,
                   max_http_buffer_size=1e8)

# Store the latest location and sharing state
latest_location = None
is_sharing = False

# Get credentials from environment variables
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'password123')

# Simple user credentials (in production, use a proper database)
USERS = {
    ADMIN_USERNAME: ADMIN_PASSWORD
}

def reset_sharing_state():
    global latest_location, is_sharing
    latest_location = None
    is_sharing = False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username] == password:
            session['authenticated'] = True
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Stop sharing when user logs out
    reset_sharing_state()
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('index.html')

@socketio.on('update_location')
def handle_location_update(data):
    global latest_location
    if not is_sharing:  # Only update location if sharing is active
        return
    latest_location = data
    # Broadcast the location to all connected clients
    emit('location_updated', data, broadcast=True)

@socketio.on('sharing_started')
def handle_sharing_started():
    global is_sharing
    is_sharing = True
    emit('sharing_state_changed', {'is_sharing': True}, broadcast=True)

@socketio.on('sharing_stopped')
def handle_sharing_stopped():
    reset_sharing_state()
    emit('sharing_state_changed', {'is_sharing': False}, broadcast=True)

@socketio.on('connect')
def handle_connect():
    # Send the latest location and sharing state to newly connected clients
    if latest_location and is_sharing:  # Only send location if sharing is active
        emit('location_updated', latest_location)
    emit('sharing_state_changed', {'is_sharing': is_sharing})

if __name__ == '__main__':
    # Use environment variable for port in production
    port = int(os.getenv('PORT', 5001))
    socketio.run(app, debug=False, host='0.0.0.0', port=port) 