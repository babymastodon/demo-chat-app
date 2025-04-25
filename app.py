from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3
import os
import random

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'super-secret-key')
DB_PATH = 'chat.db'

# Hard-coded bot responses
BOT_RESPONSES = [
    "That’s interesting—tell me more.",
    "I hadn’t thought of it that way before.",
    "Can you elaborate on that?",
    "That makes sense in a way.",
    "What do you think about it now?",
    "I see your point.",
    "How does that make you feel?",
    "Let’s explore that further.",
    "Why do you say that?",
    "That’s a good question.",
    "Could you give me an example?",
    "What else comes to mind?",
    "That sounds like a plan.",
    "I’m curious—what happened next?",
    "Interesting perspective.",
    "Tell me more about that.",
    "How would you compare it?",
    "What leads you to believe that?",
    "Let’s dive deeper.",
    "That’s quite thoughtful."
]

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            sender TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        if username:
            session['username'] = username
            return redirect(url_for('chat'))
    return render_template('login.html')

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    # Load chat history
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT sender, content, timestamp FROM messages WHERE username = ? ORDER BY timestamp', (username,))
    history = c.fetchall()
    conn.close()
    return render_template('chat.html', username=username, history=history)

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'username' not in session:
        return jsonify({'error': 'Not logged in'}), 403
    data = request.get_json()
    user_msg = data.get('message', '').strip()
    username = session['username']
    if not user_msg:
        return jsonify({'error': 'Empty message'}), 400
    # Save user message
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO messages (username, sender, content) VALUES (?, ?, ?)',
              (username, 'user', user_msg))
    # Pick a random bot response
    bot_msg = random.choice(BOT_RESPONSES)
    c.execute('INSERT INTO messages (username, sender, content) VALUES (?, ?, ?)',
              (username, 'bot', bot_msg))
    conn.commit()
    conn.close()
    return jsonify({'response': bot_msg})

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
