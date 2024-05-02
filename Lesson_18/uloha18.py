# Vytvoř třídu Auto (Parent class) a další pod-třídy (Child class) pro osobní auto a nákladní auto,
# které budou obsahovat specifické atributy/metody.

# POZNÁMKA - omylom som úlohu povodne umiestnil, ako úlohu č.17b, teraz som ju trochu rozsiril

class Auto:
    def __init__(self, urcenie, druh, znacka, model, rok_vyroby, nosnost, spz, spotreba, realna_spotreba,
                 stav_tachometra, cena):
        self.urcenie = urcenie
        self.druh = druh
        self.znacka = znacka
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.nosnost = nosnost
        self.spz = spz
        self.spotreba = spotreba
        self.realna_spotreba = realna_spotreba
        self.stav_tachometra = stav_tachometra
        self.cena = cena

    def popis_auta(self):
        if self.urcenie == "AUO":
            print(f"Popis osobného auta: \ndruh: {self.druh} model: {self.znacka}, rok výroby: {self.rok_vyroby}, nosnosť: {self.nosnost}, ŠPZ: {self.spz}, \n spotreba podľa TP: {self.spotreba}, skutočná spotreba: {self.realna_spotreba:.2f}, \nstav tachometra: {self.stav_tachometra}, cena: {self.cena} EUR")
        elif self.urcenie == "AUN":
            print(f"Popis nákladného auta: \ndruh: {self.druh} model: {self.znacka}, rok výroby: {self.rok_vyroby}, nosnosť: {self.nosnost}, ŠPZ: {self.spz}, \nspotreba podľa TP: {self.spotreba}, skutočná spotreba: {self.realna_spotreba:.2f}, \nstav tachometra: {self.stav_tachometra}, cena: {self.cena} EUR")

    def aktualizuj_spotrebu(self):
        print("Reálna spotreba automobilu ", self.druh, self.znacka, " pred aktualizáciou je: ", self.realna_spotreba)
        a = float(input("prejdená vzdialenosť: "))
        b = float(input("Spotrebované phm: "))
        # aritmetický priemer medzi akamžite vypočítanou spotrebou a predchádzajúcou hodnotou reálnej spotreby
        self.realna_spotreba =( b / (a / 100) + self.realna_spotreba ) / 2
        print(f"Aktualizovaná reálna spotreba automobilu je teraz: {self.realna_spotreba:.2f}")
        print("\n")


auto1 = Auto("AUO", "BMV", "X3", "2015", 2018, 890, "BA 1234XY", 7.3, 8.5, 121000, 32000)
auto2 = Auto("AUO", "Škoda", "Rapid", "Sport", 2015, 620, "BA 999AA", 6.3, 7.1, 121000, 16000)
auto3 = Auto("AUN", "V3S", "Special", "1965", 2018, 890, "BA 1234XY", 32.2, 41.1, 350000, 16000)

print("Aktualizácia spotreby. ", auto1.druh, auto1.znacka, "Reálna spotreba pred aktualizáciou je: ", auto1.realna_spotreba)
auto1.aktualizuj_spotrebu()
print("Aktualizácia spotreby. ", auto2.druh, auto2.znacka, "Reálna spotreba pred aktualizáciou je: ", auto2.realna_spotreba)
auto2.aktualizuj_spotrebu()
print("Aktualizácia spotreby. ", auto3.druh, auto3.znacka, "Reálna spotreba pred aktualizáciou je: ", auto3.realna_spotreba)
auto3.aktualizuj_spotrebu()




print(f"Rozdiel v spotrebe od údajov v technickom preukaze je: {auto1.realna_spotreba - auto1.spotreba:.2f} l/100 km")
auto1.popis_auta()
print("\n")
spotreba = auto2.realna_spotreba
print(f"Rozdiel v spotrebe od údajov v technickom preukaze je: {auto2.realna_spotreba - auto2.spotreba:.2f} l/100 km")
auto2.popis_auta()
print("\n")
spotreba = auto3.realna_spotreba
print(f"Rozdiel v spotrebe od údajov v technickom preukaze je: {auto3.realna_spotreba - auto3.spotreba:.2f} l/100 km")
auto3.popis_auta()
