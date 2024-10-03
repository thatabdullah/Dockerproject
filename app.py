from flask import Flask
import psycopg2


app = Flask(__name__)
def get_db_connection():
    conn = psycopg2.connect(
    host="db",
    database="test_db",
    user="postgres",
    password="password"
)
    return conn
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Database connected: {db_version}'
if __name__ == '__main__':
    app.run()