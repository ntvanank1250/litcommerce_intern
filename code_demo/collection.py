import json
import shopify
import requests

shop_url = "https://%s:%s@hieuduy.myshopify.com/admin/api/2022-04/" % ('dad4dcdbd9cd059f260a5e8f09a55634', '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')
def create_customCollection():
    endpoint="custom_collections.json"
    payload={
       "custom_collection":{
            "title":"Macbook",
        }
    }
    r = requests.post( shop_url +endpoint, json=payload)
    print(r.json)
    return
def create_smartCollection():
    endpoint= "smart_collections.json"
    payload={
       "smart_collection":{
            "title":"Ipod",
            "rules":[{"column":"title",
                "relation":"starts_with",
                "condition":"iPod"}]
        }
    }
    r = requests.post( shop_url +endpoint, json=payload)
    print(r.json)
    return

def del_custom_collections(collectionID):
    endpoint=f"custom_collections/{collectionID}.json"
    r = requests.delete( shop_url +endpoint)
    print(r.json)
    return

def del_smart_collections(collectionID):
    endpoint=f"smart_collections/{collectionID}.json"
    r = requests.delete( shop_url +endpoint)
    print(r.json)
    return

