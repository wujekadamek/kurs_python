setData = {2, 1, 3, 7, 69, 420}
setData.add(67)
setData.discard(69)
print(type(setData))
print(setData)

for v in setData:
    print(v)

frozenData = frozenset(setData)
print(type(frozenData))

#frozenData.add(345678) # <-- nie da się, bo frozen jest niemutowalny

for value in frozenData:
    print(value)