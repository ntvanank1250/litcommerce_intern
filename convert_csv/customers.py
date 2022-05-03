import json
import shopify
import requests
from sqlalchemy import true
from convert_to_sql import *

shop_url = "https://%s:%s@doduyhieu.myshopify.com/admin/api/2022-04/" % ('0fee9ce3f8b7aab133a414adfc0e3311', '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')
def create_customer():
    data= SQL().getAll()
    for cus in data:
        payload={               
            "customer":{
                "first_name": f"{cus[1]}",
                "last_name": f"{cus[2]}",
                "email":f"{cus[11]}",
                
                "addresses" : [{
                    "company": f"{cus[3]}",
                    "city": f"{cus[6]}",
                    "address1": f"{cus[4]}",
                    "address2": f"{cus[5]}",
                    "country": f"{cus[9]}",
                    "phone":f"{cus[10]}",
                    "zip": f"{cus[8]}",
                    "last_name": f"{cus[2]}",
                    "first_name": f"{cus[1]}",
                        }]
                }}
        endpoint="customers.json"
        r = requests.post( shop_url + endpoint, json=payload)
        print(r.text)
    return 
class getcustomer:
    def __init__(self):
        self.DBProvider = DBProvider()

    def openScreen(self):
        result = self.DBProvider.get_data()
        print(result)
        return result
