def main():
    wzrost = float(input("Podaj swój wzrost (w metrach): "))
    if wzrost <=0:
        print("Wzrost musi byc wiekszy od 0!")
        return
    
    waga = float(input("Podaj swoją wagę (w kilogramach): "))
    if waga <=0:
        print("Waga musi byc wieksza od 0!")
        return

    bmi = waga / (wzrost) ** 2

    print(f"BMI dla wzrostu {wzrost} metra oraz wagi {waga} kg wynosi: {bmi:.2f}")

if __name__ == "__main__":
    main()
