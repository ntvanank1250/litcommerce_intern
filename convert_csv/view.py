
from customers import *
from convert_to_sql import *

menu_file=["1.Import data", "2.Upload data"]

def data():
    for i in menu_file:
        print(i)   
    x=int(input(""))
    if x==1:
        readfilecsv()
    elif x==2:
       create_customer()

if __name__=="__main__":
    data()
