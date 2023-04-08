"""
用户账户管理，包括用户的增删改查，addUser，deleteUser，updateUser，getUser
"""
from Function.SQLConnect import SQLConnect


class UserManager:
    def __init__(self):
        self.db = SQLConnect().connect()

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


