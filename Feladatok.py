import korszamitas
# Hozz létre egy listát, amelyben 5 különböző gyümölcs neve található.
gyumolcsok = ["alma", "körte", "szilva", "banán", "ananász"]

# Írj egy for ciklust, ami kiírja a gyümölcsök neveit betűrendben.
print("Gyümölcsök betűrendben:")
for gyumolcs in sorted(gyumolcsok):
    print(gyumolcs)

# Adj hozzá egy feltételvizsgálatot, ami csak az "a" betűvel kezdődő gyümölcsöket írja ki.
print("\n'A' betűvel kezdődő gyümölcsök:")
for gyumolcs in (gyumolcsok):
    if gyumolcs.startswith('a'):
        print(gyumolcs)

# korszamitas
sugar = float(input("Kérem, adja meg a kör sugarát: "))
terulet, kerulet = korszamitas.kor_terulet_es_kerulet(sugar)

print(f"A kör területe: {terulet:.2f}")
print(f"A kör kerülete: {kerulet:.2f}")
