# Zadanie - zarządzanie książką adresową
# W tym zadaniu będziesz używać słowników do zarządzania prostą
# książką adresową. Nauczysz się dodawać, usuwać, kopiować oraz
# przeszukiwać dane w słowniku.
#
# 1) Stwórz słownik `addressBook` zawierający początkowo jedną
#    osobę: Jan Kowalski, mieszka w Gdańsku, kod pocztowy 80-000.
# 2) Dodaj do książki adresowej nową osobę: Anna Nowak, mieszka w
#    Warszawie, kod pocztowy 00-001.
# 3) Usuń Jan Kowalski z książki adresowej.
# 4) Skopiuj książkę adresową do nowej zmiennej i sprawdź, czy
#    kopia jest identyczna (porównaj referencje i zawartość).
# 5) Sprawdź, czy w skopiowanej książce adresowej jest osoba
#    mieszka w Krakowie. Jeśli nie, wyświetl odpowiedni komunikat.
# 6) Wyświetl wszystkie klucze i wartości w książce adresowej.
#

addressBook = {
    "jan": {
    "name" : "Jan",
    "surname" : "Kowalski",
    "city" : "Gdańsk",
    "code" : "80-000"
    }
}
print("Poczatkowa wartosc ksiazki adresowej: ", addressBook)

addressBook["anna"] = {"name" : "Anna", "surname" : "Nowak", "city" : "Warszawa", "code" : "00-001"}
print("Ksiazka po aktualizacji: ", addressBook)

del addressBook["jan"]
print("Ksiazka po usunieciu elementu: ", addressBook)

copyAddressBook = addressBook.copy()

print("Czy zawartosc jest identyczna:", addressBook == copyAddressBook)
print("Czy referencje sa identyczne:", addressBook is copyAddressBook)

for person in addressBook.values():
    if person["city"] == "Kraków":
        print("Jest ktos mieszkajacy w Krakowie.")
    else:
        print("Nie ma osoby mieszkajacej w Krakowie.")

print("Klucze:", addressBook.keys())
print("Wartosci:", addressBook.values())