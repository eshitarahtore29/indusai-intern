# Contact Book Application

# List to store contact information
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print("Contact added successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    for contact in contacts:
        if contact['name'] == name:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found!")

def display_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
