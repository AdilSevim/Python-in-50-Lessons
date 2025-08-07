"""
Day 17, Homework: Contact Manager Program

Purpose: Create a simple contact manager that stores contacts in JSON format.
We use JSON to save and load contact information to and from files.

Expected output when run:
Contact Manager
1. Add contact
2. View contacts
3. Find contact
4. Exit
Choose an option (1-4): [user input]
[Based on user input, appropriate action is taken]
"""

import contact_manager


def main():
    """Run the contact manager program."""
    filename = "contacts.json"
    contacts = contact_manager.load_contacts(filename)
    
    while True:
        print("\nContact Manager")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Find contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contact_manager.add_contact(contacts, name, phone)
            print("Contact added!")
        elif choice == "2":
            if contacts:
                print("\nContacts:")
                for contact in contacts:
                    print(f"- {contact['name']}: {contact['phone']}")
            else:
                print("No contacts found.")
        elif choice == "3":
            name = input("Enter name to search: ")
            contact = contact_manager.find_contact(contacts, name)
            if contact:
                print(f"Found: {contact['name']}: {contact['phone']}")
            else:
                print("Contact not found.")
        elif choice == "4":
            contact_manager.save_contacts(contacts, filename)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
