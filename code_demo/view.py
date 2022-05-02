
from __init__ import *
from customers import *

menu_create=["1.Create Collection","2.Create Product", "3.Create Customer", "4.Create Order"]
menu_update=["1.Update Price","2.Update Image"]
menu_delete=["1.Delete Order","2.Delete product", "3.Delete Custom Collection","4.Delete Smart Collection"]
menu_file=["1.Import data", "2.Upload data"]
def create():
    for i in menu_create:
        print(i)   
    x=int(input(""))
    if x==1:
        create_smartCollection()
        create_customCollection()
    elif x==2:
        title=input("title:")
        body_html="<strong>"+input("body_html:")+"</strong>"
        vendor=input("vendor:")
        product_type=input("product_type:")
        tags=input("tags:")
        y=["Option:","1.No option", "2.+1 option"]
        create_products(title,body_html,vendor,product_type,tags)
        while True:
            for i in y:
                print(i)
            z=int(input(""))
            
            if z==1:
                return
            elif z==2:
                # option=input("option:")
                products=get_products()
                add_product_option(products["products"][len(products)]["id"])
            
    elif x==3:
        create_customer()
    elif x ==4:
        create_order()
def update():
    for i in menu_update:
        print(i)   
    x=int(input(""))
    if x==1:
        change_productsPrice()
    elif x==2:
       change_productsImage()
def delete():
    for i in menu_delete:
        print(i)   
    x=int(input(""))
    if x==1:
        del_order()
    elif x==2:
        del_product()
    elif x==3:
        del_custom_collections()
    elif x ==4:
        del_smart_collections()

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
