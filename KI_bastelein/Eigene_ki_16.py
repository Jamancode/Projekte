
#https://www.youtube.com/watch?v=5xSbiRHUnZc&list=PLIYzsTnFhywyjBon1_tE4ZGVzXAx5FpWr&index=4
#For-Schleife-Teil 1 (Range, Enumerate, Zip)

#for x in feature:       würde einmal die ganze liste durch itrerieren.
  #  print(x)

import numpy as np
import matplotlib.pyplot as plt

feature = np.array([[37.92655435, 23.90101111],
                    [35.88942857, 22.73639281],
                    [29.49674574, 21.42168559],
                    [32.48016326, 21.7340484],
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
                    [4.44136559, 3.52432493],
                    [10.26395607, 1.07729281],
                    [7.39058439, 3.44234423],
                    [4.23565118, 4.28840232],
                    [3.87875761, 5.12407692],
                    [15.12959925, 6.26045879],
                    [5.93041263, 1.70841905],
                    [4.25054779, 5.01371294],
                    [2.15139117, 4.16668657],
                    [2.38283228, 3.83347914]])

feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
print(feature[0:3,:])


labels = np.concatenate((np.ones(21), np.zeros(22)))
print(labels.shape)


def visualize(feature, labels, w, x=None, w_old=None):
    # Hier werden x und w_old als None definiert, sodass man sie beim Aufrufen nicht
    # unbedingt angeben muss. Sie könnten auch als [1,2,3,4] o.Ä. definiert werden,
    # aber None macht es einfacher für die if-Statements

    fig, ax = plt.subplots()
    plt.title('Trainingsdaten')
    plt.xlabel('Grösse [cm]')
    plt.ylabel('Länge [cm]')
    plt.scatter(feature[:, 0], feature[:, 1], c=labels)

    # Linie
    x0 = np.array([min(feature[:, 1]), max(feature[:, 0])])
    if w[1] != 0:
        x1 = -(w[0] * x0 + w[2]) / w[1]
        plt.plot(x0, x1, label='Gewichte')
        if w[1] > 0:
            ax.fill_between(x0, x1, x1 + 5, alpha=0.2, label='Hund', facecolors='tab:green')
        else:
            ax.fill_between(x0, x1, x1 - 5, alpha=0.2, label='Hund', facecolors='tab:green')

    if x is not None:
        plt.scatter(x[0], x[1], c='r', marker='x', label='Falsch klass.')

    if w_old is not None and w_old[1] != 0:
        x1_new = -(w_old[0] * x0 + w_old[2]) / w_old[1]
        plt.plot(x0, x1_new, 'r', label='Alten Gewichte')
        if w_old[1] > 0:
            ax.fill_between(x0, x1_new, x1_new + 5, alpha=0.2, facecolors='#50bf87')
        else:
            ax.fill_between(x0, x1_new, x1_new - 5, alpha=0.2, facecolors='#50bf87')

    ax.set_facecolor('#fed0d0')
    fig.patch.set_facecolor('#F6F6F6')

    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.show()


def perzeptron(w, x):
    if np.dot(w, x) > 0:
        return 1.0
    else:
        return 0.0



zaehler = 0
for x in feature:
    if x[1] > x[0]:
        zaehler += 1

print("Es gibt " + str(zaehler) + " Tiere die breiter sind als ihre Größe.")

np.random.seed(5)

w = np.random.rand(feature.shape[1])



x = feature[0]
label = labels[0]

ausgabe = perzeptron(w, x)
if ausgabe == label:
    pass
elif ausgabe == 1 and label == 0:
    w += x
elif ausgabe == 0 and label == 1:
    w -= x

delta = label - perzeptron(w, x)
w += delta * x


# In einer Zeile:
w += (label - perzeptron(w, x)) * x


#for index in range(len(feature)):
    #x = feature[index]
    #label = labels[index]
    #delta = label - perzeptron(w,x)
    #w += delta * x

#for index, x in enumerate(feature):
    #label = labels[index]
    #delta = label - perzeptron(w,x)
    #w += delta * x

fehler = 0
for x, label in zip(feature, labels):
    delta = label - perzeptron(w,x)
    w += delta * x
    if delta != 0:
        fehler += 1
print('Es wurden ' + str(fehler) + ' datenpunkte falsch ausgegeben.')

visualize(feature, labels, w)