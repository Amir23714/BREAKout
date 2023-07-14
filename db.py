import sqlite3 as sq


with sq.connect('BD_database.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    TG_user_id INTEGER,
    api_key TEXT,
    secret_key TEXT)""")

def add_user(TG_user_id, api_key, secret_key):
    with sq.connect('BD_database.db') as con:
        cur = con.cursor()
        cur.execute(f"""INSERT INTO users(TG_user_id, api_key, secret_key)
        VALUES({TG_user_id}, '{api_key}', '{secret_key}')""")
        con.commit()

def get_user(TG_user_id):
    with sq.connect('BD_database.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT api_key, secret_key FROM users WHERE TG_user_id = {TG_user_id}""")
        return cur.fetchone()

if __name__ == '__main__':

    add_user(1, "3w", "w4")
    add_user(4, "w2", "q5")
    print(get_user(1))



