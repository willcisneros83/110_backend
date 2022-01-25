
from flask import Flask, request, abort
from mock_data import catalog
import json  
import random 
from config import db 
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) # *DANGER* anyone can connect to this server

me = {
        "name": "Will",
        "last": "Cisneros",
        "age": 38,
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city": "Springfield"
        }
    }

@app.route("/")
def home():
    return "Hello from Python"

@app.route("/test")
def any_name():
    return "I'm a test function."

# return the full naame getting the values from the dictionary
@app.route("/about")
def about():
    return me["name"] + " " + me["last"]




# ***************************************************************
# ********************* API ENDPOINTS ***************************
# ***************************************************************



@app.route("/api/catalog")
def get_catalog():
    test = db.products.find({})
    print(test)

    return json.dumps(catalog)



@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json() 
    print (product)

    if not 'title' in product or len(product["title"]) < 5:
        return abort(400, "Title is required, and should be at least 5 chars long")


    if not "price" in product:
        return abort(400, "Price is required")

    if not isinstance(product["price"], float) and not isinstance(product["price"], int):
        return abort(400, "Price should be a valid number")



    if product["price"] <= 0:
        return abort(400, "Price should be greater than zero")


    
    db.products.insert_one(product)

    print("-----Saved-----")
    print(product)


    return json.dumps(product) 



@app.route("/api/cheapest")
def get_cheapest():
    # find the cheapest product on the catalog list   
    cheap = catalog[0]
    for product in catalog:
        if product["price"] < cheap["price"]:
            cheap = product 
        
    # return it as json
    return json.dumps(cheap)


@app.route("/api/products/<id>")
def get_product(id):
    # find the product whose _id is equal to id
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    # return as json
    return "Not Found"



# endpoint to retreive all the products by category
@app.route("/api/catalog/<category>")
def get_by_category(category):
    result = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:
            result.append(product)
            
            
    return json.dumps(result)






@app.route("/api/categories")
def get_categories():
    result = []
    for product in catalog:
        cat = product["category"]

        if cat not in result:
            result.append(cat)

    return json.dumps(result)


#  Get /api/reports/prodCount
@app.route("/api/reports/prodCount")
def get_prod_count():
    count = len(catalog) 
    return json.dumps(count)




@app.route("/api/reports/total")
def get_total():
    total = 0 

    for prod in catalog:
        totalProd = prod["price"] * prod["stock"]
        total += totalProd

    return json.dumps(total)





@app.route("/api/reports/highestInvestment")
def get_highest_investment():
    highest = catalog[0]

    for prod in catalog:
        prod_invest = prod["price"] * prod["stock"]
        high_invest =highest["price"] * highest["stock"]

        if prod_invest > high_invest:
            highest = prod



    return json.dumps(highest)





#  start the server 
app.run(debug=True)
