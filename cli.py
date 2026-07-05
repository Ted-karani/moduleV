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

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        get_all()
    elif choice == "7":    
        print("Goodbye tschuss")
        break
    else:
        print("not valid monsuir")