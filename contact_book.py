"""
Contact Book
-------------
A menu-driven contact manager using a dictionary of dictionaries:

contacts = {
    "Alice": {"phone": "...", "email": "...", "city": "..."},
    "Bob":   {"phone": "...", "email": "...", "city": "..."},
    ...
}

Search is case-insensitive and supports partial name matches.
"""

contacts = {}


def add_contact():
    """Ask the user for contact details and add them to the dictionary."""
    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty.\n")
        return

    if name in contacts:
        print(f"A contact named '{name}' already exists. Use 'update' instead.\n")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()

    contacts[name] = {"phone": phone, "email": email, "city": city}
    print(f"Contact '{name}' added.\n")


def find_matches(query):
    """
    Return a list of (name, info) pairs whose name contains the query,
    case-insensitively.
    """
    query_lower = query.lower()
    matches = []

    for name, info in contacts.items():
        if query_lower in name.lower():
            matches.append((name, info))

    return matches


def display_contact(name, info):
    """Print a single contact's details in a readable format."""
    print(f"Name : {name}")
    print(f"Phone: {info['phone']}")
    print(f"Email: {info['email']}")
    print(f"City : {info['city']}")
    print("-" * 20)


def search_contact():
    """Search for contacts by partial, case-insensitive name match."""
    if not contacts:
        print("No contacts saved yet.\n")
        return

    query = input("Enter a name (or part of a name) to search: ").strip()
    matches = find_matches(query)

    if not matches:
        print(f"No contacts found matching '{query}'.\n")
        return

    print(f"\nFound {len(matches)} matching contact(s):")
    for name, info in matches:
        display_contact(name, info)
    print()


def update_contact():
    """Update one or more fields of an existing contact."""
    if not contacts:
        print("No contacts saved yet.\n")
        return

    query = input("Enter the exact name of the contact to update: ").strip()
    matches = find_matches(query)

    # For update/delete, require an exact (case-insensitive) match to avoid ambiguity
    exact_match = None
    for name, info in matches:
        if name.lower() == query.lower():
            exact_match = name
            break

    if exact_match is None:
        print(f"No contact found with the exact name '{query}'.\n")
        return

    print(f"\nUpdating '{exact_match}'. Press Enter to keep the current value.")
    info = contacts[exact_match]

    new_phone = input(f"Phone [{info['phone']}]: ").strip()
    new_email = input(f"Email [{info['email']}]: ").strip()
    new_city = input(f"City [{info['city']}]: ").strip()

    if new_phone:
        info["phone"] = new_phone
    if new_email:
        info["email"] = new_email
    if new_city:
        info["city"] = new_city

    print(f"Contact '{exact_match}' updated.\n")


def delete_contact():
    """Delete a contact by exact (case-insensitive) name match."""
    if not contacts:
        print("No contacts saved yet.\n")
        return

    query = input("Enter the exact name of the contact to delete: ").strip()

    # Find the exact key (case-insensitive) so we can delete it correctly
    target_name = None
    for name in contacts:
        if name.lower() == query.lower():
            target_name = name
            break

    if target_name is None:
        print(f"No contact found with the exact name '{query}'.\n")
        return

    confirm = input(f"Are you sure you want to delete '{target_name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[target_name]
        print(f"Contact '{target_name}' deleted.\n")
    else:
        print("Deletion cancelled.\n")


def list_contacts():
    """List all contacts, sorted alphabetically by name."""
    if not contacts:
        print("No contacts saved yet.\n")
        return

    print(f"\n--- All Contacts ({len(contacts)}) ---")
    for name in sorted(contacts.keys(), key=str.lower):
        display_contact(name, contacts[name])
    print()


def main():
    print("=== Contact Book ===")

    while True:
        print("Menu:")
        print("  1. Add contact")
        print("  2. Search contacts")
        print("  3. Update contact")
        print("  4. Delete contact")
        print("  5. List all contacts")
        print("  6. Quit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
