import requests

BASE_URL = "http://127.0.0.1:8000/api/products"

def add_product(name, description, price):
    response = requests.post(BASE_URL, json={
        "name": name,
        "description": description,
        "price": price
    })
    print(response.status_code, response.json())

def list_products():
    response = requests.get(BASE_URL)
    print(response.status_code, response.json())

# Example Usage
add_product("Laptop", "High-end gaming laptop", 1500.00)
list_products()
