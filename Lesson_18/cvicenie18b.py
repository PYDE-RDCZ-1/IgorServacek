class Character:
    def __init__(self,jmeno,zdravi):
        self.jmeno = jmeno
        self.zdravi = zdravi

    def schopnost(self):
        print(f"{self.jmeno} útočí!!!")

    def regenerace(self):
        print(f"{self.jmeno} regeneruješ.")

class Bojovník(Character):
    def __init__(self,jmeno,zdravi,zbraň,výdrž):
        super().__init__(jmeno,zdravi)
        self.zbraň = zbraň
        self.výdrž = výdrž

    def silný_útok(self):
        print(f"{self.jmeno} použil speciální silný útok")
        self.výdrž -=10
        print(f"Zbývá {self.výdrž}")

    def shield_wall(self):
        print(f"{self.jmeno} použil štít proti útoku.")
        self.výdrž +=30
        print(f"Doplnil jsi výdrž na {self.výdrž}")

class Čaroděj(Character):
    def __init__(self,jmeno,zdravi,mana):
        super().__init__(jmeno,zdravi)
        self.mana = mana
        self.FC = 0

    def Fireball(self):
        if self.FC > 0:
            print(f"Kouzlo se nabíjí. Zbývá {self.FC} kol.")
        else:
            print(f"{self.jmeno} hodil ohnivý fireball")
            self.mana -=10
            print(f"Zbývá {self.mana}")
            self.FC = 3

    def Doplněnímany(self):
        print(f"{self.jmeno} vypil lektvar many")
        self.mana +=50
        print(f"Doplnil jsi manu na {self.mana}")
        self.FC = 0
        print(f"Tvoje speciální abilita je připravená k použití")
class Lučištník(Character):
    def __init__(self,jmeno,zdravi,agilita,šípy):
        super().__init__(jmeno,zdravi)
        self.agilita = agilita
        self.šípy = šípy

    def Trojšíp(self):
        print(f"{self.jmeno} vystřelil speciálním útokem!")
        self.šípy -=3
        print(f"Zbývá {self.šípy}")


    def Doplněníšípů(self):
        print(f"Posbíral jsi šípy z mrtvol")
        self.šípy += 10
        print(f"Doplnil jsi počet šípů na {self.šípy}")
Barbar = Bojovník("Conan",150,"Meč",100)
Mág = Čaroděj("Mrakoplaš",70,100)
Lučištník = Lučištník("Legolas",100,60,20)

Barbar.silný_útok()
Barbar.schopnost()
Barbar.shield_wall()

Mág.Fireball()
Mág.schopnost()
Mág.Doplněnímany()

Lučištník.Trojšíp()
Lučištník.schopnost()
Lučištník.Doplněníšípů()