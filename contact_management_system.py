import json
import os

if os.path.exists("contacts.json"):
    with open("contacts.json","r") as file:
        contacts = json.load(file)
else:
    contacts = {}


def saveContacts():
    with open("contacts.json","w") as file:
        json.dump(contacts,file,indent=4)


def addContact():
    name = input("Enter name of the contact👤: ").strip().lower()
    if name == "":
        print("⚠️ Name cannot be empty")
        return
    else:
        phone = input("Enter phone number📞: ").strip()
        email = input("Enter email-id📧: ").strip()
        if "@" not in email or "." not in email:
            print("⚠️ Invalid email format")
            return
        if not phone.isdigit():
            print("⚠️ Phone number should contain only numbers\nPlease try again!!")
            return
        else:
            phone = int(phone)
            if name not in contacts:
                contacts[name] = {
                    "phone":phone,
                    "email":email
                }
                saveContacts()
                print(f"✅ Contact {name} is added to your contacts")
            else:
                print("⚠️ The contact already exists!!")


def viewContacts():
    if not contacts:
        print("⚠️ Your contact list is empty!!")
    else:
        print(f"Total contacts: {len(contacts)}")
        for name,details in sorted(contacts.items()):
            print(f"Name  : {name.title()}")
            print(f"Phone  : {details['phone']}")
            print(f"Email  : {details['email']}")
            print("-"*35)


def searchContact():
    name = input("🔍Search contact name: ").strip().lower()
    if name in contacts:
        print("-"*35)
        print(f"Name  : {name.title()}")
        print(f"Phone  : {contacts[name]['phone']}")
        print(f"Email  : {contacts[name]['email']}")
        print("-"*35)
    else:
        print(f"⚠️ {name} is not found in your contacts!")


def updateContact():
    name = input("🔍Search contact name to update: ").strip().lower()
    if name in contacts:
        new_phone = input("New-phone no📞: ").strip()
        new_email = input("New email📧: ").strip()
        if "@" not in new_email or "." not in new_email:
            print("⚠️ Invalid email format")
            return
        if new_email.strip() == "" or new_phone.strip() == "":
            print("Phone number or email cannot be empty⚠️\nPlease try again!!") 
            return
            
        else:
            if not new_phone.isdigit():
                print("Phone number must contain only digits⚠️\nPlease try again!!")
                return
            else:
                new_phone = int(new_phone)
                contacts[name]["phone"] = new_phone
                contacts[name]["email"] = new_email
                saveContacts()
                print("Contact updated successfully✅")
    else:
        print("❌ Contact not found!!")


def deleteContact():
    name = input("Enter the name of the contact to be deleted: ").strip().lower()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name} ❓(yes/no): ").strip().lower()
        if confirm == "yes":
            del contacts[name]
            saveContacts()
            print(f"{name} is successfully deleted✅")
        elif confirm == "no":
            print(f"{name} is not deleted❎")
        else:
            print("⚠️ invalid input!!")
    else:
        print(f"{name} is not in your contacts list❌")


while True:
    print("*"*30)
    print("📞 CONTACT MANAGEMENT SYSTEM")
    print("*"*30)
    print("1.Add Contact➕ 👤\n2.View Contacts📖 👥\n3.Search Contact🔍 👤\n4.Update Contact✏️ 👤\n5.Delete Contact🗑️ 👤\n6.Exit🚪")

    try:
        choice = int(input("Choose any one of the option👉 "))
    except Exception as e:
        print("❌ Error!",e,"\nPlease try again!")
    else:
        match choice:
            case 1:
                addContact()
            case 2:
                viewContacts()
            case 3:
                searchContact()
            case 4:
                updateContact()
            case 5:
                deleteContact()
            case 6:
                print("✅ Exited...")
                break
            case _:
                print("⚠️ Enter the correct option!!")


    




