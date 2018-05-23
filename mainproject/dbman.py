import sqlite3

class DBMan:
    def __init__(self):
        self.connection = sqlite3.connect("data.db")

    def select_many(self, sql, *args):
        cursor = self.connection.cursor()
        res = cursor.executemany(sql, (*args,))
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
        result = self.runquery(sql, *args)
        if result:
            self.connection.commit()
            self.connection.close()
            return True

    def delete(self, sql, *args):
        cursor = self.connection.cursor()
        res = cursor.execute(sql, (*args,))

        self.connection.close()

        return res

    def runquery(self, sql, *args):
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, (*args,))
        except:
            return False

        return True

    def update(self, sql, *args):
        result = self.runquery(sql, *args)
        if result:
            self.connection.commit()
            self.connection.close()
            return True