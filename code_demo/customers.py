import json
import shopify
import requests
from __init__ import *
from convert_to_sql import DBProvider

shop_url = "https://%s:%s@hieuduy.myshopify.com/admin/api/2022-04/" % ('dad4dcdbd9cd059f260a5e8f09a55634', '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')
def create_customer():
    data= DBProvider.get_data()
    for cus in data:
        payload={               
            "customer":{
                "email":f"{cus[11]}",
                "first_name": f"{cus[1]}",
                "last_name": f"{cus[2]}",
                "phone":f"{cus[10]}",
                "addresses" : [{
                    "company": f"{cus[3]}",
                    "address1": f"{cus[4]}",
                    "address2": f"{cus[5]}",
                    "city": f"{cus[6]}",
                    "country": f"{cus[9]}",
                    "zip": f"{cus[8]}",
                    "last_name": f"{cus[2]}",
                    "first_name": f"{cus[1]}",
                        }]
                }}
        endpoint="customers.json"
        r = requests.post( shop_url +endpoint, json=payload)
        print(r.json)
    return 
class getcustomer:
    def __init__(self):
        self.DBProvider = DBProvider

    def openScreen(self):
        result = self.DBProvider.get_data()
        print(result)
        return result
