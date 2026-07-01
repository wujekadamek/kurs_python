# Zadanie: Wypisanbie elementow z listy list
#
#Cel: napisz program, ktory przechodzi przez zagniezdzona liste (liste list)
#
# Kroki do wykonania:
#
# 1. Stworz zmienna nested_list, ktora bedzie zawierac kilka list z roznymi typami elementow.
# 2. Uzyj zagniezdzonej petli for do przejscia przez wszystkie listy i ich elementy.
# 3. Wypisz kazdy element z kazdej listy.

nested_list = [
    [21,37,69,420],
    ["Jan", "Pawel", "Drugi"],
    ["Bestia", 2137, "Wadowice", 235876, True]
]

for listData in nested_list:
    for v in listData:
        print(v)