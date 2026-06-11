# 1. zadeklaruj zmienna "number" z int o wartosci 5 i wyswietl jej adres w pamieci
# 2. zwieksz wartosc zmiennej "number" o 2 i ponownie wyswietl jej adres w pamieci
# 3. utworz liste "fruits" z trzema owocami: apple, banana, cherry. wyswietl adres listy w pamieci
# 4. dodaj do listy "fruits" kolejny owoc: orange i wyswietl adres listy w pamieci
# 5. na podstawie wykonanych czynnosci wyjasnij rozmice miedzy typami mutowalnymi a niemutowalnymi

number = 5
print("Adres zmiennej number w pamięci wynosi teraz: \t \t \t \t", id(number))

number += 2
print("Adres zmiennej number w pamięci po dodaniu 2 wynosi teraz: \t \t", id(number))

fruits = ["apple", "banana", "cherry"]
print("Adres listy fruits w pamięci wynosi teraz: \t \t \t \t", id(fruits))
fruits += ["orange"]
print("Adres listy fruits w pamięci po dodaniu jednej pozycji wynosi teraz: \t", id(fruits))
print(fruits)

print("Różnica między mutable a immutable polega na tym, że: ")
print("Mutable NIE zmieniaja adresu w pamięci")
print("Immutable zmieniają adres w pamięci")
