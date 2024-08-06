contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contacts():
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    if not results:
        print("No contacts found.")
    else:
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")

def update_contact():
    query = input("Enter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new contact name: ") or contact['name']
            contact['phone'] = input("Enter new contact phone number: ") or contact['phone']
            contact['email'] = input("Enter new contact email: ") or contact['email']
            contact['address'] = input("Enter new contact address: ") or contact['address']
            print("Contact updated successfully!")
            return
    print("No contact found with that name or phone number.")

def delete_contact():
    query = input("Enter name or phone number of the contact to delete: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("No contact found with that name or phone number.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
