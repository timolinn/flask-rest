import sqlite3

class DBMan:
    def __init__(self):
        self.connection = sqlite3.connect("data.db")

    def select_many(self, sql, *args):
        cursor = self.connection.cursor()
        res = cursor.execute(sql, (*args,))
        results = res.fetchall()

        self.connection.close()

        return results

    def selectall(self, sql):
        cursor = self.connection.cursor()
        res = cursor.execute(sql)
        results = res.fetchall()

        self.connection.close()

        return results

    ## Select one item from DB
    def select_one(self, sql, *args):
        cursor = self.connection.cursor()
        res = cursor.execute(sql, (*args,))
        results = res.fetchone()

        self.connection.close()

        return results

    def insert_one(self, sql, *args):
        cursor = self.connection.cursor()
        cursor.execute(sql, (*args,))

        self.connection.commit()
        self.connection.close()

    def delete(self, sql, *args):
        cursor = self.connection.cursor()
        res = cursor.execute(sql, (*args,))

        self.connection.close()

        return res