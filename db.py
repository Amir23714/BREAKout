import sqlite3 as sq

'''Create the database and the table if they don't exist'''
with sq.connect('BD_database.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    TG_user_id INTEGER,
    api_key TEXT,
    secret_key TEXT)""")

'''The function, which adds the user to the database'''
def add_user(TG_user_id, api_key, secret_key):
    with sq.connect('BD_database.db') as con:
        cur = con.cursor()
        cur.execute(f"""INSERT INTO users(TG_user_id, api_key, secret_key)
        VALUES({TG_user_id}, '{api_key}', '{secret_key}')""")
        con.commit()
'''The function, which returns the api_key and secret_key of the user'''
def get_user(TG_user_id):
    with sq.connect('BD_database.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT api_key, secret_key FROM users WHERE TG_user_id = {TG_user_id}""")
        return cur.fetchone()



