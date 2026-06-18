# immutable: int, float, bool, str, frozenset
# mutable: list, set, dictionary

def modifyStr(strData):
    strData += "!"
    print(id(strData))
    print(strData)
    print(id(strData))

string = "Hello"

modifyStr(string)
print(id(string))
print(string)
print(id(string))

# mutable: list, set, dictionary
def modifyList(listData):
    print(id(listData))
    listData = [1,2,3,4,5,6]
    listData.append(10)
    print(id(listData))

listValue = [0,1,2]
print(id(listValue))
modifyList(listValue)