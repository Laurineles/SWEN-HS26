import random
from rich import print

def zeichne_schicht(zeile, höhe_baum):
    leerzeichen = höhe_baum - zeile - 1
    sterne = 2 * zeile + 1
    reihe = ""
    for j in range(sterne):
        reihe = reihe + random.choice(["[bright_red]O[/bright_red]", "[green]*[/green]", "[green]*[/green]", "[green]*[/green]", "[green]*[/green]"])
    print(" " * leerzeichen + reihe)

def zeichne_stamm(höhe_baum):
    leerzeichen = höhe_baum - 1
    sterne = 1
    print(" " * leerzeichen + "[red]*[/red]" * sterne)

def zeichne_weihnachts_baum(höhe_baum, höhe_stamm=2):
    for i in range(höhe_baum):
        zeichne_schicht(i, höhe_baum)
    for i in range(höhe_stamm):
        zeichne_stamm(höhe_baum)

zeichne_weihnachts_baum(8, 3)