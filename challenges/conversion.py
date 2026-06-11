#1. stworz zmienna decimalNum z wartoscia dziesietna 45.6789
#2. skonwertuj decimalNum do typu integer i zapisz wynik w zmiennej
#   wholeNum. Wyswielt typ zmiennej wholeNum oraz jej wartosc
#3. przeksztalc lancow znakow "4321" do typu calkowitego
#   i wyswielt typ po konwersji
#4. stworz zmienna wholeNum2 z wartoscia calkowita 123, skonwertuj
#   ja do typu float i wyswielt typ oraz zawartosc
#5. skonwertuj lancuch znakow "98.76" do typu float i wyswielt
#   typ i zawartosc
#6. skorzystaj z funkcji print do wyswietlenia ciagu tekstu
# zawierajacego wartosc wholeNum2, laczac ja z tekstem oraz innymi
# typami danych, np. float, list. Uzyj dwoch metod: konkatenacji
# za pomoca funkcji str() oraz oddzielania wartosci przecinkami w funkcji print

decimalNum = 45.6789
wholeNum = int(decimalNum)
print("Typ zmiennej wholeNum to: ", type(wholeNum))
print("Wartość zmiennej wholeNum: ", wholeNum)

intNum = int(" 4321 ")
print("Typ łańcucha po konwersji: ", type(intNum))

wholeNum2 = 123
floatNum = float(wholeNum2)
print("Typ zmiennej floatNum: ", type(floatNum))
print("Zawartość floatNum: ", floatNum)

floatNum2 = float("98.76")
print("Typ zmiennej floatNum2: ", type(floatNum2))
print("Wartość zmiennej floatNum2: ", floatNum2)

print("Wartość wholeNum2: " + str(wholeNum2) + "," + str(45.0) + "," + str([2,1,3,7]))
print("Wartość wholeNum2: ", wholeNum2, 45.0), [2,1,3,7]
