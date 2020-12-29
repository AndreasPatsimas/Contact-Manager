from controllers.contact import ContactController

def inputId(contacts_ids):
    try:
        id = int(input())
        if id not in contacts_ids:
            print("Please input a number from the given ids.")
            id = None
    except:
        print("Please give a number.")
        id = None
    return id

def delete_contact():
    my_contacts = ContactController.get_contacts()
    contacts_ids = [i for i in range(len(my_contacts))]
    print(list(zip(contacts_ids, my_contacts)))
    print("Give id to delete contact...")
    while True:
        id = inputId(contacts_ids)
        if id is not None:
            break
    ContactController.delete_contact(id)