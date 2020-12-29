from domain.contact import Contact

contacts = [Contact(name="Andreas Patsimas", email="andreas-patsim@hotmail.com", phone="555-555-5555").__str__(),
            Contact(name="Sotiris Patsimas", email="sotirinio@hotmail.com", phone="333-333-3333").__str__(),
            Contact(name="Chris Bolosis", email="bolosis@gmail.com", phone="222-222-2222").__str__(),
            Contact(name="Tasos Bolosis", email="tasosbolo@hotmail.com", phone="777-777-7777").__str__()]

class ContactRepository:

    @staticmethod
    def save(contact):
        contacts.append(contact.__str__())

    @staticmethod
    def find_all():
        return contacts

    @staticmethod
    def delete(id):
        contacts.pop(id)

