# Command-Line Contact Book

A simple yet powerful command-line based Contact Book application written in Python. This tool allows users to manage their contacts efficiently through a text-based interface, with data persistence via JSON and optional export to CSV.

---

## 🚀 Features

* 📇 Add, View, Search, Edit, and Delete contacts
* 💾 Data persistence using JSON file storage
* ✅ Input validation for phone numbers and email addresses
* 📤 Export all contacts to a `.csv` file
* 💡 Organized modular code structure using Python functions

---

## 📦 Stored Contact Fields

Each contact entry includes:

* **Name**
* **Phone Number** (10-digit validation)
* **Email** (validated with regex)
* **Address**

---

## 🔧 Installation & Setup

1. **Clone the repository** (or copy the code file):

* git clone https://github.com/evars69/contact-book-cli.git

2. **Navigate to the directory** :

* cd contact-book-cli

3. **Run the Python script** :

* python contact_book.py

---

## 📖 Usage

### Menu Options:

* Add Contact
* View Contacts
* Search Contact
* Edit Contact
* Delete Contact
* Export Contacts to CSV
* Exit

---

### Example:

* To add a contact, press `1`, then enter the contact details as prompted.

---

## 💡 Validations

* **Phone Number** : Must be 10 digits long, only numeric characters allowed.
* **Email** : Must follow standard email format using regular expressions.

---

## 📁 Files Used

* `contacts.json` – Stores all contact entries persistently.

---

## 📤 Exported CSV Format

| Name     | Phone      | Email             | Address |
| -------- | ---------- | ----------------- | ------- |
| John Doe | 9876543210 | [john@example.com]() | Mumbai  |

---

## 📌 Dependencies

Only standard Python libraries are used:

* `json`
* `re`

---

## 📈 Future Enhancements

* Command-line arguments support
* GUI version using Tkinter or PyQt
* Search filters and pagination for large contact books
* Integration with cloud storage (e.g., Google Drive or Firebase)

---

## 👩‍💻 Author

**Varsha** – [LinkedIn](https://www.linkedin.com/in/varsha-kumari-2b5741202/) | [GitHub](https://github.com/evars69)
