while True:
    try:
        # Felhasználótól bekérjük a számot
        szam = input("Kérem, adjon meg egy egész számot (legalább 10): ")

        # Ellenőrizzük, hogy a bevitel egy érvényes egész szám-e
        if not szam.isdigit():
            raise ValueError("A megadott érték nem egy érvényes egész szám.")

        # Konvertáljuk a számot int típusúvá
        szam = int(szam)

        # Ellenőrizzük, hogy a szám nagyobb-e 10-nél
        if szam <= 10:
            # Ha a feltétel nem teljesül, kivételt dobunk
            raise ValueError("A megadott szám nem nagyobb 10-nél.")

        # Ha minden rendben van, kiírjuk az üzenetet és kilépünk a ciklusból
        print(f"A megadott szám ({szam}) megfelelő.")
        break

    except ValueError as e:
        # Hibaüzenet, ha a bevitel nem érvényes vagy a szám kisebb vagy egyenlő 10-nél
        print(f"Hiba: {e} Kérem, próbálja újra.")
    except TypeError as e:
        # Hibaüzenet, ha a bevitel nem érvényes típusú
        print(f"Hiba: {e} A megadott érték nem egy érvényes egész szám.")
