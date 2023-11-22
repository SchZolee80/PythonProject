import math
def kor_terulet_es_kerulet(sugar):
# Terület kiszámítása: A = π * r^2

    terulet = math.pi * sugar ** 2

# Kerület kiszámítása: K = 2 * π * r

    kerulet = 2 * math.pi * sugar

    return terulet, kerulet
