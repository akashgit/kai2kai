# Location Share

A real-time location sharing application built with Flask and Socket.IO.

## Features

- Real-time location sharing
- Secure authentication
- Interactive map interface
- Start/Stop sharing controls
- Responsive design

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/akashgit/kai2kai.git
cd location-share
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your configuration:
```
FLASK_SECRET_KEY=your_secret_key_here
ADMIN_USERNAME=your_username
ADMIN_PASSWORD=your_password
```

5. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5001`

## Deployment on PythonAnywhere

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com)

2. Once logged in:
   - Go to the "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.11

3. Set up your virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.11 location-share
   pip install -r requirements.txt
   ```

4. Clone your repository:
   ```bash
   git clone https://github.com/akashgit/kai2kai.git
   ```

5. Configure your web app:
   - Set the working directory to `/home/YOUR_USERNAME/location-share`
   - Set the WSGI configuration file to `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`
   - Update the WSGI file with your project path and environment variables

6. Set up environment variables in the Web app configuration:
   - FLASK_SECRET_KEY
   - ADMIN_USERNAME
   - ADMIN_PASSWORD

7. Reload your web app

## Security Notes

- Always use HTTPS in production
- Use strong passwords
- Keep your `.env` file secure and never commit it to version control
- Consider implementing rate limiting for production use
- Use a proper database for user management in production

## License

Apache License 2.0

## Contributing

Feel free to submit issues and pull requests. 