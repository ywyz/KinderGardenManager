from Function.SQLConnect import SQLConnect


class Login:
    def __init__(self):
        self.db = SQLConnect().connect()

    def login(self, username, password):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserName = %s AND UserPassword = %s", (username, password))
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False

    def close(self):
        self.db.close()
