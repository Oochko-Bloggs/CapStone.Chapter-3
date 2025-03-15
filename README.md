# GitHub Codespaces ♥️ Flask

Welcome to our shiny new project with Codespace running Flask!

To run this application:

```
flask --debug run
```

### Directory structure model

```
ctf-platform/
│── app/                # Main application folder
│   ├── static/         # CSS, JavaScript, Images
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── main.js
│   ├── templates/      # HTML Templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   ├── routes/         # App routes
│   │   ├── auth.py     # Login, Logout, Register
│   │   ├── challenges.py # Challenge system
│   │   ├── scoreboard.py # Live scoreboard
│   ├── models.py       # Database models
│   ├── __init__.py     # App initialization
│── migrations/         # Database migrations (if using Flask-Migrate)
│── instance/           # Instance config (for secrets)
│── tests/              # Unit tests
│── config.py           # Configuration file
│── run.py              # Entry point
│── requirements.txt    # Python dependencies
│── .env                # Environment variables
│── README.md           # Documentation

```

### If you want to change the database modify the models.py and run the migration script 

```
flask db migrate -m "Some comments here to let you partner know what happend"
```

