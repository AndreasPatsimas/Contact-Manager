from view.allcontacts import view_contacts
from view.savecontact import save_contact
from view.deletecontact import delete_contact


def menu():
    print(
        "------------Μενού Επιλογών------------ \n" +
        "1. Παρουσίαση όλων των επαφών \n" +
        "2. Προσθήκη μιας επαφής \n" +
        "3. Διαγραφή μιας επαφής \n" +
        "4. Έξοδος \n" +
        "Εισάγετε επιλογή [1-4]")

def menu_choice():
    choice = 0
    while (choice < 1 or choice > 4):
        try:
            choice = int(input())
        except:
            print("Μη έγκυρη τιμή")
        if (choice < 1 or choice > 4):
            print("Εισάγετε επιλογή [1-4]")
    return choice

if __name__ == "__main__":
    while True:
        menu()
        choice = menu_choice()
        print(choice)
        if choice == 1:
            view_contacts()
        elif choice == 2:
            save_contact()
        elif choice == 3:
            delete_contact()
        else:
            break