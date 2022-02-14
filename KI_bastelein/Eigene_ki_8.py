# https://www.youtube.com/watch?v=DXpk5hniOK4

#grunde gerüst
def meine_funktion():
    print('Die Funktion wurde aufgerufen')

meine_funktion()

txt = ' mit neuem Inhalt.'
def meine_neue_funktion(input_text):
    print('Die Funktion wurde aufgerufen' + input_text)

meine_neue_funktion(txt)


def neue_funktion(input_text):
    text = 'Tolle eine ausgeführte funktion.' + input_text
    return text

txt2 = 'mit Text als Argument.'
voller_text = neue_funktion(txt2)
print(voller_text)

#<-------

def kugel_volumen(radius, kommastellen):
    pi = 3.14159
    volumen = (4 / 3) * pi * radius ** 3
    volumen = round(volumen, kommastellen)

    return pi, radius, volumen

pi, r, vol = kugel_volumen(5, 3)
print('Eine Kugel mit dem Radius ' + str(r) + ' hat das Volumen ' + str(vol) + '.' + '\nIn der Formel benutzt man pi =' + str(pi))