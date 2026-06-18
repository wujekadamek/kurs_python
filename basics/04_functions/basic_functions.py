def addNumber(a, b):
    return a + b

def subNumber(a, b):
    return a - b

def multiplyNumber(a, b):
    return a * b

def add4numbers(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

print(addNumber(21,37))

number = subNumber(69,67)
print(number)

number = multiplyNumber(4,20)
print(number)

sum = add4numbers(1, number, addNumber(11,4), 9)
print(sum)