print("Hello " + "World!") # <-- Hello World!
print("Hello" * 3) # <-- powtorzy Hello x3

string = "Hello World!"
print(string[0]) # <-- H
print(string[0:5]) # <-- Hello
print("Hello" in string) # <-- True
print("Hello" not in string) # <-- False

multline = """line 1
line 2
line 3
"""

print("Ala".capitalize()) # <-- Ala
print("Ola Ma kota. Ola ma psa.".count("Ola")) # <-- 2
print("Hello".center(20, "-")) # <-- wypelni myslnikami przestrzen lewo-prawo
print(string.startswith("Hello")) # <-- True
print(string.endswith("World")) # <-- False

print(string.find("Ola")) # <-- "-1", jeżeli nie znajdzie
print(string.find("World")) # <-- 6 - wartość indeksu, pod którym jest World
print("Ola ma psa. Ola ma kota.".rfind("Ola")) # 12
print("213769420".isalnum()) # <-- True
print("213769420.".isalnum()) # <-- False
print("213769420h".isalnum()) # <-- False

print("213769420.".isalpha()) # <-- False
print("Kot ".isalnum()) # <-- False
print("Kot".isalnum()) # <-- True
print("Kot2".isalnum()) # <-- False

print("test".islower()) # True
print("tesT".islower()) # False
print("TEST".isupper()) # True
print("test".isspace()) # False
print(" \n \t  ".isspace()) # True

print("-|".join(["Ola", "Ala", "Adam"])) # <-- doda "-| na koniec każdego elementu listy"
print("Hello World".lower()) # <-- hello world
print("Hello World".upper()) # <-- HELLO WORLD
print("Hello World".swapcase()) # <-- hELLO wORLD
print("   \t \n    Hello  \t \n  World \t \n \n\n   ".lstrip()) # <-- Likwiduje białe znaki z lewej
print("   \t \n    Hello  \t \n  World \t \n \n\n   ".rstrip()) # <-- Likwiduje białe znaki z prawej
print("   \t \n    Hello  \t \n  World \t \n \n\n   ".strip()) # <-- Likwiduje białe znaki z obu, ale w środku nic nie rusza

print("Ola ma psa. Ola ma kota".replace("Ola", "Kasia")) # <-- zamienia Ola na Kasia

print("My name is {myName}, I am from {country}".format(myName = "Karol", country = "Watykan"))
print("My name is {myName}, my postal code is {postalCode}".format(myName = "Karol", postalCode = 2137))
print("My name is {0}, my postal code is {1}".format("Karol", 2137))

