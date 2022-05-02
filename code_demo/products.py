import json
from operator import index
from turtle import pos
import shopify
import requests

shop_url = "https://%s:%s@hieuduy.myshopify.com/admin/api/2022-04/" % ('dad4dcdbd9cd059f260a5e8f09a55634', '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')
shopify.ShopifyResource.set_site(shop_url)
# get all products
def get_products():
    endpoint= 'products.json'
    r = requests.get( shop_url +endpoint)
    return r.json()

def get_product(productID):
    endpoint= f'products/{productID}.json'
    r = requests.get( shop_url +endpoint)
    return r.json()

#change price product
def change_productsPrice(product_id,price):
    payload={
                "product" : {
                    "variants" : [{
                        "price" : price
                        }]
                }
        }
    endpoint=f"products/{product_id}.json"
    r = requests.put( shop_url +endpoint, json=payload)
    # print(r.json())
    return
#chang link image product
def change_productsImage(product_id,image):
    payload={
                "product" : {
                    "images" : [{
                        "src" : image
                        }]
                }
        }
    endpoint=f"products/{product_id}.json"
    r = requests.put( shop_url +endpoint, json=payload)
    # print(r.json())
    return
    
#create products (title,body_html,product_type,tags)
def create_products(title,body_html,vendor,product_type,tags):
    endpoint= 'products.json'
    payload= {
    "product":{
        "title":title,
        "body_html":body_html,
        "vendor":vendor,
        "product_type":product_type,
        "tags":tags
        }
    }
    r = requests.post( shop_url +endpoint, json=payload)
    print(r.json)
    return
def add_product_option(product_id):
    endpoint=f"products/{product_id}.json"
    option = {
    'name': 'color',
    'product_id': product_id,
    'values': ['blue', 'red']}
    variant = {
        'product_id': product_id,
        'title': '',
        'sku': '',
        'price': '',
        'compare_at_price': '',
        'weight': 0,
        'cost': 0,
        'inventory_policy': '',
        'inventory_management': '',
        'taxable': False
}
    payload={"product":{"variants":variant,
                        "options":option}}
    print(payload)
    r = requests.put(shop_url +endpoint, json=payload)
    print(r.json)
    return

def del_product(productID):
    endpoint=f"products/{productID}.json"
    r = requests.delete( shop_url +endpoint)
    print(r.json)
    return
