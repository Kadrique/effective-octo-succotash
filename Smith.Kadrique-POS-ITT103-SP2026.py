# Best Buy Retail store
# This part of the code list the srtucture of the menu as name, price then quantity\qty
products = [
    {"name": "Bread", "price": 500, "qty": 20},
    {"name": "Milk", "price": 130, "qty": 15},
    {"name": "Tin Milk", "price": 200, "qty": 30},
    {"name": "Eggs", "price": 240, "qty": 30},
    {"name": "Butter", "price": 200, "qty": 10},
    {"name": "Cheese", "price": 300, "qty": 8},
    {"name": "Rice", "price": 400, "qty": 12},
    {"name": "Beans", "price": 350, "qty": 18},
    {"name": "Sugar", "price": 120, "qty": 22},
    {"name": "Salt", "price": 80, "qty": 40},
    {"name": "Red Bull", "price": 150, "qty": 40},
    {"name": "Orange Juice", "price": 150, "qty": 18},
    {"name": "Pepsi", "price": 150, "qty": 22},
    {"name": "Coconut Water", "price": 190, "qty": 40},
    {"name": "Vita Malt", "price": 190, "qty": 40},
    {"name": "Bleach", "price": 80, "qty": 40},
    {"name": "Ariel Fob", "price": 80, "qty": 40},
    {"name": "Detergent", "price": 150, "qty": 18},
    {"name": "Jasmine HandSoap", "price": 150, "qty": 22},
    {"name": "Protex Soap", "price": 190, "qty": 40},
    {"name": "Dove BodyWash", "price": 200, "qty": 18},
    {"name": "Shampoo", "price": 190, "qty": 40},
    {"name": "Conditioner", "price": 190, "qty": 40},
    {"name": "Disinfectant", "price": 310, "qty": 40}

]
#This part of the code initializes cart as a dictionary
cart = {}


# This part of the code finds the product in the list

def find_product(name):
    for item in products:
        if item["name"] == name:
            return item
    return None



# This part of code shows the  products selected

def show_products():
    print("\n--- Product List ---")
    for item in products:
        print(item["name"], "- Price:", item["price"], "| Stock:", item["qty"])



# This part of the code allows user to add items to the cart

def add_item():
    show_products()
    name = input("Enter item name: ").title()

    product = find_product(name)

    if product is None:
        print("Item could not found, Try again.")
        return

    try:
        qty = int(input("Enter quantity: "))
    except:
        print("Invalid number try again.")
        return

    if qty <= 0:
        print("Invalid quantity try again.")
        return

    if qty > product["qty"]:
        print("Not enough in stock.")
        return

    # This part of the code gives confirmation of the item added to cart
    if name in cart:
        cart[name] += qty
    else:
        cart[name] = qty

    product["qty"] -= qty
    print("Item is added.")



# This part of code allows the user remove item from the cart

def remove_item():
    if not cart:
        print(" Your Cart is empty.")
        return

    name = input("Enter item to remove it: ").title()

    if name not in cart:
        print("Item is not in cart.")
        return

    product = find_product(name)

    try:
        qty = int(input("Enter quantity to remove: "))
    except:
        print("Invalid number try again.")
        return

    if qty >= cart[name]:
        product["qty"] += cart[name]
        del cart[name]
        print("Item is removed.")
    else:
        cart[name] -= qty
        product["qty"] += qty
        print("Item is updated.")



# This part of code allows the user to view what is in the cart

def view_cart():
    if not cart:
        print("Cart is empty.")
        return

    print("\n--- Cart ---")
    total = 0

    for name, qty in cart.items():
        product = find_product(name)
        cost = product["price"] * qty
        total += cost
        print(name, "x", qty, "=", cost)

    print("Subtotal:", total)



# This part of the code allows the user to Checkout

def checkout():
    if not cart:
        print("Cart is empty.")
        return

    subtotal = 0
    for name, qty in cart.items():
        product = find_product(name)
        subtotal += product["price"] * qty

    # This part of the code calculates the discount if subtotal is greater than 5000 as well as tax
    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.05

    subtotal -= discount
    tax = subtotal * 0.10
    total = subtotal + tax

    print("\nTotal needed to pay:", total)

    # This part of code validates the total needed to be paid
    while True:
        try:
            paid = float(input("Enter the amount paid: "))
        except:
            print("Invalid input.")
            continue

        if paid < total:
            print("Not enough money.")
        else:
            change = paid - total
            break

    # This part of the code generates the receipt
    print("\n====== RECEIPT ======")
    print("Best Buy Retail Store\n")

    for name, qty in cart.items():
        product = find_product(name)
        print(name, "x", qty, "=", product["price"] * qty)

    print("\nSubtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Total:", total)
    print("Paid:", paid)
    print("Change:", change)

    print("\nRespect and Big Up Yuh Self!")
    print("=====================")

    cart.clear()



# This part of the code gives a low stock warning if product quantity in inventory falls below 5

def low_stock():
    print("\nLow Stock on that particular Item:")
    for item in products:
        if item["qty"] < 5:
            print(item["name"], "- only", item["qty"], "left")



# This part of the code is core program in which the user navigates the menu via numbers

while True:
    print("\n1. Show Products")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_item()

    elif choice == "3":
        remove_item()

    elif choice == "4":
        view_cart()

    elif choice == "5":
        checkout()
        low_stock()

    elif choice == "6":
        print("Big Up Yuh Self, Thanks for Shopping at Best Buy Retail Store!")
        break

    else:
        print("Invalid choice.")
