# Zadanie: Kalkulator wieku psa na ludzkie lata
#
# Cel: Napisz program, który przeliczy wiek psa na ludzkie lata.

# Kroki do wykonania:
# 1. Poproś użytkownika o wprowadzenie wieku psa w latach i zapisz tę wartość do zmiennej.
# 2. Użyj instrukcji warunkowych, aby obliczyć wiek psa w ludzkich latach. 
#    - Pierwszy rok życia psa to 15 ludzkich lat. human_age = dog_age * 15
#    - Drugi rok życia psa to kolejne 9 ludzkich lat. human_age = 15 + (dog_age - 1) * 9
#    - Każdy kolejny rok to 5 ludzkich lat. 24 + (dog_age - 2) * 5
# 3. Jeśli podana wartość wieku psa jest mniejsza niż 0, wyświetl komunikat o błędzie.
# 4. Wyświetl wynik obliczeń w konsoli. 

humanAge = 0
dogAge = float(input("Podaj wiek psa (w latach): "))
if dogAge < 0:
    print("Wiek nie może być liczbą ujemną!")
elif dogAge <= 1:
    humanAge = dogAge * 15
    print("Ludzki wiek Twojego psa to:", humanAge, "lat.")
elif dogAge <= 2:
    humanAge = 15 + (dogAge - 1) * 9
    print("Ludzki wiek Twojego psa to:", humanAge, "lat.")
else:
    humanAge = 24 + (dogAge - 2) * 5
    print("Ludzki wiek Twojego psa to:", humanAge, "lat.")
