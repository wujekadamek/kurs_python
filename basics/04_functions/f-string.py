age = 32
print("age:", age)

print(f"Wiek uzytkownika: {age} lat.")


pi = 3.141592
print(f"Wartosc liczby pi to w przyblizeniu {pi:.2f}") # <-- 2 miejsca po przecinku

list = ["jablko", "cytryna"]
print(f"Lista owocow: {list}")

person = {
    "name" : "Ania",
    "age" : 32
}
print(f"User: {person}, {person["name"]}")

a = 5
b = 10
print(f"Wynik dodawania liczb {a} i {b} to dokladnie: {a + b}")

score = 69
print(f"Test zakonczony {("sukcesem." if score >= 70 else "porazka.")}")