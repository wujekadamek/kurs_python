listData = [1,2,3,4,5,6]

tupleData = tuple(listData)
print(tupleData)

otherList = list(("Ola", 23, 2137))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

tupleData = (("Jan", 420), ("Pawel", 69))

dictData = dict(tupleData)
print(dictData)
print(dictData["Jan"])