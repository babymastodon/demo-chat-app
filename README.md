# Chat Web Application

This is a simple chat web application built with **Python (Flask)** and **JavaScript**. It allows users to log in with just a username (no password) and chat with a bot that responds with polite, vague, pre-defined answers. The chat history is stored in a **SQLite** database, allowing users to resume their conversation when they log back in.

## Features
- Username-only login
- Persistent chat history stored in SQLite
- Bot replies with random, polite responses from a pre-defined list
- Responsive UI styled with Bootstrap

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite
- **Deployment**: Render-compatible (via Gunicorn & Procfile)

## Directory Structure
```
.
├── app.py
├── requirements.txt
├── Procfile
├── templates
│   ├── login.html
│   └── chat.html
└── static
    ├── chat.js
    └── style.css
```

## Getting Started

### Prerequisites
- Python 3.x installed

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
1. Set the Flask app environment variable:
   ```bash
   export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
   ```

2. Start the Flask development server:
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000/`.

3. (Optional) Run with Gunicorn (for production-like environment):
   ```bash
   gunicorn app:app
   ```
   By default, Gunicorn runs on `http://127.0.0.1:8000/`.

### Deployment on Render
1. Push your project to a Git repository (GitHub, GitLab, etc.).
2. Create a new **Web Service** on Render.
3. Connect your repository.
4. Set the **Build Command** to:
   ```bash
   pip install -r requirements.txt
   ```
5. Set the **Start Command** to:
   ```bash
   gunicorn app:app
   ```
6. Choose your preferred region and deploy!

## License
This project is licensed under the MIT License.

---

Feel free to customize or expand this project as needed!
