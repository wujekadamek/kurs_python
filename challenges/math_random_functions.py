# Zadanie - symulacja kosztów podróży
# W tym zadaniu skorzystasz z funkcji matematycznych i losowych
# do symulacji kosztów podróży. Użyj danych typów, funkcji matematycznych
# oraz funkcji z modułu random do wyliczenia i przewidzenia kosztów.
#
#1. Stwórz zmienną "distance" z losową wartością od 100 do 1000, która
# oznacza dystans w kilometrach do pokonania.
#2. Oblicz spodziewane spalanie na podróż, przyjmując, że samochód
# spala średnio 7 litrów na 100 km. Użyj zaokrąglenia w górę.
#3. Przyjmij cenę paliwa za litr jako losową wartość zmiennoprzecinkową
# między 4.5 a 5.5. Zaokrąglij cenę do dwóch miejsc po przecinku.
#4. Oblicz całkowity koszt paliwa na podróż.
#5. Jeśli koszt paliwa przekracza 400 zł, wyświetl komunikat o wysokich
# kosztach podróży. W przeciwnym razie, poinformuj o przystępnych kosztach.

import math
import random

distance = random.randint(100, 1000)
fuelConsumptionPer100km = 7
expectedFuelConsumption = math.ceil(distance / 100) * fuelConsumptionPer100km
fuelPrice = round(random.uniform(4.5, 5.5), 2)
totalCost = round(expectedFuelConsumption * fuelPrice, 2)
print("Koszt podróży: ", totalCost)

if totalCost > 400:
    print("Koszty podróży są wysokie.")
else:
    print("Koszty podróży są przystępne.")

