#Task Contact Book
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, updated_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = updated_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            removed_contact = self.contacts.pop(index - 1)
            print(f"{removed_contact.name} removed from contacts.")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print(f"{name} added to contacts.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Search by name or phone: ")
            found_contacts = contact_book.search_contact(query)
            if found_contacts:
                print("\nSearch Results:")
                for idx, contact in enumerate(found_contacts, start=1):
                    print(f"{idx}. {contact.name} - {contact.phone}")
            else:
                print("No contacts found.")
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            updated_contact = Contact(name, phone, email, address)
            contact_book.update_contact(index, updated_contact)
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    print("Welcome to the Contact Book!")
    main()


