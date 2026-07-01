# Zadanie: filtracja i przetwarzanie listy
#
# Cel: napisz program, ktory przechodzi przez liste liczb calkowitych od 1-10,
# pomija liczby parzyste, zatrzymuje sie, gdy napotka liczbe wieksza niz 8,
# a dla pozostalych liczb wypisuje ich kwadrat.
#
# Kroki do wykonania:
# 1. Stworz liste liczb calkowitych 1-10
# 2. Uzyj petli for do iteracji przez liste
# 3. W petli uzyj instrukcji "continue" do pominiecia liczb parzystych
# 4. Uzyj instrukcji "break" do zakoczenia petli, gdy liczba jest wieksza od 8
# 5. Dla liczb nieparzystych mneijszych lub rownych 8 wypisz ich kwadrat
# 6. Na koncu petli uzyj instrukcji "else" do wypisania komunikatu o zakonczeniu przetwarzania

numbers = [1,2,3,4,5,6,7,8,9,10]

for v in numbers:
    if v > 8:
        break
    if v % 2 == 0:
        continue
    print("Kwadrat liczby", v, "===>", v ** 2)
    
else:
    print("Koniec przetwarzania.")