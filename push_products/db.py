import csv
from sqlalchemy import null
import mysql.connector
from datetime import datetime
def convertDatetime(a):
    date_time_str = a
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
    return date_time_obj

class SQL:
    def __init__(self):
        self.__dbProvider = DBProvider()
    def listrow(self):
        sql="""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = 'products'
            ORDER BY ORDINAL_POSITION
            """
        x = DBProvider().get_data(sql)
        result=[]
        for i in x:
            result.append(i[0])
        return result
    def getData(self):
        x=self.listrow()
        sql = f"""
            SELECT *
            FROM products
        """
        return DBProvider().get_data(sql)
    def get_All(self):
        products = self.getData()
    
        listKey =self.listrow()
        list=[]
        
        
        for pro in products:
            i=0
            dict={}
            for keys in listKey:    
                dict[keys]=pro[i]
                i+=1
            
            list.append(dict)
        return list
class DBProvider:
    # Khoi tao thong tin MySQL
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "1250"
        self.db = "world"
        self.connects = None
        self.cursors = None
    

    # Ket noi toi MySQL
    def connect(self):
        try:
            self.connects = mysql.connector.connect(host=self.host,
                                                user=self.user,
                                                passwd=self.passwd,
                                                db=self.db)
            self.cursors = self.connects.cursor()
        except:
            print("Không thể kết nối tới database")
    # Dong ket noi
    def close(self):
        try:
            if self.connects is not None:
                self.connects.close()
                self.connects = None
                self.cursors = None
        except:
            print("Không thể đóng database")

    # Get many => Lay nhieu ban ghi thành 1 cái tuple trong list
    def get_data(self, sql: str, *params):
        self.connect()
        self.cursors.execute(sql, *params)
        result = [row for row in self.cursors.fetchall()]
        self.close()
        return result
    #ghi vao database
    def add_data(self, sql, *params):
            rowCount = 0
            try:
                self.connect()
                self.cursors.execute(sql, *params)
                self.connects.commit()
                rowCount = self.cursors.rowcount
            except Exception as e:
                print(e)
            finally:
                self.close()
            return rowCount

# if __name__ == "__main__":
#     SQL().get_All()
