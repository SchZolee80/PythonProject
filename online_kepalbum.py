class Felhasznalo:
    def __init__(self, felhasznalonev, jelszo):
        self._felhasznalonev = felhasznalonev
        self._jelszo = jelszo
        self.albumok = []

    @property
    def felhasznalonev(self):
        return self._felhasznalonev

    @property
    def jelszo(self):
        return "Nincs hozzáférés"  # A jelszót nem közöljük nyilvánosan

    @jelszo.setter
    def jelszo(self, adott_jelszo):
        if self._jelszo_ellenorzes():
            self._jelszo = adott_jelszo
            print("Jelszó sikeresen megváltoztatva.")
        else:
            print("Hibás jelszó. A jelszó nem változott meg.")

    def _jelszo_ellenorzes(self):
        megadott_jelszo = input("Kérem a jelszót: ")
        return self._jelszo == megadott_jelszo


class Kep:
    def __init__(self, nev, meret, formatum, tulajdonos):
        self._nev = nev
        self._meret = meret
        self._formatum = formatum
        self._tulajdonos = tulajdonos

    @property
    def nev(self):
        return self._nev

    @property
    def meret(self):
        return self._meret

    @meret.setter
    def meret(self, uj_meret):
        # Itt lehetne tenni további ellenőrzéseket
        self._meret = uj_meret

    @property
    def formatum(self):
        return self._formatum

    @formatum.setter
    def formatum(self, uj_formatum):
        # Itt lehetne tenni további ellenőrzéseket
        self._formatum = uj_formatum

    @property
    def tulajdonos(self):
        return self._tulajdonos

    @tulajdonos.setter
    def tulajdonos(self, uj_tulajdonos):
        # Itt lehetne tenni további ellenőrzéseket
        self._tulajdonos = uj_tulajdonos


class Album:
    def __init__(self, nev, tulajdonos):
        self._nev = nev
        self._tulajdonos = tulajdonos
        self._kepek = []

    @property
    def nev(self):
        return self._nev

    @property
    def tulajdonos(self):
        return self._tulajdonos

    @tulajdonos.setter
    def tulajdonos(self, uj_tulajdonos):
        # Itt lehetne tenni további ellenőrzéseket
        self._tulajdonos = uj_tulajdonos

    @property
    def kepek(self):
        return self._kepek

    def kep_hozzaadasa(self, kep):
        # Itt lehetne tenni további ellenőrzéseket
        self._kepek.append(kep)
        print(f"Kép '{kep.nev}' hozzáadva az albumhoz.")


## Felhasználó létrehozása
user = Felhasznalo("user", "password")

# Kép létrehozása
kep = Kep("Tengerpart", "2 MB", "JPEG", user)

# Album létrehozása
album = Album("Nyaralas", user)

# Kép hozzáadása az albumhoz
album.kep_hozzaadasa(kep)

# Felhasználó jelszó módosítása
user.jelszo = "new_password"

# Kijelzés
print(f"Felhasználó neve: {user.felhasznalonev}")
print(f"Kép neve: {kep.nev}, Méret: {kep.meret}, Tulajdonos: {kep.tulajdonos.felhasznalonev}")
print(f"Album neve: {album.nev}, Tulajdonos: {album.tulajdonos.felhasznalonev}")
print(f"Képek az albumon belül: {[k.nev for k in album.kepek]}")
