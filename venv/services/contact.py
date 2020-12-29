from repositories.contact import ContactRepository
from domain.contact import Contact

class ContactService:
    @staticmethod
    def fetch_all_contacts():
        return ContactRepository.find_all()

    @staticmethod
    def save_contact(contact):
        if isinstance(contact, Contact):
            ContactRepository.save(contact)
            return True
        return False

    @staticmethod
    def delete_contact(id):
        ContactRepository.delete(id)