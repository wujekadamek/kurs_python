# Skorzystaj ze skroconych operatorow przypisania z operacja
# matematyczna, np. +=  -=  *=  /= itd
# Uwaga, po kazdej operacji wyswietl saldo w konsoli

# 1. Stworz zmienna balance z wartoscia poczatkowa 1000
# 2. Dodaj wartosc nowej pensji 7000
# 3. Odejmij 2000 kosztow za mieszkanie
# 4. Blad banku pomnozyl twoje saldo 3x
# 5. Odejmij 4000 na komputer
# 6. Bank zorientowal sie ze powstal blad i cofa ostatnie transakcje.
#   Dodaj do salda 4000, podziel saldo przez 3 i dopiero teraz odejmij 4000
# 7. Pokaz saldo koncowe

balance = 1000
print("Saldo początkowe: ", int(balance) , " PLN.")

balance += 7000
print("Saldo po wpływie pensji: ", int(balance) , " PLN.")

balance -= 2000
print("Saldo po opłatach za mieszkanie: ", int(balance) , " PLN.")

balance *= 3
print("Saldo po błędzie banku: ", int(balance) , " PLN.")

balance -= 4000
print("Saldo po zakupie komputera: ", int(balance) , " PLN.")

balance = (balance + 4000) / 3 - 4000
#balance += 4000
#print("Saldo konta wynosi: ", int(balance) , " PLN.")

#balance /= 3
#print("Saldo konta wynosi: ", int(balance) , " PLN.")

#balance -= 4000
print("Saldo po poprawieniu błędu banku: ", int(balance) , " PLN.")
