#Define the Contact class
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email


# Define the AddressBook class
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def search_contact(self, name):
        return next((contact for contact in self.contacts if contact.name == name), None)


# Example usage with user input
address_book = AddressBook()

# Add contacts based on user input
while True:
    choice = input("Do you want to add a contact? (yes/no): ").lower()

    if choice != 'yes':
        break

    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    # Create a Contact object and add it to the address book
    new_contact = Contact(name, phone_number, email)
    address_book.add_contact(new_contact)

# Display the contacts in the address book
print("Contacts in the address book:")
for contact in address_book.contacts:
    print(f"{contact.name}, {contact.phone_number}, {contact.email}")
