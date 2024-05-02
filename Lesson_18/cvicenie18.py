def funkcia(**kwargs):
    for kluc, hodnota in kwargs.items():
        print(f"{kluc} + {hodnota}")


funkcia(meno="alica", vek="15")


class Zviera:
    def __init__(self, druh):
        self.druh = druh

    def zvuk(self):
        print("Haf")

class Pes(Zviera):
    def __init__(self, druh, plemeno):
        super().__init__(druh)
        self.plemeno = plemeno

    def zvuk(self):
        print("Zvuk")


class Macka(Zviera):
    def __init__(self, druh, farba):
        super().__init__(druh)
        self.farba = farba

    def zvuk(self):
        print("Mňau")


zviera = Zviera("Nezname")
pes = Pes("psi", "labrador")
macka = Macka("macacia", "hnedá")


class Charakter:
    def __init__(self, meno, zdravie):
        self.meno = meno
        self.zdravie = zdravie

    def schopnost(self):
        print(f"{self.meno} útoči")

class Bojovnik(Charakter):
    def __init__(self, meno, zdravie, zbran, vydrz):
        super().__init__(meno, zdravie)
        self.zbran = zbran
        self.vydrz = vydrz

    def silny_utok(self):
        print(f" {self.meno} pouzil specialnu zbran")
        self.vydrz -=10
        print(f"Zostava {self.vydrz}")

    def shield_wall(self):
        print(f"{self.meno} požil štít proti útoku")
        self.vydrz +=50
        print(f"Doplnil si vydrzna {self.vydrz}")

class Carodejnik(Charakter):
    def __init__(self, meno, zdravie, mana):
        super().__init__(meno, zdravie)
        self.mana = mana
        self.fireball_cooldown = 0

    def fireball(self):
        if self.fireball_cooldown > 0:
            print(f"Kuzlo sa nabija. Zostáva {self.fireball_cooldown}")
        else:
            print(f"{self.meno} hodil supeball")
            self.mana -=10
            print(f"Zostáva {self.mana}")
            self.fireball_cooldown = 3

    def doplnenie_many(self):
        print(f"{self.meno} doplnil manu")
        self.mana +=50
        print(f"Zostáva {self.sipy}")
        self.fireball_cooldown = 0

class Lucistnik(Charakter):
    def __init__(self, meno, zdravie, agilita, sipy):
        super().__init__(meno, zdravie)
        self.aglita = agilita
        self.sipy = sipy

    def trojsip(self):
        print(f"{meno} vystrelil specialny sip")
        self.sipy -=3
        print(f"Zostava {self.sipy}")

    def doplnenie_sipov(self):
        print(f"{self.meno} vystrelil specialnym utokom")
        self.sipy += 10
        print(f"Dopnil si {self.sipy}")

Barbar = Bojovnik("Conan", 150, "Meč", 100)
Mag = Carodejnik("Mako", 70, 100, 100)
Lucistnik = Lucistnik ("Bobo", 100, 50, 100)

Barbar.silny_utok()
Barbar.schopnost()
Barbar.shield_wall()


Mag.fireball()
Mag.fireball()
Mag.fireball()
Mag.schopnost()


Carodejnik.schopnost()
Carodejnik.fireball()

Lucistnik.schopnost()
Lucistnik.trojsip()
Lucistnik.dopnenie_sipov()