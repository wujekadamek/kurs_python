from functools import reduce

sum = lambda a,b: a + b

print(sum(21,37)) # <== 58
print(sum(10, 15)) # <== 25

def generateLambda(num):
    return lambda a: a * num
doubler = generateLambda(2) # <== 4

listData = [0,1,2,3]

result = list(map(lambda a: a * 3, listData)) # <== [0, 3, 6, 9]
print(result)

result = list(filter(lambda a: a > 1, listData)) # <== [2, 3]
print(result)

result = reduce(lambda x, y: x + " " + y, ("Ola", "Ania"))
print(result) # <== "Ola Ania"