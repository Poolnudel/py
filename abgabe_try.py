# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:32:31 2022

@author: jakob.gattung

Treiber installieren (Anaconda Prompt):
    pip install mysql-connector-python
    pip install pyzufall
    
DB erstellen
    CREATE DATABASE pyPoolnudel
"""

from mysql.connector import connect
from pyzufall.person import Person
import random

conn = connect(host="localhost",
               user="root",
               passwd="",
               db="pyPoolnudel")

def createTabellen():
    cursor = conn.cursor()
    
    cursor.execute("""CREATE OR REPLACE TABLE `kunde` (
                    `ID` int(11) NOT NULL,
                    `vorname` varchar(30) DEFAULT NULL,
                    `nachname` varchar(30) DEFAULT NULL,
                    `geburtsdatum` varchar(30) DEFAULT NULL,
                    `age` int(11) DEFAULT NULL,
                    `geschlecht` varchar(30) DEFAULT NULL,
                    PRIMARY KEY (`ID`)
                    )
                """)
    cursor.execute("""CREATE OR REPLACE TABLE `konto` (
                    `IBAN` varchar(35) NOT NULL,
                    `kunde_ID` int(11) NOT NULL,
                    `wohnort` varchar(30) DEFAULT NULL,
                    `beruf` varchar(30) DEFAULT NULL,
                    `email` varchar(30) DEFAULT NULL,
                    `guthaben` int(11) DEFAULT NULL,
                    PRIMARY KEY (`IBAN`)
                    )
                """)
    cursor.close()
    #FOREIGN KEY (`kunde_ID`) REFERENCES `kunde` (`ID`)
    
def getValue(min, max):
    wert = random.randrange(min,max)
    return wert
    
def generatPerson(amount):
    i = 0
    
    while i <= amount:
        p1 = Person()
        
        x = "männlich" if p1.geschlecht == 1 else "weiblich"
        
        ranID = getValue(1, amount)
        
        guthaben = random.randrange(0,1000000)
        
        Bankleitzahl = "{} {}".format(getValue(1000, 9999), getValue(1000, 9999))
        Kontonummer = "{} {} {}".format(getValue(1000, 9999), getValue(1000, 9999), getValue(10, 99))
        
        Prufziffer = getValue(30, 60)
        
        IBAN = "DE{} {} {}".format(Prufziffer, Bankleitzahl, Kontonummer)
        
        insertKunde(i,p1,x)
        insertKonto(p1,IBAN,ranID,guthaben)
        
        del p1
        i +=1
        
def insertKunde(ID,p1,x):
    #print("KUNDE: {},{},{},{},{},{}".format(ID,p1.vorname,p1.nachname,p1.geburtsdatum,p1.alter,x))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO kunde (ID,vorname,nachname,geburtsdatum,age,geschlecht) VALUES ({},'{}','{}','{}',{},'{}')"
                   .format(ID,p1.vorname,p1.nachname,p1.geburtsdatum,p1.alter,x))
    cursor.close()


def insertKonto(p1,IBAN,ranID,guthaben):
    #print("KONTO: {},{},{},{},{},{}".format(IBAN,ranID,p1.wohnort,p1.beruf,p1.email,guthaben))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO konto (IBAN,kunde_ID,wohnort,beruf,email,guthaben) VALUES ('{}',{},'{}','{}','{}',{})"
                    .format(IBAN,ranID,p1.wohnort,p1.beruf,p1.email,guthaben))                    
    cursor.close()
    
    
    
    
createTabellen()
generatPerson(1000)

conn.commit()
conn.close()
