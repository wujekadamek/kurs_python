data = {"name" : "Ola", "city" : "Waw"}
print(data["name"])
dataPostalCode = "postalCode"
data[dataPostalCode] = 12345
print(data)
print(len(data))

del data["city"]
print(data)
data.clear()
print(data)

data = {"name" : "Kasia", "city" : "Krk"}
dataCopy = data.copy()
print(dataCopy)
print(data["name"] is dataCopy["name"]) # <-- True, bo odwoluje sie do elementu ze slownika, to tzw. plytka kopia
print(data is dataCopy) # <-- False, bo sprawdza czy te 2 slowniki sa w tym samym miejscu w pamieci

data2 = dict.fromkeys(("name", "city", "code"))
print(data2)

data3 = dict.fromkeys(("name", "city", "code"), 0)
print(data3)

print(data2.get("x", "DEFAULT"))

print("name" in data2) # <-- True
print(data2.keys())
print(data2.values())