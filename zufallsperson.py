from pyzufall.person import Person
p1 = Person()
 
print(p1)

x = "männlich" if p1.geschlecht == 1 else "weiblich"

print("Vorname: " + p1.vorname)
print("Nachname: " + p1.nachname)
print("Geschlecht: " + x)
print("Geburtsdatum: {} Alter: {}".format(p1.geburtsdatum, p1.alter))
print("Wohnort: " + p1.wohnort)
print("E-Mail: " + p1.email)
print("Beruf:: " + p1.beruf)

del p1