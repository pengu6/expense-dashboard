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


def get_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute('SELECT * FROM expenses')
    expenses = c.fetchall()
    conn.close()
    return expenses


def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()

    c.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()