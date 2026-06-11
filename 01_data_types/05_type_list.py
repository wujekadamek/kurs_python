list = ["Ola", "Ania", 23, 99, "Rafal"]
print(type(list))
print(list)

print(list[0])
print(len(list))
print(list[4])
print(list[len(list)-1])

print(list[-1])
print(list[-2])

print (list[1:4])
print (list[2:])

list[0] = "Wadowice"
print(list)

del list[2]
print(list)

print(99 in list)
print("Rafal" in list)
print("Ola" in list)

if "Ania2" in list:
    print("Ania jest w liscie")
    print("Kod idzie dalej")

print("Kod idzie jeszcze dalej")

for v in list:
    print(v)

data = [
    ["Daniel", "Rafal"],
    ["Jan", "Pawel"],
    ["Karol", "JP2GMD"]
]

print(len(data))

print(data[1][0])
print(data[2][1])

data1 = [2, 1, 3]
data2 = [7, 6, 9]

numbers = data1 + data2
print(numbers)

numbersX2 = numbers * 2
print(numbersX2)