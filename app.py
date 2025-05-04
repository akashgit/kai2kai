from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
import json
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generate a random secret key
socketio = SocketIO(app)

# Store the latest location and sharing state
latest_location = None
is_sharing = False

# Simple user credentials (in production, use a proper database)
USERS = {
    'admin': 'password123'  # Change this to your desired password
}

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
    global is_sharing
    is_sharing = False
    emit('sharing_state_changed', {'is_sharing': False}, broadcast=True)

@socketio.on('connect')
def handle_connect():
    # Send the latest location and sharing state to newly connected clients
    if latest_location:
        emit('location_updated', latest_location)
    emit('sharing_state_changed', {'is_sharing': is_sharing})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5001) 