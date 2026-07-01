# Stworz funkcje do konwersji czasu:
# 1. convertToSeconds przyjmujaca ilosc godzin oraz minut i zwracajaca ilosc sekund.
# jako parametry funkcji zapisz: hours, minutes. Skonwertuj 3 godziny i 25 minut na sekundy,
# pokaz wynik w konsoli.
#
# 2. convertToHours przyjmujaca parametr minutes oraz zwracajac ilosc godzin.
# Skonwertuj 120 minut na godziny i pokaz wynik w konsoli.

def convertToSeconds(h,m):
    return h * 3600 + m * 60


def convertToHours(minutes):
    return minutes / 60

print("3 godziny i 25 minut to", int(convertToSeconds(3,25)), "sekund.")
print("120 minut to", int(convertToHours(120)), "godzin.")