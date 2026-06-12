#contact book
contacts = []

def add_contact(name, phone, email):
    if find_contact(name) is None:
        new_contact = {'name':name.strip(), 'phone':phone, 'email':email.strip()}
        contacts.append(new_contact)
        print("Contact added successfully.")
    else:
        print("The contact name already exists.")
def find_contact(name):
    
    for i in contacts:
        if i.get('name') == name:
            return i
    return None


def display_all_contact():
    if len(contacts) > 0:
        print(f"\n\n{'Name':<15} {'Phone':<15} {'Email':<15}")
        for i in contacts:
            print(f"{i['name']:<15} {i['phone']:<15} {i['email']:<15}")
    else:
        print("The contact list is empty. Please add contact to see the contacts.")

def delete_contact(name):
    check_contact = find_contact(name)
    if check_contact is not None:
        contacts.remove(check_contact)
        print(f'{name} deleted successfully. ')
    else:
        print('The contact is not present in the contact book.')

while True:
    print("\n\n1. Add Contact \n2. Find Contact \n3.Display all contact \n4.Delete Contact \n5.Exit")
    choice = input("Enter the choice you want: ")
    if choice == '1':
        name = input("Enter the name: ").lower()
        phone = input("Enter the phone: ")
        email = input("Enter the email: ").lower()

        if(name and phone and email):
            add_contact(name,phone,email)
        else:
            print('please fill all the details correctly.')
    elif choice == '2':
        name = input("Enter the name of the contact you want to search: ")
        if name != "":
            find_value = find_contact(name.lower())
            if find_value is not None:
                print(f'Name: {find_value["name"]}  Phone: {find_value["phone"]}  Email: {find_value["email"]} ')
            else:
                print("The contact you're searching for doesn't exist.")
        else:
            print("Please fill the details")
    elif choice == '3':
        display_all_contact()

    elif choice == '4':
        name = input("Enter the name of contact to delete: ")
        if name != "":
            delete_contact(name.lower())
        else:
            print("Please fill the details")
    elif choice == '5':
        break
    else:
        print("You entered the invalid value. Try again: ")