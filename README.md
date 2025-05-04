# Location Share

A simple web application that allows users to share their real-time location with others. Built with Python Flask and WebSocket for real-time updates.

## Features

- Real-time location sharing
- Simple authentication system
- Interactive map interface using OpenStreetMap
- WebSocket-based real-time updates
- Mobile-friendly design

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd location-share
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with the following variables:
```bash
FLASK_SECRET_KEY=your-secret-key-here
ADMIN_USERNAME=your-username
ADMIN_PASSWORD=your-password
```

Replace the values with your desired credentials. The `FLASK_SECRET_KEY` should be a random string for security.

## Running the Application

1. Start the server:
```bash
python app.py
```

2. Access the application:
- Open a web browser and go to `http://localhost:5001`
- Log in with your credentials
- Click "Start Sharing Location" to begin sharing your location
- Others can view your location by accessing the same URL and logging in

## Security Notes

This is a basic implementation with simple authentication. For production use, consider:
- Using a proper database for user management
- Implementing HTTPS
- Adding more robust security measures
- Never commit the `.env` file to version control
- Use strong, unique passwords
- Regularly rotate credentials

## License

MIT License

## Contributing

Feel free to submit issues and pull requests. 