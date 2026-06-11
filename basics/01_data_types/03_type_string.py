str = "Hello world!"
print(str);
print(len(str))         # <-- pokaż długość str
print(type(str))        # <-- pokaż typ str

print(str[0])           # <-- pokaż pierwszy element / znak w str
print(str[len(str) -1]) # <-- pokaż ostatni element / znak w str
print(str[0:5])         # <-- pokaż ciąg znaków od 1-5 w str
print(str * 4)          # <-- pokaż str czterokrotnie
strX3 = str * 3
print(strX3)

str2 = str + " and Hello again!"
print(str2)

print(str2[6:])
print(str2[::3])

# kod w wielu liniach - potrójny cudzysłów:
multiLine = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia \t linia \" \\ " # nową linię dodajemy za pomocą " \n ",
                                                                    # wcięcie za pomocą " \t ". Backslash - " \\ "typ 
                                                                    # cudzysłów - " \" "

print(multiLine2)