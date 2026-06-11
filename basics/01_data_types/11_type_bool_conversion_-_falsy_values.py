# falsy values, czyli wartosci, ktore daja False przy konwersji na boolean:

print(bool())           # <-- brak wartosci daje zawsze False
print(bool(False))      # <-- recznie wstawiona wartosc False
print(bool(0))          # <-- wartosc zero tez daje False
print(bool(0.0))        # <-- j.w.
print(bool( ( ) ) )     # <-- pusta krotka tez daje False
print(bool( [ ] ) )     # <-- pusta lista tez daje False
print(bool( { } ) )     # <-- pusty zbior tez daje False
print(bool( "" ) )      # <-- pusty lancuch tez daje False
print(bool( None ) )    # <-- pusta wartosc tez daje False

# ponizsze daja True:
print(bool(True))
print(bool(10))
print(bool(-10))
print(bool(-2.137))
print(bool((1,2,3)))
print(bool([0]))
print(bool({0}))
print(bool("cos"))