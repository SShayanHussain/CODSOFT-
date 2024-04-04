class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name}: {contact.phone_number}")

    def search_contact(self, query):
        search_results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def delete_contact(self, index):
        del self.contacts[index]

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(query)
            if search_results:
                print("Search results:")
                for index, contact in enumerate(search_results, start=1):
                    print(f"{index}. {contact.name}: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            index = int(input("Enter the index of the contact to update: ")) - 1
            if 0 <= index < len(contact_manager.contacts):
                updated_name = input("Enter updated name: ")
                updated_phone_number = input("Enter updated phone number: ")
                updated_email = input("Enter updated email: ")
                updated_address = input("Enter updated address: ")
                updated_contact = Contact(updated_name, updated_phone_number, updated_email, updated_address)
                contact_manager.update_contact(index, updated_contact)
                print("Contact updated successfully.")
            else:
                print("Invalid index.")

        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contact_manager.contacts):
                contact_manager.delete_contact(index)
                print("Contact deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
