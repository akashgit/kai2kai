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

## Deployment

This application can be deployed for free using Render.com:

1. Create a Render account at https://render.com
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure the following environment variables in Render:
   - `FLASK_SECRET_KEY`
   - `ADMIN_USERNAME`
   - `ADMIN_PASSWORD`
5. Deploy!

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