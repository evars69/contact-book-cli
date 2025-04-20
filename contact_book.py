import json
import csv
import re

# Load contacts from JSON file
def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            data = file.read()
            return json.loads(data) if data else []  # Return empty list if file is empty
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist
    except json.JSONDecodeError:
        return []  # Return empty list if file is corrupted or empty

# Save contacts to JSON file
def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

# Validate phone number (10 digits)
def validate_phone(phone):
    return len(phone) == 10 and phone.isdigit()

# Validate email
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    while not validate_phone(phone):
        print("Invalid phone number. Please enter a valid 10-digit phone number.")
        phone = input("Enter Phone Number: ")

    email = input("Enter Email: ")
    while not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        email = input("Enter Email: ")

    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact for {name} added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

# Search contact by field
def search_contact():
    contacts = load_contacts()
    if not contacts:
        print("No contacts available to search.")
        return

    print("Search by:")
    print("1. Name")
    print("2. Email")
    print("3. Phone")

    choice = input("Enter choice (1/2/3): ")

    field_map = {
        '1': 'name',
        '2': 'email',
        '3': 'phone'
    }

    field = field_map.get(choice)
    if not field:
        print("Invalid choice.")
        return

    query = input(f"Enter {field} to search: ").strip().lower()

    found_contacts = []
    for contact in contacts:
        if query in contact[field].lower():
            found_contacts.append(contact)

    if found_contacts:
        print("\n--- Matching Contacts ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

# Edit a contact
def edit_contact():
    view_contacts()
    try:
        contact_index = int(input("Enter contact index to edit: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    contacts = load_contacts()

    if 0 <= contact_index < len(contacts):
        contact = contacts[contact_index]
        print(f"Editing Contact: {contact['name']}")

        name = input(f"Enter new name (current: {contact['name']}): ")
        phone = input(f"Enter new phone (current: {contact['phone']}): ")
        while not validate_phone(phone):
            print("Invalid phone number. Please enter a valid 10-digit phone number.")
            phone = input(f"Enter new phone (current: {contact['phone']}): ")

        email = input(f"Enter new email (current: {contact['email']}): ")
        while not validate_email(email):
            print("Invalid email format. Please enter a valid email.")
            email = input(f"Enter new email (current: {contact['email']}): ")

        address = input(f"Enter new address (current: {contact['address']}): ")

        contact['name'] = name or contact['name']
        contact['phone'] = phone or contact['phone']
        contact['email'] = email or contact['email']
        contact['address'] = address or contact['address']

        save_contacts(contacts)
        print(f"Contact for {contact['name']} updated successfully!")
    else:
        print("Invalid contact index.")

# Delete a contact
def delete_contact():
    view_contacts()
    try:
        contact_index = int(input("Enter contact index to delete: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    contacts = load_contacts()

    if 0 <= contact_index < len(contacts):
        deleted_contact = contacts.pop(contact_index)
        save_contacts(contacts)
        print(f"Contact for {deleted_contact['name']} deleted successfully!")
    else:
        print("Invalid contact index.")

# Export contacts to CSV
def export_contacts_to_csv():
    contacts = load_contacts()
    if not contacts:
        print("No contacts to export.")
        return

    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address"])
        for contact in contacts:
            writer.writerow([contact['name'], contact['phone'], contact['email'], contact['address']])

    print("Contacts exported to 'contacts.csv'.")

# Main Menu
def contact_book():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact (by Name/Email/Phone)")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Export Contacts to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            export_contacts_to_csv()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Contact Book
contact_book()