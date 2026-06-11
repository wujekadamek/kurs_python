contacts = {
    "Olga" : "olga@przedszkole.pl",
    "Stasiu" : "stasiu@przedszkole.pl",
    "Szymon" : "szymon@przedszkole.pl"
    }

contacts["zosia"] = "zosia@przedszkole.pl"
contacts["megan"] = "megan@przedszkole.pl"
contacts["emilka"] = "emilka@przedszkole.pl"

print(contacts)
print(contacts["emilka"])
print(contacts["megan"])
print(type(contacts))
print(len(contacts))
print(contacts.keys)
print(contacts.values)

for key in contacts:
    print(key + " " + str(contacts[key]))

for key, value in contacts.items():
    print(key, " ", value)
