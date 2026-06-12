# Contact Book Manager — Capstone Mini-Project

contacts = []

def add_contact(name, phone, email):
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print(f"Contact '{name}' added.")

def find_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return 'Not found'

def display_all_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    print("\n--- Contact Book ---")
    for i, contact in enumerate(contacts):
        print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print("--------------------\n")

def delete_contact(name):
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            contacts.pop(i)
            print(f"Contact '{name}' deleted.")
            return
    print(f"'{name}' not found.")

# --- Demo ---
add_contact("Alice", "555-1234", "alice@mail.com")
add_contact("Bob", "555-5678", "bob@mail.com")
add_contact("Carol", "555-9999", "carol@mail.com")
display_all_contacts()
print(find_contact("Bob"))
print(find_contact("Zara"))
delete_contact("Alice")
display_all_contacts()
