# 1. Oblicz zwrot z inwestycji po roku, zmienne ponizej:
# - capital - 5000
# - rateOfInterest - 0.08 czyli 8%
# - inflationRate - 0.15 czyli 15%

# 2. Oblicz zwrot z inwestycji oraz o ile spadla wartosc kapitalu
# z uwagi na inflacje, pokaz te kwoty w konsoli

# 3. Dodaj do kapitalu zwrot z inwestycji oraz odejmij utracony kapital
# z uwagi na inflacje, pokaz wartosc koncowa w konsoli

capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

profit = rateOfInterest * capital
print("Zysk z inwestycji wynosi: ", profit)

loss = capital * inflationRate
print("Strata z inwestycji wynosi: ", loss)

investmentReturn = capital + profit - loss
print("Wartość kapitału po inwestycji: ", investmentReturn)
