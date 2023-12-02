from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Create a SQLite database
conn = sqlite3.connect('feedback.db') 
c = conn.cursor()

# Create a feedback table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        question_1 TEXT,
        question_2 TEXT,
        question_3 TEXT,
        question_4 TEXT,
        question_5 TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('feedback.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()

        # Retrieve user information & answers from the form
        name = request.form['name']
        email = request.form['email']
        question_1 = request.form['question_1']
        question_2 = request.form['question_2']
        question_3 = request.form['question_3']
        question_4 = request.form['question_4']
        question_5 = request.form['question_5']

        # Insert answers into the database
        c.execute('INSERT INTO feedback (name, email, question_1, question_2, question_3, question_4, question_5) VALUES (?, ?, ?, ?, ?, ?, ?)',
                  (name, email, question_1, question_2, question_3, question_4, question_5))

        conn.commit()
        conn.close()

        return "Feedback submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)