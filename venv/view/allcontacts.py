from controllers.contact import ContactController

my_contacts = ContactController.get_contacts()

def view_contacts():
    print(f"My contacts are: {my_contacts}")
