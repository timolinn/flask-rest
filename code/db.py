import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# user = (1, 'timolinn', 'fabby')
# create_user = "INSERT INTO users VALUES (?,?,?)"
# cursor.execute(create_user, user)

connection.commit()

connection.close()