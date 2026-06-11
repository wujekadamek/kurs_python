# Skorzystaj z operatorow porownania, aby sprawdzic prawdziwosc
# roznych stwierdzen i uzyj instrukcji warunkowych do wyswietlenia
# odpowiednich komunukatow.
# 1. Porownaj, czy 15 jest wieksze od 10, wyswietl wynik
# 2. Sprawdz, czy 5 jest rowne 5 i wyswietl wynik
# 3. Zadeklaruj 2 zmienne: x = 20 i y = 30.
#   Sprawdz, czy x jest mniejsze od y
# 4. Sprawdz, czy 100 jest mniejsze lub rowne 101
# 5. Uzyj instrukcji warunkowej, aby sprawdzic, czy 50 nie jest rowne 20.
#   Jesli tak, wyswietl stosowny komunikat.
# 6. Porownaj, czy "hello" jest rozne od "goodbye".
#   Jesli tak, wyswietl komunikat potwierdzajacy.

if 15 > 10:
    print("15 jest wieksze od 10.")
else:
    print("15 nie jest wieksze od 10.")

if 5 == 5:
    print("5 jest rowne 5.")
else:
    print("5 nie jest rowne 5.")

x = 20
y = 30
if x < y:
    print("x jest mniejsze od y.")
else:
    print("x nie jest mniejsze od y.")

if 100 <= 101:
    print("100 jest mniejsze lub rowne 101.")
else:
    print("100 nie jest mniejsze lub rowne 101.")

if 50 != 20:
    print("50 nie jest rowne 20.")
else:
    print("50 jest rowne 20.")

if "hello" != "goodbye" :
    print("hello jest rozne od goodbye.")
else:
    print("hello nie jest rozne od goodbye")