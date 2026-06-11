for v in [1,2,3,4]:
    print(v * 2)

for v in ("Ania", "Ola", "Rafał"):
    print(v)

for el in {3,4,5,6,"Jan"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("Pętla zakończona.")

dictionaryData = {"Papież" : "papaj@watykan.com", "Karol" : "bestia@wadowice.pl"}
for key in dictionaryData:
    print(key)

for key in dictionaryData.keys():
    print(key)

for key in dictionaryData.keys():
    print(dictionaryData[key])

for key, value in dictionaryData.items():
    print(key, " : ", value)

for v in dictionaryData.values():
    print(v)