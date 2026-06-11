# Wykorzystaj operatory logiczne (and, or, not) do sprawdzenia
# roznych warunkow i wyswietl odpowiednie komunikaty w konsoli.
# 1. Sprawdz jednoczesnie, czy zmienna hoursWorked z wartoscia 9 jest wieksza od 8 i czy projectFinished z True jest True.
#   Jesli tak, wyswietl "Mozesz isc do domu"
# 2. Sprawdz, czy temperatura temp jako 35 jest mniejsza od 0 lub wieksza od 30.
#   Jesli tak, wyswietl "Ekstremalne warunki pogodowe"
# 3. Uzyj operatora not, aby sprawdzic, czy isHoliday z False czy jest False.
#    Jesli tak, wyswietl "Dzis jest dzien roboczy"
# 4. Uzyj kombinacji operatorow, aby sprawdzic, czy errorsFound z 12 jest mniejsze od 10 i czy warnings z 1 jest rowne 0.
#   Jesli nie, wyswietl "Sprawdz kod jeszcze raz"

hoursWorked = 9
projectFinished = True

if hoursWorked > 8 and projectFinished == True:
    print("Mozesz juz isc do domu!")

temp = 35
if temp < 0 or temp > 30:
    print("Ekstremalne warunki pogodowe!")

isHoliday = False
if not isHoliday == True:
    print("Dzis jest dzien roboczy.")

errorsFound = 12
warnings = 1

if not errorsFound < 10 or warnings == 0:
    print("Sprawdz kod jeszcze raz!")