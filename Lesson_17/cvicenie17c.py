class Auto:
    def __init__(self, znacka, model, rok_vyroby, spotreba, dostupnost, stav_tachometra, realna_spotreba):
        self.znacka = znacka
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.spotreba = spotreba
        self.dostupnost = dostupnost
        self.stav_tachometra = stav_tachometra
        self.realna_spotreba = realna_spotreba

    def popis_auta(self):
        return self.znacka, self.model, self.rok_vyroby, self.spotreba, self.dostupnost, self.stav_tachometra, self.realna_spotreba

    def spotreba_na_vzdialenost(self, trasa):
        return (trasa / 100) * float(self.spotreba)

    def vypocitana_spotreba(self, trasa, objem_phm):
        return objem_phm / (trasa/100)

auto1 = Auto("BMV", "X3", "2015", "6.3", "6/2024", "165000", "7.5")
auto2 = Auto("Škoda", "Rapid", "2010", "5.9", "ihneď", "110000", "6.1")
print(f"Auto1, spotreba na vzdialenosť 50 km: {auto1.spotreba_na_vzdialenost(50)}")
print(f"Auto2, spotreba na vzdialenosť 50 km: {auto2.spotreba_na_vzdialenost(50)}")
print("\n")
popis = auto1.popis_auta()
print("Popis auto1 pred úpravou reálnej spotreby:")
print(popis)
print("\n")
pom = auto1.vypocitana_spotreba(250, 17.5)
print("Vypocitana reálna spotreba auta1  je: ", pom, " l/100 km")
auto1.realna_spotreba = pom
# vytvorit metodu, ktora aktualizuje spotrebu na zaklade realnych udajov (trasa, spotrebovany objem phm)
print("\n")
print("Popis auto1 po uprave reálnej spotreby:")
print(auto1.popis_auta())
print("\n")
print(f"Značka auta : {auto1.znacka}")
print(f"Model  auta : {auto1.model}")
print(f"Spotreba podľa TP : {auto1.spotreba}")
print(f"Reálna spotreba auta : {auto1.realna_spotreba}")
print(f"Auto spotrebuje podľa dokumentácie na 1000 km : {auto1.spotreba_na_vzdialenost(1000)}")