"""
用户账户管理，包括用户的增删改查，addUser，deleteUser，updateUser，getUser
"""
from Function.SQLConnect import SQLConnect


class UserManager:
    def __init__(self):
        self.sql = SQLConnect()
        self.db = self.sql.connect()

    def add_User(self, username, password, Permissions):
        """
        添加用户
        :param username:
        :param password:
        :param Permissions:
        :return: bool: True or False
        """
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO Users (UserName, UserPassword, UserPermissions) VALUES (%s, %s, %s)",
                       (username, password, Permissions))
        try:
            self.db.commit()
            self.db.close()
            return True
        except:
            self.db.rollback()
            self.db.close()
            return False

    def load_data(self):
        """
        从数据库中读取数据,以元组的形式返回
        :return:
        """
        # 使用cursor()方法获取操作游标

        cursor = self.db.cursor()
        # 执行查询
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        self.db.close()
        return rows

    def delete_User(self, username, password):
        """
        删除用户,需要用户名和密码一致
        :param username:
        :param password:
        :return:
        """
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM Users WHERE UserName = %s AND UserPassword = %s", (username, password))
        try:
            self.db.commit()
            self.db.close()
            return True
        except:
            self.db.rollback()
            self.db.close()
            return False

    def change_User(self, username, password, newPassword, Permissions):
        """
        修改用户信息,需要用户名和旧密码一致
        :param username:
        :param password:
        :param newPassword:
        :param Permissions:
        :return:
        """
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE Users SET UserPermissions = %s, UserPassword = %s WHERE UserName = %s AND UserPassword = %s",
            (Permissions, newPassword, username, password))
        try:
            self.db.commit()
            self.db.close()
            return True
        except:
            self.db.rollback()
            self.db.close()
            return False
