# Major Groove

A minimal web application built with Flask, SQLAlchemy, HTMX, and Alpine.js.

## Features

- Flask backend with SQLAlchemy for database management
- HTMX for dynamic content loading
- Alpine.js for reactive UI components
- Live reload during development
- SQLite database
- Minimal and clean UI with Tailwind CSS
- Blueprint-based route organization
- Application factory pattern

## Setup

1. Create a virtual environment:
```bash
python3.13 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

### nupack
```bash
cd third_party
cd nupack-4.x.x.x
pip install -U nupack -f package
```

**Note:** your venv needs to use a python version for which nupack has been packaged (e.g. `package/nupack-4.0.2.0-cp313...` is for Python 3.13).

### The rest

```bash
pip install -r requirements.txt
```

### In production

In production environment (e.g. RNA), run:

```bash
pip install -r requirements-prod.txt
```


3. Run the application:
```bash
python app.py
```

The application will be available at http://localhost:5002

## Development

The application includes live reload functionality, so any changes to templates or static files will automatically refresh the browser.

## Project Structure

```
.
├── app/                    # Application package
│   ├── __init__.py        # Application factory
│   ├── routes/            # Route blueprints
│   │   ├── __init__.py
│   │   └── main.py        # Main routes
│   ├── static/            # Static files (CSS, JS, images)
│   └── templates/         # Jinja2 templates
│       ├── base.html      # Base template
│       └── main/          # Templates for main blueprint
│           └── index.html # Home page template
├── app.py                 # Application entry point
├── requirements.txt       # Python dependencies
└── site.db               # SQLite database (created on first run)
``` # majorgroove
