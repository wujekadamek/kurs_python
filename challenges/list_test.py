data = [0, 1, 2, 3, 4, 5, 6]
print("Liczba elementów na liście: ", len(data))

del data[1]
print("Liczba elementów na liście po skasowaniu: ", len(data))

if 3 in data:
    print("Liczba 3 znajduje się na liście")

for v in data:
    print("Element listy: ", v)

for v in data:
    print("Element listy pomnożony przez 2: ", v * 2)
