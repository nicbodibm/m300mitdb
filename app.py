from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Pfad zur SQLite-Datenbankdatei
db_file = os.path.join('database', 'products.db')

# Verbindung zur SQLite-Datenbank herstellen
def get_db_connection():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

# Index-Seite definieren
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, price, image_path FROM products')
    rows = cursor.fetchall()
    conn.close()

    return render_template('index.html', products=rows)

# Datenbanktabelle erstellen (falls sie nicht existiert)
def create_table():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Beispiel-Datensätze einfügen (falls Tabelle leer ist)
def insert_example_data():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM products')
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute('''
            INSERT INTO products (name, price, image_path) VALUES
            ('Lenovo Laptop', 400.0, 'lenovo.jpg'),
            ('Apple iPhone', 800.0, 'iphone.jpg'),
            ('Samsung TV', 1200.0, 'samsung.jpg'),
            ('Sony Camera', 600.0, 'sony.jpg')
        ''')
        conn.commit()

    conn.close()

# Ausführung der Funktionen beim Start der Anwendung
if __name__ == '__main__':
    if not os.path.exists('database'):
        os.makedirs('database')
    create_table()         # Tabelle erstellen (falls nicht existiert)
    insert_example_data()  # Beispiel-Datensätze einfügen (falls Tabelle leer ist)
    app.run(host='0.0.0.0', debug=True)
