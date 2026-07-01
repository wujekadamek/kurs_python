
# 1. Napisz funkcję findLargest która przyjmuje 
#    dwie liczby jako parametry num1 i num2. 
#    Funkcja musi pokazać w konsoli informację,
#    która liczba jest większa oraz jej wartość.
#    np: "num1 jest większą liczbą: 12" lub, że obie 
#    liczby są równe. 
#    Pamiętaj aby użyć if elif oraz else.
# 2. Dodatkowo funkcja zwraca większą liczbę dzięki return
# 3. Sprawdź funkcję przekazując wartości 3 i 10,
#    pokaż w konsoli zwróconą wartość z funkcji
# 4. W ten sam sposób sprawdź funkcję dla 12 i 7


def findLargest(num1,num2):
    if num1 > num2:
        print("Liczba", float(num1), "jest wieksza od liczby", float(num2))
        return num1

    elif num1 < num2:
        print("Liczba", float(num1), "jest mniejsza od liczby", float(num2))
        return num2

    else:
        print("Liczba", float(num1), "oraz", float(num2), "sa rowne.")
        return num1

v1 = findLargest(3,10)
print("Wynik wywolania:", v1)

v2 = findLargest(12,7)
print("Wynik wywolania:", v2)