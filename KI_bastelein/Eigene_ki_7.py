# https://www.youtube.com/watch?v=k7rxRtMVskc

# funtion des Perzeptron w * x + b

# Skalarprodukut = Multipikation + Addition
# b = bias (voreingenmmenheit) hängt nicht vom eingenagssignal ab


#------------------------------
# Operatoren der Arithmetik:

# Addition -> y = x[0] + x[1]
# Subtraktion -> y = x[0] - x[1]
# Multiplikation -> y = x[0] * w[0]
# Division -> y = x[0] / w[0]

# Operationen auf Vaiablen:
# x[0] += 2
# x[0] -= 2
# x[0] *= 2
# x[0] /= 2

# Exponention opperator -> x[0]² wäre y = x[0] **2
# Abgerundete Division -> x[0] = 37.92655435
#                         x[0] // 2 = 18
# Modulo Operator (rest) -> y = x[0] % 5
# hiemit kann man         print (y)
# grande oder ungrade     2.92655435

# Vergleichendeoperatoren:

# (größer)
# hund = y > 1  "also wenn y größer 1 wäre also = True"

# (kleiner)
# hund = y < 1 "also wenn y kleiner als 1 wäre"

# (gleich)
# hund = y == 1  "also wenn y gleich 1 wäre"

# (ungleich)
# hund = y != 1 "also wenn y ungleich 1 wäre"

# (größergleich)
# hund = y >= 1 "wenn y größer oder gleich 1 wäre"

# (kleinergleich)
# hund = y <= 1 "wenn y kleiner und gleich (genau) 1 wäre"

# Gilt auch für Variablen hier Beispiel (größergleich)
# hund = y >= x "wenn y größer oder gleich x wäre"

# Boolsche Operatoren:
#Verarbeiten mehrere Booleans zu eiem booleschen Wert!

# and       hund = y >= 0 and y != 0  " hier wäre y >= 0 True wenn y = 0 als gegeben wäre und y != 0 wäre False also ist die gesammte gleich und False"

# or        hund = y >= 0 or y != 0  " hier wäre y >= 0 True wenn y = 0 als gegeben wäre oder y != 0 wäre False also ist die gesammte gleich und True"

# not    hund = not y == 0 <-> y != 0  " heir wenn y == 0 True ist wäre das ergebniss hier False"

#Logische Operatoren

# is -> == " also print(5 is 6) -> Flase wäre das selbe wie print(5 == 6) -> Flase
#  is not -> == " also print(5 is not 6) -> True wäre das selbe wie print(5 != 6) -> True

# in "prüft ob ein wert IN einer funktion oder menge vorhanden ist; also print(0 in feature) -> True




#Strings
# kann man nur addieren
# print('man kann stings ' + 'auch addieren')
# zahlen und stings kombinieren
# print('Der wert von x[0] ist' + str(x[0]))
# Der wert von x[0] ist 37.92655435
#----------------------------------------------------------

# w1*x1 + w2*x2 + b

import numpy as np

feature = np.array([[4.0, 37.92655435, 23.90101111],
                    [4.0, 35.88942857, 22.73639281],
                    [4.0, 29.49674574, 21.42168559],
                    [4.0, 32.48016326, 21.7340484 ],
                    [4.0, 38.00676226, 24.37202837],
                    [4.0, 30.73073988, 22.69832608],
                    [4.0, 35.93672343, 21.07445241],
                    [4.0, 38.65212459, 20.57099727],
                    [4.0, 35.52041768, 21.74519457],
                    [4.0, 37.69535497, 20.33073640],
                    [4.0, 33.00699292, 22.57063861],
                    [4.0, 33.73140934, 23.81730782],
                    [4.0, 43.85053380, 20.05153803],
                    [4.0, 32.95555986, 24.12153986],
                    [4.0, 36.38192916, 19.20280266],
                    [4.0, 36.54270168, 20.45388966],
                    [4.0, 33.08246118, 22.20524015],
                    [4.0, 31.76866280, 21.01201139],
                    [4.0, 42.24260825, 20.44394610],
                    [4.0, 29.04450264, 22.46633771],
                    [4.0, 30.04284328, 21.54561621],
                    [4.0, 18.95626707, 19.66737753],
                    [4.0, 18.60176718, 17.74023009],
                    [4.0, 12.85314993, 18.42746953],
                    [4.0, 28.62450072, 17.94781944],
                    [4.0, 21.00655655, 19.33438286],
                    [4.0, 17.33580556, 18.81696459],
                    [4.0, 31.17129195, 17.23625014],
                    [4.0, 19.36176482, 20.67772798],
                    [4.0, 27.26581705, 16.71312863],
                    [4.0, 21.19107828, 19.00673617],
                    [4.0, 19.08131597, 15.24401994],
                    [4.0, 26.69761925, 17.05937466],
                    [2.0, 4.44136559 , 3.52432493 ],
                    [2.0, 10.26395607, 1.07729281 ],
                    [2.0, 7.39058439 , 3.44234423 ],
                    [2.0, 4.23565118 , 4.28840232 ],
                    [2.0, 3.87875761 , 5.12407692 ],
                    [2.0, 15.12959925, 6.26045879 ],
                    [0.0, 5.93041263 , 1.70841905 ],
                    [0.0, 4.25054779 , 5.01371294 ],
                    [0.0, 2.15139117 , 4.16668657 ],
                    [0.0, 2.38283228 , 3.83347914 ]])

#label = np.concatenate((np.ones(21), np.zeros(22)))
#print(label)
x = feature[0, 1:]
x = np.insert(x,2,1)
#w = np.zeros(3)
w = np.random.rand(3)



print(x)
print(w)

#hier 3 wege um das selbe zu machen also w * x + b
y = w[0] * x[0] + w[1] * x[1] + w[2] * x[2]
y2 = np.dot(w, x)
y3 = w @ x

print(y)
print(y2)
print(y3)
print(x + w)

print('balalal 1' + '    ' + str(x[0]))


