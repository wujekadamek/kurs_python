# Zadanie: Zarządzanie stanem konta użytkownika
#
# Cel: Napisz program do zarządzania stanem konta użytkownika, który pozwala na
# dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program
# powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz
# zawierać funkcje do modyfikacji tego stanu i wyświetlania go. 
#
# Kroki do wykonania:
# 1) Zdefiniuj globalną zmienną accountBalance z wartością początkową 0.
# 2) Napisz funkcję addFunds, która przyjmuje kwotę do dodania do konta.
#    Funkcja ta powinna modyfikować globalną zmienną accountBalance.
# 3) Napisz funkcję withdrawFunds, która przyjmuje kwotę do wypłaty z konta.
#    Sprawdź, czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat.
# 4) Napisz funkcję displayBalance, która wyświetla aktualny stan konta.
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlenie stanu)
#    i odpowiednio zareaguj, wywołując odpowiednią funkcję.
#
# Rozwiązanie:

accountBalance = 0
def addFunds(amount):
    global accountBalance
    accountBalance += amount
    print("Dodano środki do konta: ", amount , "Nowy stan konta: ", accountBalance)

def withdrawFunds(amount):
    global accountBalance
    if amount > accountBalance:
        print("Nie można wypłacić środków - brak wystarczających środków na koncie.")
    else:
        accountBalance -= amount
        print("Wypłacono ", amount , " z konta. Nowy stan konta: ", accountBalance)

def displayBalance():
    global accountBalance
    print("Aktualny stan konta: ", accountBalance)
          
while True:
    print("\nWybierz działanie:")
    print("1. Dodaj środki")
    print("2. Wypłać środki")
    print("3. Wyświetl stan konta")
    print("4. Zakończ")
    
    choice = input("Wybierz opcję (1-4): ")
    
    if choice == "1":
        amount = float(input("Podaj kwotę do dodania: "))
        addFunds(amount)
    elif choice == "2":
        amount = float(input("Podaj kwotę do wypłaty: "))
        withdrawFunds(amount)
    elif choice == "3":
        displayBalance()
    elif choice == "4":
        print("Zakończono program.")
        break
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")