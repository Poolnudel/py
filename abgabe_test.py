# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:26:59 2022

@author: jakob.gattung
"""

from mysql.connector import connect
from pyzufall.person import Person
import random

# Verbuindungsparameter
conn = connect(host="localhost",
               user="root",
               passwd="",
               db="random")

# Personen schleife

i = 0

while i <= 1000:
    p1 = Person()

    x = "männlich" if p1.geschlecht == 1 else "weiblich"

    print("Vorname: " + p1.vorname)
    print("Nachname: " + p1.nachname)
    print("Geschlecht: " + x)
    print("Geburtsdatum: {} Alter: {}".format(p1.geburtsdatum, p1.alter))
    print("Wohnort: " + p1.wohnort)
    print("E-Mail: " + p1.email)
    print("Beruf:: " + p1.beruf)

    ranID = random.randrange(1,1000)
    guthaben = random.randrange(0,1000000000)
    
    Prufziffer = random.randrange()
    Bankleitzahl = random.randrange(1000000000,9999999999)
    Kontonummer = random.randrange(1000000000,9999999999)
    
    IBAN = "DE{}{}{}".format(Prufziffer, Bankleitzahl, Kontonummer) Prufziffer + str(Bankleitzahl) + Kontonummer

    # Datensätze schreiben

    # INSERT Kunden
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO kunden (Vorname,Nachname,Geschlecht,Geburtsdatum,Alter) VALUES
                    ('p1.vorname,p1.nachname,x,p1.geburtsdatum,p1.alter')""")
    cursor.close()

    # INSERT Konten
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO konten (ID_kunde,Wohnort,Beruf,E-Mail,Guthaben) VALUES
                    ('ranID,p1.wohnort,p1.beruf,p1.email,IBAN,guthaben')""")
    cursor.close()


    del p1