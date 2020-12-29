from services.contact import ContactService

class ContactController():
    @staticmethod
    def get_contacts():
        return ContactService.fetch_all_contacts()

    @staticmethod
    def save_contact(contact):
        return ContactService.save_contact(contact)

    @staticmethod
    def delete_contact(id):
        ContactService.delete_contact(id)