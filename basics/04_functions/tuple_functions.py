tuple1 = (1,2,3,4) + (5,) + tuple([6,7]) # <-- przy dodawaniu jednego elementu do krotki musi byc na koncu przecinek
print(type(tuple1))
print(tuple1) # <-- (1, 2, 3, 4, 5, 6, 7)

print((1,2) * 4) # <-- (1, 2, 1, 2, 1, 2, 1, 2)
print(9 in tuple1) # <-- False
print(tuple1[1]) # <-- 2
print(len(tuple1)) # <-- 7
print(min(tuple1)) # <-- 1
print(max(tuple1)) # <-- 7