class Citizen:
    def __init__(self, meno, priezvisko, rok_nar, miesto):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok_nar = rok_nar
        self.miesto = miesto

    def vypis(self):
        return self.meno, self.priezvisko, self.rok_nar, self.miesto

osoba1 = Citizen("Peter", "Kováč", "1955", "Nitra" )
osoba2 = Citizen("Ján", "Bobok", "1977", "Zvolen")

udaje = osoba1.vypis()
print(osoba1.priezvisko)
