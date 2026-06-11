# Lista liczb od -4 do 4
# 1. Wyświetl w konsoli następujące informacje z użyciem pętli na liście
# oraz instrukcji if elif else w celu sprawdzenia, czy liczba jest parzysta,
# czy nieparzysta. Dodaj tę informację w konsoli.
#
# 2. Pamiętaj, że 0 będzie osobnym przypadkiem, który trzeba sprawdzić jako
# pierwszy w if i w jej bloku wpisz "zero jest parzyste". Następnie w elif
# sprawdź, czy liczba jest parzysta, a w else będzie pewność, że jest nieparzysta.


list = [-4,-3,-2,-1,0,1,2,3,4]

for v in list:
    if v == 0:
        print("Zero jest parzyste.")
    elif v % 2 == 0:
        print("Liczba ", (v), " jest parzysta.")
    else:
        print("Liczba ", (v), " jest nieparzysta.")