#set z wartościami: Ania, Kasia, Ola, Karol, Daniel, Zuza
#dodaj: Olek, Basia, Kasia, Karol, Zuza, Paulina
#pokaż wielkość set
#pokaż wszystkie elementy w set za pomocą pętli for


set = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}
set.add("Olek")
set.add("Basia")
set.add("Kasia")
set.add("Karol")
set.add("Zuza")
set.add("Paulina")

print(len(set))

for v in set:
    print(v)