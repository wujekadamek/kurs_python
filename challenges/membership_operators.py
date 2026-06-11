# Wykorzystaj operatory przynaleznosci (in, not in) do sprawdzenia obecnosci elementow w kolekcjach
# i uzycie instrukcji warunkowej if
# 1. Sprawdz, czy liczba 7 znajduje sie w liscie numbers i wyswietl odpowiedni komunikat.
# 2. Sprawdz, czy ciag znwkow "kot" nie znajduje sie w tuple "animals" i wyswietl odpowiedni komunikat.
# 3. Stworz slownik "user" z kluczami "name" i "age". Sprawdz ,czy klucz name znajduje sie w slowniku.

numbers = [0,1,2,3,4,5,6,7]
if 7 in numbers:
    print("Liczba 7 jest w liscie \"numbers\".")
else:
    print("Liczba 7 NIE jest w liscie \"numbers\".")

animals = ("pies", "pajonk")
if "kot" not in animals:
    print("\"kot\" nie znajduje sie w \"animals\".")
else:
    print("\"kot\" znajduje sie w \"animals\".")


user = {
    "name" : "abc",
    "age" : 12
}

if "name" in user:
    print("\"name\" znajduje sie w slowniku.")
else:
    print("\"name\" nie znajduje sie w slowniku.")