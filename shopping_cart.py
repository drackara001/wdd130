# user can add item quantity for the each items added.
print("Welcome to the Shopping Cart Program!")

# item list stored.
item_names = []
item_prices = []
item_quantities = []

while True:
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = input("Please enter an action: ")

    if choice == "1":
        name = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{name}'? "))
        quantity = int(input(f"How many '{name}' would you like to add? "))
        item_names.append(name)
        item_prices.append(price)
        item_quantities.append(quantity)
        print(f"'{name}' (x{quantity}) has been added to the cart.")

    elif choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(item_names)):
            print(f"{i+1}. {item_names[i]} (x{item_quantities[i]}) - ${item_prices[i]:.2f}")

    elif choice == "3":
        print("The contents of the shopping cart are:")
        for i in range(len(item_names)):
            print(f"{i+1}. {item_names[i]} (x{item_quantities[i]}) - ${item_prices[i]:.2f}")
        remove_index = int(input("Which item would you like to remove? ")) - 1
        if 0 <= remove_index < len(item_names):
            removed_item = item_names.pop(remove_index)
            item_prices.pop(remove_index)
            item_quantities.pop(remove_index)
            print(f"{removed_item} removed.")
        else:
            print("Sorry, that is not a valid item number.")

    elif choice == "4":
        total = 0
        for i in range(len(item_prices)):
            total += item_prices[i] * item_quantities[i]
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")