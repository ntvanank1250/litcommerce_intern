import json
import shopify
import requests
from sqlalchemy import true
from db import *

shop_url = "https://%s:%s@doduyhieu.myshopify.com/admin/api/2022-04/" % ('0fee9ce3f8b7aab133a414adfc0e3311', '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')
def push_products():
    products= SQL().get_All()
    
    for pro in products:
        payload={               
             "product": {
                "title": pro["name"],
                "body_html": pro["description"],
                "vendor": pro["distributor"],
                "status": "active",
                "tags": pro["metatags"],
                "variants": [{
                        "title": pro["name"],
                        "price": pro["price"],
                        "sku": pro["SKU"],
                        "option1": "Default Title",
                        "weight": pro["weight"]
                    }]
                }}
        endpoint="products.json"
        print(payload)
        r = requests.post(shop_url + endpoint, json=payload)
        print(r.text)
    return 
class getcustomer:
    def __init__(self):
        self.DBProvider = DBProvider()

    def openScreen(self):
        result = self.DBProvider.get_data()
        print(result)
        return result
