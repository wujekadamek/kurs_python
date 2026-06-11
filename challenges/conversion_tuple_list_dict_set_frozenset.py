#   1. stworz liste "numbers" zawierajaca liczby od 7-12. Wyswielt te liste.
#   2. zamien liste "numbers" na  krotke "tupleNumbers" i wyswielt wynik.
#   3. utworz liste "mixedList" skladajaca sie z roznych typow danych, np.
#   string, integer, float. wyswietl mixedList
#   4. przeksztalc "mixedList" w zbior "setMixed" i wyswielt jego typ oraz zawartosc
#   5. zamien "tupleNumbers" na frozen set "frozenSetNumbers" i wyswielt jego zawartosc
#   6. stworz krotke "nameAgePairs" zawierajaca pary (imie, wiek), na jej podstawie
#   utworz slownik "ageDict". Wyswietl slownik, potem wyswietl wiek osoby o imieniu "Marek"

numbers = [7,8,9,10,11,12]
print("Zawartość numbers:", numbers)

tupleNumbers = tuple(numbers)
print("Zawartość tupleNumbers: ", tupleNumbers)

mixedList = ["tekst", 2137, 67.69]
print("Zawartość mixedList: ", mixedList)

setMixed = set(mixedList)
print("Typ setMixed: ", type(setMixed))
print("Zawartość setMixed: ", setMixed)

frozenSetNumbers = frozenset(tupleNumbers)
print("Typ frozenSetNumbers: ", type(frozenSetNumbers))
print("Zawartość frozenSetNumbers: ", frozenSetNumbers)

nameAgePairs = (("Karol", 21), ("Jan", 37), ("Paweł", 67), ("Marek", 69))
ageDict = dict(nameAgePairs)
print("Zawartość słownika: ", ageDict)
print("Wiek Marka: ", ageDict["Marek"])
