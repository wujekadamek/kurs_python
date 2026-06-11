# Wykorzystaj operator konkatenacji do laczenia stringow i list oraz zastosuj prosta instrukcje if.
# 1. Polacz 2 stringi firstName i lastName w jeden string fullName i wyswietl go. Dodaj miedzy nimi spacje.
# 2. Stworz 2 listy listOne z liczbami 1-3 i listTwo z liczbami 4-6. Polacz je w jedna liste combinedList i wyswietl
# 3. Jesli dlugosc combinedList jest wieksza od 5, wyswietl "Lista jest dluga".
# 4. Do zmiennej greeting dodaj string Hello a do niej fullName. Sprawdz, czy w greeting znajduje sie slowo Hello. Jesli tak, wyswietl pelne powitanie.


firstname = "Jan"
lastName = "Paweł"
fullName = firstname + " " + lastName
print(fullName)

listOne = [1,2,3]
listTwo = [4,5,6]
combinedList = listOne + listTwo
print(combinedList)

if len(combinedList) > 5:
    print("Lista jest dluga.")

greeting = "Hello " + fullName
if "Hello" in greeting:
    print(greeting)