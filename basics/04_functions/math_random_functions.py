import math
import random
print(type(str(12)))
print(type(str([12,34])))

number = int("123")
print(type(number))

number += 10
print(number)
print("123" + "10")

floatNum = float("45.67")
print(type(floatNum))
floatNum = floatNum * 2
print(floatNum)

print(abs(9))
print(abs(-9.1))

print(math.ceil(11.00000001)) # 12
print(math.ceil(9.99999999)) # 10
print(math.ceil(-1.00000001)) # -1
print(math.ceil(-1.99999999)) # -1

print(math.floor(11.00000001)) # 11
print(math.floor(11.99999999)) # 11
print(math.floor(5.12)) # 5
print(math.floor(-5.12)) # -6

print(max(10,1,-9,33,21,37,0)) # 37
print(max([10,1,-9,33,21,37,0])) # 37
print(max((10,1,-9,33,21,37,0))) # 37
print(min((10,1,-9,33,21,37,0))) # -9
print(min([10,1,-9,33,21,37,0])) # -9
print(min(10,1,-9,33,21,37,0)) # -9

print(4 ** 3) # 64
print(pow(4,3)) # 64
print(math.sqrt(128)) # 11.313708498984761
print(round(12.34567, 3)) # 12.346
print(round(12.34567, 2)) # 12.35
print(round(12.34567, 1)) # 12.3

print(random.random()) # 0.0 <= x < 1.0
print(random.random() * 100) # 0.0 <= x < 100.0
print(int(random.random() * 100)) # 0 <= x < 100
print(random.choice([1,2,3,4,5,6])) # losowy element z listy
print(random.choice(["Ola", "Jan", "Paweł"])) # losowy element z listy

print(random.randrange(-10, 30, 5))

listData = [1,2,3,4,5,6]
random.shuffle(listData)
print(listData)
