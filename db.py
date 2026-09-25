import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(amount, category, date, note):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO expenses (amount, category, date, note)
        VALUES (?, ?, ?, ?)
    ''',
    (amount, category, date, note))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    add_expense(12.50, "Food", "2026-09-25", "lunch")