# Zadanie: Tworzenie profilu użytkownika
#
# Cel: Napisz program, który umożliwia utworzenie profilu użytkownika w systemie.
# Program powinien prosić użytkownika o podanie imienia, nazwiska, wieku oraz
# miasta pochodzenia. Nie wszystkie informacje są wymagane. Użyj funkcji z nazwanymi
# argumentami
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję createUserProfile przyjmującą argumenty: firstName, lastName,
#    age oraz city 
# 2) Funkcja powinna zwracać słownik zawierający informacje o profilu użytkownika.
# 3) Poproś użytkownika o wprowadzenie wymaganych danych.
# 4) Wywołaj funkcję createUserProfile z odpowiednimi argumentami wprowadzonymi przez
#    użytkownika i przechowaj zwrócony słownik.
# 5) Wyświetl zwrócony profil użytkownika.


def createUserProfile(firstName, lastName, age, city):
    return {
        "firstName" : firstName,
        "lastName" : lastName,
        "age" : age,
        "city" : city
    }

firstName = str(input("Podaj imie: "))
lastName = str(input("Podaj nazwisko: "))
age = str(input("Podaj wiek: "))
city = str(input("Podaj miasto: "))

userProfile = createUserProfile(firstName, lastName, age, city)
#userProfile = createUserProfile(firstName=firstName, lastName=lastName, age=age, city=city) ### <-- daje dokladnie taki sam wynik, co linia wyzej
print("********************************************************************************")
print("*\tProfil uzytkownika: \t \t \t \t \t \t \t \t *")
print("*\tImię:", userProfile["firstName"])
print("*\tnazwisko:", userProfile["lastName"])
print("*\twiek:", userProfile["age"])
print("*\tmiasto:", userProfile["city"])
print("********************************************************************************")