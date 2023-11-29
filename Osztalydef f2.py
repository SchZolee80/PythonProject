class Etel:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

    def __str__(self):
        return f"{self.nev}................{self.ar} Ft"

class Etterem:
    def __init__(self, nev):
        self.nev = nev
        self.menu = []

    def __str__(self):
        return self.nev

    def getmenuItems(self):
        if not self.menu:
            return "Az étteremnek nincs még menüje."
        else:
            return "\n".join([str(item) for item in self.menu])

    def hozzaad(self, etel):
        self.menu.append(etel)

    def __add__(self, other):
        if isinstance(other, Etel):
            self.hozzaad(other)
            return self
        else:
            raise TypeError("Az Étteremhez csak Étel objektumot lehet hozzáadni.")

# Példa használat:
etterem = Etterem("Példa Étterem")

while True:
    nev = input("Adja meg az étel nevét: ")
    ar = input("Adja meg az étel árát (Ft): ")

    try:
        ar = float(ar)
        if 0 < ar <= 100000:
            etel = Etel(nev, ar)
            etterem += etel
            print(f"{etel} hozzáadva a menühöz.\n")
        else:
            print("Hiba: Az étel árának 0 és 100 000 Ft között kell lennie.\n")
    except ValueError:
        print("Hiba: Az árnak egy érvényes számnak kell lennie.\n")

    folytatni = input("Szeretne még ételt hozzáadni? (igen/nem): ").lower()
    if folytatni != 'igen' :
        break

print(f"\n{etterem} Étterem menüje:")
print(etterem.getmenuItems())
