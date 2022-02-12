 # Arten von Machinelen lernen

# 1 supervised lerning:
# Ziel: Stellschrauben einer Funktion so zu einzustellen, dass die richtige Ausgabe generiert werden.
# Stellschrauben hier: lernphase --- Wenn stellschrauben optimale (prarmeter) enthalten bzw optimal eingestellt werden ---> verwendung
# * Einstellung der Stellschrauen
# * Ausgaben der Funktion werden mit Zielaufgaben verglichen.


 # 2 unsupervised lerning:
 # Ziel: Etwas über die Daten zu lernen, welche man durch Erzeugung von Gruppen (cluster) ähnlicher Daten bildetet.
 # Typischerweise mit der hilfe von Clustering: = Erzeugen von Gruppen ähnlicher Daten, ohne dass die Gruppen vorher definiert wurden.
 # * wird eingesetzt bei sehr großen Datenmengen, die Menschen überfordern würden.


#1+2 semi- supervised lerning
# zwischenform aus supervised lerning und unsupervised lerning


# 3 reinfocement lerning:
# kommt meinst bei Trainieren von Robotern oder eigenständigen prozessbedingten Maschienen zu Einsatz
# * KI lernt durch Versuch & Irrtum
# * KI mann frei habdeln
# * KI erhält Blohnung oder Bestrafungen


#Beispiele für Anwendungen: Klassifikation, Regession, Clustering

# für 1 supervised lerning:
# Kassifikation über einen Klassifokator : Kassifikation ist nicht Clustering!
# Ziel = Daten in Klassen einordnen: " Klassifokator " soll nach dem Lernen neue Daten in die Klassen einordnen können.
# Beispliele hier ist die unterscheidung von Hunden und Katzen. #Klassifokator bauen: Eingabe -> Funktion -> Ausgabe
# merkmale finden mit hilfe einer Funktion, hier zu benötigt sie viele beispieldaten. zb: viele bilder von den zu kassifizierenden daten haben zum beispiel Tiere.
# Klassen werden für die Zieldaten am anfang genau definiert ( Beispieldaten (Klassen werden am anfang definiert) Zieldaten)
# weiterer einsatz zb, bei selbstfahrenden autos die Fußgänger erkennen sollen.


# für 1 supervised lerning:
# Regression
# Ziel hängt von der anwendung ab.
# Gemeinsamkeit mit Klassifikation: Funktion, die aus Eingangedaten eine Ausgage generiert.
# Unterschied zur Klassifikation: Ausgabe sind keine Klassen oder Cluster, sondern Zahlen.
# Eingabe -> Funktion -> Ausgabe : Hier muss die funktion lernen welche zieldaten wir wollen.
# Beispiel: Alter von Mneschen schätzen: Bilder von menschen mit echtem alter zugeordnet.
# Weiteres Beispiel / Anwendung für vorhersagen zb, Vorhersage von Aktienkursen.


# für 2 unsupervised lerning:
# Clustering
# ein Ziel beispiel: Twitter- Nutzer in Gruppen einordnen. Clustering kritteriern (Merkmale = Statistiken = Features)
# ZB: Fußball-Twitterer oder Bots
# : mit hilfe von Metadaten zb, anzahl der Tweets pro woche, aktivität der Nutzer, Anzahl von Adjektiven pro Tweet.
# Clutering umsetzung: für 15 Nutzer und 2 Merkmale pro Nutzer auf x achse anzahl der Tweets pro Woche auf der y achse Aktivität. Die methode hier würde grppen von Nutzern finden und zusammen kassifizieren.
# Gruppen werden vorher NICHT definiert!

#_____

# Schwache und Starke KI:
# Schwache KI: Können nur für die spezifischen Anwendungen genutzt werden, für die sie entwikelt wurden. ( Greifen auf Methoden der Informatik und Mathematik zurück --> Eingeschränkt)
# Starke KI: Eine Starke KI kann ihr Wissen auf andere Kontexte übettragen und eigene Handlungen reflektieren. (* menschenähnliche Fähigkeiten, * kann selbstäandig denken, * handelt aus eigenem Antrieb) [noch nicht existent!]

# Gefahren von Schwacher KI: Missbrach wie Deep fakes oder Autonome drohen
# Deep Fakes: sind gefälschte Bilder oder Videos, die mithilfe Künstlicher Intelligenz erstellt wurden.

#_____________________

# Ethische KI! (Sehr WICHTIG! ASIMOVSCHE GESETZE)
# 1942 habt Biochemiker und Schriftsteller "Isaac Asimov" die "Asimov die 3 Gesetze der Robotik" (Asimovsche Gesetze) geschrieben.
# Zitate:
# 1. Ein Roboter darf kein menschenliches Wesen wissendlich verletzen oder druch Untätigkeit wissentlich zulassen, dass einem menschlichen Wesen Schaden zugefügt wird!
# 2. Ein Roboter muss den ihm von einem Menschen gegenenen Befehlen gehorchen - es sei denn, ein solcher Befehl würde mit Regel eins Kollidieren.
# 3. Ein Roboter muss seine Existenz beschützen, solange dieser Schutz nicht mit Regel eins oder zwei kollidiert.

# 1983 hat Asimov die 0. Regel hinzugefügt.
# 0. Ein Roboter darf die Menschheit nicht verletzen oder druch Passivität zulassen, dass die Menscheit zu schaden kommt.

# Leitlinie der EU "ETHIK-LEITLINIEN FÜR EINE VERTRAUENSWÜRDIGE KI" link zum dokument =(' https://ec.europa.eu/newsroom/dae/document.cfm?doc_id=60425 ')

#___________________
