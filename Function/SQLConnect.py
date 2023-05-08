"""
使用PyMySQL连接数据库,并返回数据库对象
"""

import pymysql
from PyQt6.QtWidgets import QFileDialog, QWidget
import os


class SQLConnect:
    def __init__(self):
        self.db = pymysql.connect()

    def connect(self):
        return self.db

    def close(self):
        self.db.close()

    def commit_students_info(self, lists):
        if lists is None:
            pass
        cursor = self.db.cursor()
        sql_commit = "INSERT INTO StudentsBasicInfo (StudentName, StudentIDNum, PlaceOfAccount, \
                        PlaceOfCurrent, PlaceOfBirth, Nationality, Class, EthnicGroup, Sex, IsHKMcTW, IsOnlyChild, \
                        HealthStatus, HowToEnroll, BloodType, IsOrphan, isMinLiving, StudentIDType, isLeftBehind, IsHandicapped,\
                        BirthDate, IntoKindergarten, NameofGuardian, relationShipofGuardian ,GuardianIDType, GuardianIDNum, GuardianBirthDate, \
                       GuardianSex,IsLegalGuardian, ContactAddress, WorkPlace, Position, GuardianNationality, Telephone, \
                       GuardianGroup) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                       %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        StudentName = lists[0]
        StudentIDNum = lists[1]
        PlaceOfAccount = lists[2]
        PlaceOfCurrent = lists[3]
        PlaceOfBirth = lists[4]
        Nationality = lists[5]
        Class = lists[6]
        EthnicGroup = lists[7]
        Sex = lists[8]
        IsHKMcTW = lists[9]
        IsOnlyChild = lists[10]
        HealthStatus = lists[11]
        HowToEnroll = lists[12]
        BloodType = lists[13]
        IsOrphan = lists[14]
        isMinLiving = lists[15]
        StudentIDType = lists[16]
        isLeftBehind = lists[17]
        IsHandicapped = lists[18]
        BirthDate = lists[19]
        IntoKindergarten = lists[20]
        NameofGuardian = lists[21]
        relationShipofGuardian = lists[22]
        GuardianIDType = lists[23]
        GuardianIDNum = lists[24]
        GuardianBirthDate = lists[25]
        GuardianSex = lists[26]
        IsLegalGuardian = lists[27]
        ContactAddress = lists[28]
        WorkPlace = lists[29]
        Position = lists[30]
        GuardianNationality = lists[31]
        Telephone = lists[32]
        GuardianGroup = lists[33]

        cursor.execute(sql_commit,
                       (StudentName, StudentIDNum, PlaceOfAccount, PlaceOfCurrent, PlaceOfBirth, Nationality,
                        Class, EthnicGroup, Sex, IsHKMcTW, IsOnlyChild, HealthStatus, HowToEnroll, BloodType,
                        IsOrphan, isMinLiving, StudentIDType, isLeftBehind, IsHandicapped, BirthDate,
                        IntoKindergarten, NameofGuardian, relationShipofGuardian, GuardianIDType,
                        GuardianIDNum, GuardianBirthDate, GuardianSex, IsLegalGuardian,
                        ContactAddress, WorkPlace, Position, GuardianNationality,
                        Telephone, GuardianGroup))
        try:
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False


    def Export_Data(self):
        widget = QWidget()
        # 获得包含文件路径+文件名的元组
        # 例如：('C:/Users/lenovo/Desktop/1.txt', 'All Files (*)')
        filename, filetype = QFileDialog.getSaveFileName(QWidget(), "选择保存文件名", "./", "sql Files (*.sql)")
        user = 'ywyz'
        password = 'YUEwei980924'
        host = 'sh-cynosdbmysql-grp-lhkebs8k.sql.tencentcdb.com'
        port = 21651
        db = 'KinderGarten'
        # 调用cmd命令导出数据库
        cmd = f"mysqldump --column-statistics=0 -u{user} -p{password} -h{host} -P{port} {db} > {filename}"
        os.system(cmd)
        return True
