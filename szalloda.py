class Szoba:
    """A szálloda szobáját reprezentáló osztály"""

    def __init__(self, szobaszam, foglalt=False):
        """Inicializálja a szoba attribútumait"""
        self.szobaszam = szobaszam
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
