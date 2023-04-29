"""
使用PyMySQL连接数据库,并返回数据库对象
"""

import pymysql


class SQLConnect:
    def __init__(self):
        self.db = pymysql.connect(host='sh-cynosdbmysql-grp-lhkebs8k.sql.tencentcdb.com',
                                  user='ywyz',
                                  password=' ',
                                  database='KinderGarten',
                                  port=21654)

    def connect(self):
        return self.db

    def close(self):
        self.db.close()
