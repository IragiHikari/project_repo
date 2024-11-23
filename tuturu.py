from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, first_name TEXT, last_name TEXT)')
    cursor.execute('INSERT INTO users VALUES (1, "John", "Doe")')
    conn.commit()
    conn.close()

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')

    # Validate input
    if not user_id.isdigit():
        return jsonify({"error": "Invalid ID"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Prepared statement to prevent SQL injection
    cursor.execute("SELECT first_name, last_name FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({"first_name": user[0], "last_name": user[1]})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
