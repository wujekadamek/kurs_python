#zmienna config, która jest słownikiem
#website - example.com
#dbType - mysql
#dbUser - admin
#dbPassword - 12345

#pokaż ilość elementów słownika
#pokaż wartość klucza dbType
#pętla for in aby przejść po wszystkich elementach słownika w formacie:
#Klucz w config: website z wartością example.com

config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dbPassword" : "12345"
}

print("Ilość elementów słownika: ", (len(config)))
print("Wartość dbType: ", config["dbType"])

for key, value in config.items():
    print(key + ": " + value)