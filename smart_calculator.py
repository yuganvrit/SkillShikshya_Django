"""
Smart Calculator with History
------------------------------
Takes two numbers and an operator, performs the calculation,
and keeps track of the last 10 calculations.
"""

# History stored as a list of tuples: (num1, operator, num2, result)
history = []
MAX_HISTORY = 10


def calculate(num1, operator, num2):
    """Perform the calculation and return the result (or None on error)."""
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return None
            return num1 / num2
        case "**":
            return num1 ** num2
        case "%":
            if num2 == 0:
                print("Error: Modulo by zero is not allowed.")
                return None
            return num1 % num2
        case _:
            print(f"Error: Unsupported operator '{operator}'.")
            return None


def add_to_history(num1, operator, num2, result):
    """Add a calculation to history, keeping only the last MAX_HISTORY entries."""
    history.append((num1, operator, num2, result))
    if len(history) > MAX_HISTORY:
        history.pop(0)  # remove the oldest entry


def show_history():
    """Print the calculation history."""
    if not history:
        print("\nNo calculations yet.\n")
        return

    print("\n--- Calculation History (most recent last) ---")
    for i, (num1, operator, num2, result) in enumerate(history, start=1):
        print(f"{i}. {num1} {operator} {num2} = {result}")
    print("-----------------------------------------------\n")


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        value = input(prompt)
        try:
            # Try int first, fall back to float
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            print("Invalid number. Please try again.")


def main():
    print("=== Smart Calculator ===")
    print("Supported operators: +  -  *  /  **  %\n")

    while True:
        print("Menu:")
        print("  1. Calculate")
        print("  2. View history")
        print("  3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            num1 = get_number("Enter the first number: ")
            operator = input("Enter an operator (+, -, *, /, **, %): ").strip()
            num2 = get_number("Enter the second number: ")

            result = calculate(num1, operator, num2)

            if result is not None:
                print(f"Result: {num1} {operator} {num2} = {result}\n")
                add_to_history(num1, operator, num2, result)
            else:
                print()  # blank line for readability after an error

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
