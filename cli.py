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

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "7":
        print("Goodbye tschuss")
        break
    else:
        print("not valid monsuir")