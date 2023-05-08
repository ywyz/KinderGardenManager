from Function.SQLConnect import SQLConnect
import requests


class BooksManager:
    def __init__(self):
        self.lists = None
        self.sql = SQLConnect()

    def on_query(self, isbn):
        url = 'https://api.jisuapi.com/isbn/query'
        params = {'appkey': '43e087590de8c74b', 'isbn': isbn}

        response = requests.get(url, params=params)
        data = response.json()
        return data

    def query_sql(self, isbn):
        sql = "select * from Books where isbn = '%s'" % isbn
        db = self.sql.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        return data

    def update_book(self, list1):
        print(list1)
        sql = "update Books set BooksName = '%s',Publisher = '%s',Author = '%s',Price = '%s',NowAddress = '%s'," \
              "num = '%s' where ISBN = '%s'" % (list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[0])
        db = self.sql.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()

    def add_book(self,list1):
        print(list1)
        sql = "INSERT INTO Books (ISBN,BooksName,Publisher,Author,Price,NowAddress,num) VALUES ('%s','%s','%s'," \
              "'%s','%s','%s','%s')" % (list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6])
        db = self.sql.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
