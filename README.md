# 📞 Contact Management System

A simple command-line Contact Management System built with Python that allows users to store, manage, and persist contact information using a JSON file.

## 🚀 Features

* ➕ Add new contacts
* 📖 View all saved contacts
* 🔍 Search contacts by name
* ✏️ Update existing contacts
* 🗑️ Delete contacts
* 💾 Automatic data persistence using JSON
* ✅ Input validation for phone numbers and email addresses

## 📂 Project Structure

```text
ContactManagementSystem/
│
├── main.py          # Main application
├── contacts.json    # Stores contact data
└── README.md        # Project documentation
```

## 🛠️ Technologies Used

* Python 3
* JSON for data storage
* File Handling
* Functions
* Dictionaries
* Exception Handling

## 📋 Contact Format

Each contact is stored in the following format:

```json
{
    "john": {
        "phone": 9876543210,
        "email": "john@example.com"
    }
}
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd ContactManagementSystem
```

3. Run the program:

```bash
python main.py
```

## 📸 Menu Options

```text
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

## 🔒 Input Validation

The application validates:

* Contact name cannot be empty
* Phone number must contain only digits
* Email address must follow a valid format
* Duplicate contacts are prevented

## 🎯 Learning Outcomes

This project helped practice:

* Python functions
* Dictionaries and nested dictionaries
* JSON file handling
* CRUD operations (Create, Read, Update, Delete)
* Exception handling
* User input validation

## 🌱 Future Improvements

* Partial name search
* Multiple phone numbers per contact
* Contact categories (Friends, Family, Work)
* Export contacts to CSV
* Graphical User Interface (GUI)
* Password-protected contact book

## 📄 License

This project is created for learning and educational purposes.
