# Vytvoř třídu Auto (Parent class) a další pod-třídy (Child class) pro osobní auto a nákladní auto,
# které budou obsahovat specifické atributy/metody.

class Auto:
    def __init__(self, urcenie, druh, znacka, model, rok_vyroby, nosnost, spz, spotreba, realna_spotreba, stav_tachometra, cena):
        self.urcenie = urcenie
        self.druh = druh
        self.znacka = znacka
        self.model = model,
        self.rok_vyroby = rok_vyroby
        self.nosnost = nosnost
        self.spz = spz
        self.spotreba = spotreba
        self.realna_spotreba = realna_spotreba
        self.stav_tachometra = stav_tachometra
        self.cena = cena

        def popis_auta(self):
            if self.urcenie == "AUO":
                print(self.druh, self.znacka, self.rok_vyroby, self.nosnost, self.spz, self.spotreba, self.realna_spotreba, self. stav_tachometra, self.cena)
            elif self.urcenie == "AUN":
                print(self.druh, self.znacka, self.rok_vyroby, self.spz, self.spotreba, self.realna_spotreba, self.stav_tachometra, self.cena)




auto1 = Auto("AUO", "BMV", "X3", "2015", 2018, 890, "BA 1234XY", 6.3,  7.1, 121000, 32000)
auto2 = Auto("Škoda", "Rapid", "2010", "5.9", 2018, 890, "BA 1234XY", 6.3,  7.1, 121000, 32000)
