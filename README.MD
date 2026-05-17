# Zero-Player Football

Dieses Projekt ist aus meinem Interesse an klassischen [Fußball-Manager](https://de.wikipedia.org/wiki/Fu%C3%9Fball-Manager)-Spielen entstanden. Es ist der erste Schritt des Versuchs, die Grundzüge einer solchen Fußballsimulation selbst zu programmieren. Weil das Projekt noch ganz am Anfang des Entwicklungsprozesses steht, erlaubt die derzeitige Version zunächst ausschließlich das Erzeugen, Speichern und Laden einer Vereins- und Spielerdatenbank. Weitere Features werden folgen.

![Screenshot des Database Viewers](./doc/screenshots/screenshot_database_viewer.png)


## Hintergrund

Fußball-Manager-Spiele wie die der [Anstoß](https://de.wikipedia.org/wiki/Anstoss)-Reihe waren in den 90er und frühen 00er Jahren auf dem Zenit ihrer Popularität. Die Stärke dieses Genres liegt darin, durch eine detailverliebte Simulation sportlicher und wirtschaftlicher Aspekte die Atmosphäre, Spannung und Dramatik einer gesamten Bundesligasaison auf nur wenigen Stunden Spielzeit zu verdichten.

Frustrierend können Spiele dieser Art jedoch werden, sobald man beginnt, das Spielgeschehen und dessen Zustandekommen zu hinterfragen: Welchen  genauen Effekt hat es auf die Spielberechnung, wenn ich die Mannschaftsaufstellung verändere? Warum treffen meine Spieler nie das Tor, obwohl ich ständig Torschüsse trainieren lasse? Und hat die Auswahl einer mysteriösen „Spezialtaktik“ wirklich eine Auswirkung, oder ist die dafür zuständige Checkbox vielleicht nur ein Bedienelement ohne hinterlegte Funktion?

Aus ebenjener Blackbox-Erfahrung heraus ist dieses Projekt entstanden. Sein Ziel ist die Entwicklung eines einfachen und nachvollziehbaren Fußball-Managers, der neben einer sportlichen und einer wirtschaftlichen Komponente auch Bezüge zu historischen Entwicklungen und Ereignissen aus der Bundesliga und dem internationalen Fußball enthalten soll.

## Umsetzung

Um den Enwicklungsprozess zu Beginn überschaubarer zu halten, wird die Simulation nicht von Anfang an als *interaktives* Spiel umgesetzt, sondern im ersten Schritt als ein [Zero-Player Game](https://en.wikipedia.org/wiki/Zero-player_game): Ereignisse können lediglich *betrachtet* werden, ein Eingriff in das Geschehen ist dagegen nicht möglich. Der Gedanke dahinter: Solange kein Modell existiert, das selbstständig über mehrere Spielzeiten hinweg ein stabiles System aus Vereinen, Spielern und Trainern aufrecht halten kann, ist jede spielerische Interaktion widersinnig. Erst im zweiten Schritt wird die Möglichkeit hinzukommen, aktiv die Geschicke eines Vereins beeinflussen zu können.

Die Kernbestandteile des Modells werden sich an Spielmechaniken von [Anstoß 3](https://de.wikipedia.org/wiki/Anstoss_3) orientieren, darunter beispielsweise:

- ein Spielstärkensystem mit Werten von 1 bis 12
- Spieler-Attribute, die von Talent, Kondition, Frische und Motivation geprägt sind
- die Darstellung der Partien in Textform
- eine satirische Komponente, die vor allem durch einflussreiche Zufallsereignisse zum Ausdruck kommt.

Die technische Umsetzung von *Zero-Player Football* ist als reine Desktop-Anwendung mit einer simplen, zweckmäßigen Benutzerschnittstelle geplant, um den Schwerpunkt auf die Entwicklung eines stabilen Modells zu legen. Erst im zweiten Projektabschnitt, wenn das Modell zu einem interaktiven Spiel erweitert wird, kann die Gestaltung einer grafischen Oberfläche in den Fokus rücken.
