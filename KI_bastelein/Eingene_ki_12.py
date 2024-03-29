# https://www.youtube.com/watch?v=Gg4-KNG76KI&list=PLIYzsTnFhywyjBon1_tE4ZGVzXAx5FpWr&index=6

# if - Statements
#
import numpy as np

feature = np.array([[37.92655435, 23.90101111],
                    [35.88942857, 22.73639281],
                    [29.49674574, 21.42168559],
                    [32.48016326, 21.7340484 ],
                    [38.00676226, 24.37202837],
                    [30.73073988, 22.69832608],
                    [35.93672343, 21.07445241],
                    [38.65212459, 20.57099727],
                    [35.52041768, 21.74519457],
                    [37.69535497, 20.33073640],
                    [33.00699292, 22.57063861],
                    [33.73140934, 23.81730782],
                    [43.85053380, 20.05153803],
                    [32.95555986, 24.12153986],
                    [36.38192916, 19.20280266],
                    [36.54270168, 20.45388966],
                    [33.08246118, 22.20524015],
                    [31.76866280, 21.01201139],
                    [42.24260825, 20.44394610],
                    [29.04450264, 22.46633771],
                    [30.04284328, 21.54561621],
                    [18.95626707, 19.66737753],
                    [18.60176718, 17.74023009],
                    [12.85314993, 18.42746953],
                    [28.62450072, 17.94781944],
                    [21.00655655, 19.33438286],
                    [17.33580556, 18.81696459],
                    [31.17129195, 17.23625014],
                    [19.36176482, 20.67772798],
                    [27.26581705, 16.71312863],
                    [21.19107828, 19.00673617],
                    [19.08131597, 15.24401994],
                    [26.69761925, 17.05937466],
                    [4.44136559 , 3.52432493 ],
                    [10.26395607, 1.07729281 ],
                    [7.39058439 , 3.44234423 ],
                    [4.23565118 , 4.28840232 ],
                    [3.87875761 , 5.12407692 ],
                    [15.12959925, 6.26045879 ],
                    [5.93041263 , 1.70841905 ],
                    [4.25054779 , 5.01371294 ],
                    [2.15139117 , 4.16668657 ],
                    [2.38283228 , 3.83347914 ]])

feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
print(feature[:4,:])

x = feature[1]
w = np.random.rand(feature.shape[1])



def perzeptron(w, x):
    return np.dot(w, x) > 0

y = 5
hund = y > 0 and y != 2


hund = perzeptron(w, x)
print(hund)

hund = True

if hund:
    print("Die Bedingung ist True")
else:
    print("Die Bedingung ist False")

y = 5
if y < 0:
  print("y ist negativ")
elif y % 2 == 1:
  print("y ist positiv und ungerade")
elif y > 9 and y % 3 != 0:
  print("y ist größer als 9 und nicht durch 3 teilbar")
else:
  print("Die Bedingungen sind alle False")

def perzeptron(w, x):
    if np.dot(w, x) > 0:
        return 1
    else:
        return 0

print(perzeptron(w, x))

hund = perzeptron(w, x)
if hund == 1:
    print("Das ist ein Hund!1")
elif hund == 0:
    print("Das ist kein Hund.1")


if perzeptron(w, x):
    print("Das ist ein Hund!2")
else:
    print("Das ist kein Hund.2")




