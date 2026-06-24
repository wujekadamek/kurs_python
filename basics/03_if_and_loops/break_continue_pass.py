data = [0,1,2,3,4,5,6,7,8,9]

for i in data:
    if i == 3:
        break
    print(i * 2)

print("")

for i in data:
    if i == 3 or i == 5:
        continue
    print(i)

if 10 > 2:
    print("10 > 2")
else:
    pass