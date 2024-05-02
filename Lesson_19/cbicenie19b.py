
class NakupnyZoznam:
    def __init__(self):
        self.zoznam_poloziek = []

    def pridanie_polozky(self, polozka):
        self.zoznam_poloziek.append(polozka)

    def odobranie_polozky(self, polozka):
        if polozka in self.zoznam.poloziek:
            self.zoznam_poloziek.remove(self.polozka)
        else:
            print("Polozka sa v zozname nenachádza.")

    def zobrazit_polozky(self):
        for polozka in self.zoznam_poloziek:
            print(f" cena {polozka.cena}, mnozsrvo {polozka.mnozstvo}, {polozka.cena}")

class Polozka:
    def __init__(self, nazov, mnozstvo, cena):
        self.nazov = nazov
        self.mnozstvo = mnozstvo
        self.cena = cena

polozka = Polozka("banán",  1000, 2.50)

zoznam = NakupnyZoznam()
zoznam.pridanie_polozky(polozka)
zoznam.zobrazit_polozky()

