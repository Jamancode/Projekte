
# supervised lerning:
# Kassifikation über einen Klassifokator
# Binärer klassifikatior

# Trainingsdaten
# mit Feature + Ausgabe
# Mit sogenannten Label also in deim Beispiel "Hund" oder "nicht Hund"
# immer nur ein Label pro Bild!!!  


beine = 4             # Integer = int
groesse = 35.6        # Float   = float
breite = 34.2         # Float   = float

farbe = "Braun"       # String  = str
label = "Hund"        # String  = str

# 1. SETS
# erstellung eines " SETS " ein set ist eine zusammenfassung von verschiedenen charakteristiken zu einer gruppe von Daten in direkten zusammenhang zu stellen.
# * es gibt verschiedene Datentypen für Mengen
# * hängt von Daten und Anwendungen ab
# * Sets sind "ungeordnete Mengen" -> Reihenfolge ist nicht definiert!
# * Datentypen haben eingebaute Funktionen
# * Duplikate werden nur einmal gespeichert
# zum beispiel hier

# satz = {beine, groesse, breite, farbe, label}

# auch genauso möglich wäre

# satz = {4, 35.6, 34.2, "Braun", "Hund"}

# 2. Tupel
# *  Sind geordnete Mengen
# * Werte in Sets und Tupel sind nicht änderbar!

# tupel = (4, 35.6, 34.2, "Braun", "Hund")

# 3. Listen
# --> Reihenfolge der Werte ist Wichtig

# liste = [4, 35.6, 34.2, "Braun", "Hund"]

# 4. Dictionaries "Datentyp für Mengen" = ist ein Wörterbuch
# * Werte haben Schlüssel
# * ungeordnete Menge
# * --> keine doppelten Schlüssel!

data = {
    'beine': 4,
    'groesse': 35.6,
    'breite': 34.2,
    'farbe': "Braun",
    'lable': "Hund",
    'breite': 28.3,
}
# print(data ['groesse'])
# print(data ['farbe'])
print(data ['breite'])

# Mengen von Mengen

groesse = [35.4, 28.6, 23.9, 34.6, 45.6]

breite = [21.9, 18.7, 16.4, 34.2, 25.6]

beine = [4, 4, 4, 4, 4]

farbe = ["Braun", "Braun", "Beige", "Beige", "Grau"]

label = ["Hund", "Hund", "nicht Hund", "Hund", "nicht Hund"]

data = {
    'breite': breite,
    'groesse': groesse,
    'beine': beine,
    'farbe': farbe,
    'lable': label,
}
print(data['breite'])
