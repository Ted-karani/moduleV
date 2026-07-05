import requests

def show_menu():
    print("\n Inventory Management System")
    print("1. View all inventory")
    print("2. View one item")
    print("3. Add new item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Fetch product from OpenFoodFacts api")
    print("7. Exit")

def get_all():
    response = requests.get("http://127.0.0.1:5000/inventory")
    items = response.json()
    for item in items:
        print(f"ID: {item['id']} | Name: {item['name']} | Brand: {item['brand']} | Price: {item['price']} | Stock: {item['stock']}")

def get_one():
    id = input("Enter item ID: ")
    response = requests.get("http://127.0.0.1:5000/inventory/" + id)
    print(response.json())

def add_item():
    name = input("Enter name: ")
    brand = input("Enter brand: ")
    price = input("Enter price: ")
    stock = input("Enter stock: ")
    response = requests.post("http://127.0.0.1:5000/inventory", json={
        "name": name,
        "brand": brand,
        "price": float(price),
        "stock": int(stock)
    })
    print(response.json())

def update_item():
    id = input("Enter item ID to update: ")
    price = input("Enter new price: ")
    stock = input("Enter new stock: ")
    response = requests.patch("http://127.0.0.1:5000/inventory/" + id, json={
        "price": float(price),
        "stock": int(stock)
    })
    print(response.json())

def delete_item():
    id = input("Enter item ID to delete: ")
    response = requests.delete("http://127.0.0.1:5000/inventory/" + id)
    print(response.json())

def fetch_product():
    barcode = input("Enter barcode: ")
    response = requests.get("http://127.0.0.1:5000/fetch/" + barcode)
    print(response.json())
    add = input("Add to inventory? (y/n): ")
    if add == "y":
        requests.post("http://127.0.0.1:5000/fetch/" + barcode + "/add")
        print("Added to inventory!")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        get_all()
    elif choice == "2":
        get_one()    
    elif choice == "3":
        add_item() 
    elif choice == "4":
        update_item()   
    elif choice == "5":
        delete_item()   
    elif choice =="6":
        fetch_product()         
    elif choice == "7":    
        print("Goodbye tschuss")
        break
    else:
        print("not valid monsuir")