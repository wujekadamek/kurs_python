# 1. Stworz zmienna text z wartoscia hello i uzyj metody upper() do wyswietlenia wielkich liter.
#   Sprawdz dostepne metody za pomoca dir().
# 2. Stworz dwie zmienne x i y z wartoscia 256. Sprawdz czy x is y.
# 3. Stworz liste listOne z kilkoma elementami. Skopiuj listOne do listTwo poprzez przypisanie.
#   Sprawdz, czy listOne is listTwo
# 4. Zmodyfikuj listOne przez dodanie nowego elementu. Sprawdz, czy zmiana wplynela na listTwo.
#   Użyj if do wyswietlenia komunikatu o zmianie.
# 5. Stworz nowa liste listThree z takimi samymi elementami, co listOne. Sprawdz, czy listOne is listThree
#   i wyswietl odpowiedni komunikat za pomoca if.

text = "Hello"
print(text.upper())
print(dir(text))

x = 256
y = 256
print(x is y)

listOne = [21,37,67,69,420]
listTwo = listOne
print(listOne is listTwo)

listOne.append(666)
if listTwo is listOne:
    print("tak")
else:
    print("nie")

listThree = [21,37,67,69,420,666]

if listThree is listOne:
    print("tak")
else:
    print("nie")