from controllers.contact import ContactController
from domain.contact import Contact

def save_contact():
    print("Save contact process begins.")
    name = str(input("Give name: "))
    email = str(input("Give email: "))
    phone = str(input("Give phone: "))
    print("Saving...")
    if(ContactController.save_contact(Contact(name, email, phone))):
        print("Save contact process completed successfully.")
    else:
        print("Contact not saved.")
