# Zadanie - analiza danych demograficznych
# W tym zadaniu wykorzystasz krotki do przechowywania i analizy
# danych demograficznych. Użyj podstawowych operacji na krotkach
# do manipulacji danymi oraz do wykonania prostych obliczeń.
#
# 1) Stwórz krotkę `population` zawierającą liczbę ludności w milionach
#    dla pięciu wybranych krajów. Np. Polska - 38, Niemcy - 83 itd.
# 2) Dodaj do krotki `population` dane dla kolejnego kraju używając
#    konkatenacji.
# 3) Wyświetl długość krotki `population`, aby sprawdzić ile jest
#    obecnie danych.
# 4) Sprawdź, czy liczba 100 (milionów ludności) znajduje się w krotce
#    `population`.
# 5) Wyświetl liczbę ludności dla trzeciego kraju w krotce.
# 6) Oblicz minimalną i maksymalną liczbę ludności w krotce `population`.
# 7) Jeśli maksymalna liczba ludności w krotce jest większa niż 500 mln,
#    wyświetl komunikat: "Znaleziono kraj o bardzo dużej populacji".
#    W przeciwnym razie, wyświetl: "Wszystkie kraje mają populację poniżej 500 mln".



population = (38, 83, 69, 59, 500)
population = population + (19,86)
print("Dlugosc krotki:", len(population), "elementow.")

if 100 in population:
    print("Jest kraj o populacji 100 mln.")
else:
    print("Nie ma kraju o populacji 100 mln.")

print("Liczba mieszkancow kraju nr 3 z listy (w mln): ", population[2])

min = min(population)
max = max(population)
print("Najnizsza liczba mieszkancow (w mln):", min)
print("Najwyzsza liczba mieszkancow (w mln):", max)

if max >= 500:
    print("Znaleziono kraj o bardzo dużej populacji.")
else:
    print("Wszystkie kraje mają populację poniżej 500 mln.")