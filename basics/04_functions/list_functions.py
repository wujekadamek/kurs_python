list1 = [0,1,2,3,4,5]
print(list1[3]) # <-- 3
print(list1[1:5]) # <-- [1,2,3,4]

list1[0] = 9 # <-- zamienia 0 na 9
print(list1) # <-- [9,1,2,3,4,5]

del list1[1] # <-- usuwa 1
print(list1) # <-- [9,2,3,4,5]

print(len(list1)) # <-- ilosc elementow liczac od 0
print(min(list1)) # <-- najmniejszy element listy
print(max(list1)) # <-- najwiekszy element listy

print(list(("Ala", "Ola"))) # <-- ["Ala", "Ola"]

print([0,1,2] + [3,4]) # <-- [0,1,2,3,4]
print([0,1] * 3) # <-- [0,1,0,1,0,1]

print(9 in [0,1]) # <-- False
print(9 not in [0,1]) # <-- True

list1.append(99) # <-- dodaje 99 na koniec listy
print(list1) # <-- [9,2,3,4,5,99]
print(list1.count(3)) # <-- liczy ilosc wystapien liczby w nawiasie

list1.extend([7,8,9]) # <-- dodaje elementy [w nawiasie kwadratowym] na koniec listy
print(list1) # <-- 9,2,3,4,5,99,7,8,9

list1.insert(3,9) # <-- pod indeks 3 wstawiamy wartosc 9, reszta sie przesuwa
print(list1) # <-- [9, 2, 3, 9, 4, 5, 99, 7, 8, 9]

print(list1.index(9)) # <-- zwraca pierwszy indeks szukanej liczby w nawiasie, czyli w tym przypadku "0"
print(list1.index(99)) # <-- 6

list1.reverse() # <-- odwrocenie kolejnosci
print(list1) # <-- [9, 8, 7, 99, 5, 4, 9, 3, 2, 9]

list1.sort() # <-- sortuje od najmniejszej do najwiekszej
print(list1) # <-- [2, 3, 4, 5, 7, 8, 9, 9, 9, 99]

num = list1.pop() # <-- zwraca ostatnia wartosc z listy i ja usuwa
print("num", num) # <-- num 99
print(list1) # <-- [2, 3, 4, 5, 7, 8, 9, 9, 9]

