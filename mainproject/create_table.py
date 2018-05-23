import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_users_table)

create_items_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_items_table)

# user = (1, 'timolinn', 'fabby')
# create_user = "INSERT INTO users VALUES (?,?,?)"
# cursor.execute(create_user, user)

connection.commit()

connection.close()