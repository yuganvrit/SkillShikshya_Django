"""
Shopping Cart with Discounts
-------------------------------
Cart is a list of dictionaries: {"item": "Shoes", "price": 50.0, "qty": 2}

Discount rules (based on subtotal):
  - subtotal > $200 -> 20% off
  - subtotal > $100 -> 10% off
  - otherwise       -> no discount

After the discount, an 8% tax is applied, and a formatted receipt is printed.
"""

TAX_RATE = 0.08

cart = []


def add_item():
    """Ask the user for item details and add it to the cart."""
    item = input("Enter item name: ").strip()

    if not item:
        print("Item name cannot be empty.\n")
        return

    try:
        price = float(input("Enter price per unit: $"))
        if price < 0:
            print("Price cannot be negative.\n")
            return
    except ValueError:
        print("Invalid price.\n")
        return

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Quantity must be a positive whole number.\n")
            return
    except ValueError:
        print("Invalid quantity.\n")
        return

    cart.append({"item": item, "price": price, "qty": qty})
    print(f"Added {qty} x {item} @ ${price:.2f} each.\n")


def remove_item():
    """Remove an item from the cart by its position number."""
    if not cart:
        print("Cart is empty.\n")
        return

    view_cart()

    try:
        num = int(input("Enter the item number to remove: "))
        if 1 <= num <= len(cart):
            removed = cart.pop(num - 1)
            print(f"Removed {removed['item']} from the cart.\n")
        else:
            print("Invalid item number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def view_cart():
    """Display the current contents of the cart."""
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\n--- Cart ---")
    for i, entry in enumerate(cart, start=1):
        line_total = entry["price"] * entry["qty"]
        print(f"{i}. {entry['item']} - ${entry['price']:.2f} x {entry['qty']} = ${line_total:.2f}")
    print("------------\n")


def calculate_subtotal():
    """Sum up price * qty for every item in the cart."""
    subtotal = 0.0
    for entry in cart:
        subtotal += entry["price"] * entry["qty"]
    return subtotal


def get_discount_rate(subtotal):
    """Return the discount rate (as a decimal) based on the subtotal."""
    if subtotal > 200:
        return 0.20
    elif subtotal > 100:
        return 0.10
    else:
        return 0.0


def print_receipt():
    """Print a formatted receipt with subtotal, discount, tax, and total."""
    if not cart:
        print("\nYour cart is empty. Add items before checking out.\n")
        return

    subtotal = calculate_subtotal()
    discount_rate = get_discount_rate(subtotal)
    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount
    tax_amount = discounted_subtotal * TAX_RATE
    total = discounted_subtotal + tax_amount

    print("\n========== RECEIPT ==========")
    for entry in cart:
        line_total = entry["price"] * entry["qty"]
        print(f"{entry['item']:<15} {entry['qty']:>2} x ${entry['price']:>6.2f} = ${line_total:>8.2f}")
    print("------------------------------")
    print(f"{'Subtotal:':<24} ${subtotal:>8.2f}")

    if discount_rate > 0:
        print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':<24} -${discount_amount:>7.2f}")
        print(f"{'After discount:':<24} ${discounted_subtotal:>8.2f}")
    else:
        print(f"{'Discount:':<24} ${0.0:>8.2f}")

    print(f"{'Tax (' + str(int(TAX_RATE * 100)) + '%):':<24} ${tax_amount:>8.2f}")
    print("------------------------------")
    print(f"{'TOTAL:':<24} ${total:>8.2f}")
    print("==============================\n")


def main():
    print("=== Shopping Cart with Discounts ===")
    print(f"(Discounts: 10% off over $100, 20% off over $200 | Tax: {int(TAX_RATE * 100)}%)\n")

    while True:
        print("Menu:")
        print("  1. Add item")
        print("  2. Remove item")
        print("  3. View cart")
        print("  4. Checkout (print receipt)")
        print("  5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            print_receipt()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()
