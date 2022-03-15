from pyzufall.person import Person
p1 = Person()
 
x = (p1.geschlecht "männlich" if "weiblich" else);

print(p1)

print("Vorname: " + p1.vorname)
print("Geschlecht: " + str(x))
print("Nachname: " + p1.nachname)
print("Geburtsdatum: {} Alter: {}".format(p1.geburtsdatum, p1.alter))
print("Wohnort: " + p1.wohnort)
print("E-Mail: " + p1.email)
print("Beruf:: " + p1.beruf)

del p1