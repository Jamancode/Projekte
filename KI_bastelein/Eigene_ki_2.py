
# Erste Zielanwendung klassifikatoren = mit "Binäre Klassifikatoren", die in zwei Gruppen sortieren.

# Eine algorithmus methode ist "Perzeptron" = Beliebiges Werkzeug, um so einen Kassifikatior zu bauen.

# zur erkennung von Hunden, übung Bilder in 2 kategorien sortieren.
# Also "Hunde" und "nicht_Hunde".

# Grundlage "Perzeptron":
# McCulloch-Pitts Neutron von 1943 weiter entwickelt von Frank Rosenblatt 1958 zur Perzeptron Lernregel

#schematik Perzeptron

# Input1  -->   X1              Ist ein Mathematisches Modell
#                   _w1_>
# Input2  -->   X2
#                   -w2->   Y  --> output
# Input3  -->   X3  -w3->
#
# Input m -->   Xm -w4  >
#

# Perzeptron Eingabe (Perzeptron nimmt nur reelle Zahlen als Eingabe! -> Bilder in Zahlen formantieren)
# definiert in  "Features" (Merkmale = Statistiken = Features = charakteristiken) zb. Anzahl der beine, größe, breite oder farbe.
# Beispiel für Hund mit erläuterung zu Datentypen
# Datentypten sind Kategorien von Werten, die in einer Progammiersprache verschieden genutzt werden können und sogar verschieden gespeichert werden.


beine = 4             # Integer = int
groesse = 35.6        # Float   = float
breite = 34.2         # Float   = float

farbe = "Braun"       # String  = str

beine = int(4.6)      # int rundet immer ab so das das ergebniss 4 sein wird.
print(beine)

# github mit code beispielen " https://github.com/simpleclub/startup_teens_machine_learning ". 