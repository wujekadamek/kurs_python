def printCar(brand, /, name = "concept", *, year = 1960, color = "black"):
    print(brand, name, year, color)

printCar("Ford", "Mustang", year = 1973, color = "blue")
# printCar(brand = "Ford", name = "Mustang", "blue", year = 1973) # <== błąd