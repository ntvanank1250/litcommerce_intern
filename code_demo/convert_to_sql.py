import csv
from sqlalchemy import null
import mysql.connector



def readfilecsv():
    with open("customer.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        x=0
        
        for rows in reader:
            row=rows[0].split(",")
            if x==0:
                x+=1
                continue
            else:
                
                print(row)
                SQL().insert_one_row(row)
            x+=1
        
        
class SQL:
    def __init__(self):
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        sql = """
            CREATE TABLE IF NOT EXISTS customer(
                customer_id VARCHAR(8) PRIMARY KEY ,
                firstname NVARCHAR(50),
                lastname NVARCHAR(50),
                companyname NVARCHAR(50),
                billingaddress1 NVARCHAR(100),
                billingaddress2 NVARCHAR(100),
                city VARCHAR(50),
                state varchar(10),
                postalcode varchar(15),
                country NVARCHAR(50),
                phonenumber NVARCHAR(50),
                emailaddress NVARCHAR(100),
                createddate DATETIME
            )
        """
        self.__dbProvider.add_data(sql)

    def insert_one_row(self, row):
        sql = """
            INSERT INTO customer(customer_id, firstname, lastname, companyname, billingaddress1, billingaddress2, city,state,postalcode,country,phonenumber,emailaddress,createddate)
            VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)
        """
        val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        return self.__dbProvider.add_data(sql, val)

    def getAll(self):
        sql = """
            SELECT Code, FullName, Birthday, Sex, Address, Phone, Email
            FROM Student
        """
        return DBProvider().get_data(sql)


    
class DBProvider:
    # Khoi tao thong tin MySQL
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "1250"
        self.db = "mydatabase"
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
    def add_data(self, sql: str, *params):
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

