"""
使用Login类进行登录，Login类中的login方法返回True或False，表示登录成功或失败
"""

from Function.SQLConnect import SQLConnect


class Login:
    def __init__(self):
        self.db = SQLConnect().connect()

    def login(self, username, password):
        if (username == "" or password == ""):
            return False
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserName = %s AND UserPassword = %s", (username, password))
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False

    def close(self):
        self.db.close()
