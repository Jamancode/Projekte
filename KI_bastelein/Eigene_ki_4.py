# Strings konvertieren
# im beispiel lable aus Hund und nicht Hund 1 und 0 zu machen da Perzeptron nur mit zahlen klar kommt.
import numpy as np

groesse = [35.4, 28.6, 23.9, 34.6, 45.6,]
breite = [21.9, 18.7, 16.4, 34.2, 25.6,]
beine = [4, 4, 4, 4, 4,]
label = [1, 1, 0, 1, 0,]
#farbe = ["Braun", "Braun", "Beige", "Beige", "Grau"]


data = {
    'breite': breite,
    'groesse': groesse,
    'beine': beine,
    #'farbe': farbe,
    'lable': label,
}
print(data['breite'])
# hier erstellen wir aus Daten ein numpy array, weil dies optimiert ist mit zahlen und listen sehr schnell zu arbeiten.
groesse = np.array([35.4, 28.6, 23.9, 34.6, 45.6,])

groesse = np.array(data['groesse'])
print(groesse)
print("was neues")
#Erstellen einer "Matrize" Matrizen sind Listen in Listen.

feature = np.array([data['beine'], data['groesse'], data['breite']])

avg = np.average(data['breite'])

print(feature)        # hier sehen wir das wir listen in einer liste ausgeben können.
print(feature.shape)  # Hier sehen wir die verkürze Form hier 3 für Zeilen und 5 Spalten
print(feature.T)      # Hier wird "tranzponiert" das bedeutet das Zeilen und Spalten vertauscht werden.
print(avg)            # averge erzeugt den  mittelwert aus einer Liste