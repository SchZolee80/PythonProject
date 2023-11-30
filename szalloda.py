class Szoba:
    """A szálloda szobáját reprezentáló osztály"""

    def __init__(self, szobaszam: int, foglalt=False):
        """Inicializálja a szoba attribútumait"""
        self.szobaszam = int(szobaszam)
        self.foglalt = foglalt
        self.ar = 0  # Az árat inicializáljuk 0-val, majd a különböző típusokban felülírjuk
        self.extrak = []  # Az extrák listáját inicializáljuk üres listával

    def foglal(self):
        """Foglalási folyamatot végrehajtó metódus"""
        if not self.foglalt:
            self.foglalt = True
            print(f"Szoba {self.szobaszam} sikeresen foglalva.")
        else:
            print(f"A szoba {self.szobaszam} már foglalt.")

    def szabad(self):
        """Ellenőrzi, hogy a szoba szabad-e"""
        return not self.foglalt

    def ar_megjelenites(self):
        """Megjeleníti a szoba árát"""
        print(f"A szoba {self.szobaszam} ára: {self.ar} Ft")

    def extras_megjelenites(self):
        """Megjeleníti a szoba extráit"""
        print(f"A szoba {self.szobaszam} extrái: {', '.join(self.extrak)}")


class KetagyasSzoba(Szoba):
    """Kétágyas szobát reprezentáló osztály"""

    def __init__(self, szobaszam, foglalt=False):
        super().__init__(szobaszam, foglalt)
        self.ar = 20000  # Ár inicializálása
        self.extrak = ["TV", "WIFI"]  # Extra tulajdonságok inicializálása


class EgyagyasSzoba(Szoba):
    """Egyágyas szobát reprezentáló osztály"""

    def __init__(self, szobaszam, foglalt=False):
        super().__init__(szobaszam, foglalt)
        self.ar = 15000  # Ár inicializálása
        self.extrak = ["WIFI"]  # Extra tulajdonságok inicializálása


class Lakosztaly(Szoba):
    """Lakosztályt reprezentáló osztály"""

    def __init__(self, szobaszam, foglalt=False):
        super().__init__(szobaszam, foglalt)
        self.ar = 30000  # Ár inicializálása
        self.extrak = ["TV", "WIFI", "Minibár"]  # Extra tulajdonságok inicializálása

class SzallodaRendszer:
    """A szálloda rendszerét kezelő osztály"""

    def __init__(self):
        """Inicializálja a szálloda rendszerét"""
        self.szobak = []  # Szobák listája

    def adatfeltolto(self):
        """Feltölti az adatokat néhány alapértelmezett szobával"""
        self.szobak.append(KetagyasSzoba(szobaszam=101))
        self.szobak.append(EgyagyasSzoba(szobaszam=102))
        self.szobak.append(Lakosztaly(szobaszam=201))

    def foglalas_lekerdez(self):
        """Lekérdezi a foglalásokat"""
        for szoba in self.szobak:
            if szoba.foglalt:
                print(f"Szoba {szoba.szobaszam} foglalt.")
            else:
                print(f"Szoba {szoba.szobaszam} szabad.")

    def arak_lekerdez(self):
        """Lekérdezi a szobák árait"""
        for szoba in self.szobak:
            szoba.ar_megjelenites()

    def foglalas_lead(self, szobaszam: int):
        """Foglalást hajt végre a megadott szobaszámon"""
        szobaszam = int(szobaszam)
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                szoba.foglal()
                return True
        print(f"Az adott szobaszám ({szobaszam}) nem található.")
        return False

# Tesztelés
rendsz = SzallodaRendszer()
rendsz.adatfeltolto()

while True:
    print("\nVálasszon egy opciót:")
    print("1. Foglalások lekérdezése")
    print("2. Árak lekérdezése")
    print("3. Új foglalás leadása")
    print("4. Kilépés")

    valasztas = input("Adja meg a választott opció számát: ")

    if valasztas == "1":
        rendsz.foglalas_lekerdez()
    elif valasztas == "2":
        rendsz.arak_lekerdez()
    elif valasztas == "3":
        szobaszam = input("Adja meg a foglalni kívánt szobaszámot: ")
        if rendsz.foglalas_lead(szobaszam):
            print(f"A szoba {szobaszam} sikeresen foglalva.")
        else:
            print("A foglalás sikertelen.")
    elif valasztas == "4":
        print("Viszontlát!")
        break
    else:
        print("Érvénytelen választás. Kérem, válasszon újra.")
