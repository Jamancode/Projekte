#https://www.youtube.com/watch?v=GFUz1bENOUM&list=PLIYzsTnFhywyjBon1_tE4ZGVzXAx5FpWr&index=5
# Visualisierungs-Funtion von Perzeptron Teil 2 (Original version von "Starup Teens" Grafik: "Original_plt_PT17")

import matplotlib.pyplot as plt
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

feature = np.concatenate((feature, np.ones(43).reshape(43,1)), axis=1)
print(feature[0:3,:])

labels = np.concatenate((np.ones(21), np.zeros(22)))
print(labels.shape)


def visualize(feature, labels, w, x=None, w_old=None):
    # Hier werden x und w_old als None definiert, sodass man sie beim Aufrufen nicht
    # unbedingt angeben muss. Sie könnten auch als [1,2,3,4] o.Ä. definiert werden,
    # aber None macht es einfacher für die if-Statements

    _, ax = plt.subplots()
    plt.title('Trainingsdaten')
    plt.xlabel('Grösse [cm]')
    plt.ylabel('Länge [cm]')
    plt.scatter(feature[:,0], feature[:, 1], c=labels)

    # Linie
    x0 = np.array([min(feature[:, 1]), max(feature[:, 0])])
    if w[1] != 0:
        x1 = -(w[0] * x0 + w[2]) / w[1]
        plt.plot(x0, x1, label='Gewichte')
        if w[1] > 0:
            ax.fill_between(x0, x1, x1 + 5, alpha=0.2, label='Hund')
        else:
            ax.fill_between(x0, x1, x1 - 5, alpha=0.2, label='Hund')

    if x is not None:
        plt.scatter(x[0], x[1], c='r', marker='x', label='Falsch klass.')

    if w_old is not None and w_old[1] != 0:
        x1_new = -(w_old[0] * x0 + w_old[2]) / w_old[1]
        plt.plot(x0, x1_new, 'r', label='Alten Gewichte')
        if w_old[1] > 0:
            ax.fill_between(x0, x1_new, x1_new + 5, alpha=0.2)
        else:
            ax.fill_between(x0, x1_new, x1_new - 5, alpha=0.2)

    plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
    plt.show()

np.random.seed(5) # damit die 'zufälligen' Zahlen immer gleich sind

# gewichte zufällig initialsieren
w = np.random.rand(feature.shape[1])
visualize(feature, labels, w)

