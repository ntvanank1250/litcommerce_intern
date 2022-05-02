import json
import shopify
import requests

shop_url = "https://%s:%s@hieuduy.myshopify.com/admin/api/2022-04/" % ('dad4dcdbd9cd059f260a5e8f09a55634', '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')
def create_order():
    endpoint="orders.json"
    payload={"order":{
            "email":"steve.lastnameson@example.com",
            "fulfillment_status":"fulfilled",
            "send_receipt":True,
            "send_fulfillment_receipt":True,
            "line_items":[{
                "variant_id":41823414747336,
                "quantity":1}]}}
    
    r = requests.post( shop_url +endpoint, json=payload)
    print(r.json)
    return
def del_order(oderID):
    endpoint=f"orders/{oderID}.json"
    r = requests.delete( shop_url +endpoint)
    print(r.json)
    return
