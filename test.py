from flask import Flask, request, jsonify
from Products import Products
from pymongo import MongoClient


# Mongo database
client = MongoClient('mongodb://Alejandra:comecaca@localhost:27017')
# Product database
pr_db = client["Product"]
# Product table
pr_col = pr_db["products"]

app = Flask(__name__)
s
@app.route('/products', methods=['GET', 'POST'])
def list_products():
    # Get all the products
    if request.method == 'GET':
        products = []
        # Check if there are products in the table
        if pr_col.find:
            for pr in pr_col.find():
                products.append({'name' : pr['name'], 'due_date' : pr['due_date']})
        return jsonify({'result': products})
    
    # Insert product
    elif request.method == 'POST':
        body = request.get_json()
        if body:
            pr = pr_col.insert_one(body)
            return 'Product id ' + str(pr.inserted_id) + ' sucessfully created.'
        else: 
            return 'Insert the product.'

if __name__== "__main__" :
    app.run(host='0.0.0.0', port='8000')