# Contact Book - Simple Version

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for contact in contacts:
        print(f"Name: {contact['name']} | Phone: {contact['phone']}")
    print()

def search_contact():
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print("\n--- Contact Found ---")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("Enter new details (leave blank to keep old):")
            phone = input(f"Phone ({contact['phone']}): ") or contact['phone']
            email = input(f"Email ({contact['email']}): ") or contact['email']
            address = input(f"Address ({contact['address']}): ") or contact['address']
            contact.update({'phone': phone, 'email': email, 'address': address})
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the contact book
menu()


