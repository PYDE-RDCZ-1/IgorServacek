# POZNÁMKA K TESTOM
# vzhľadom k chybovým oznamom pri vykonávaní testov, musel som v kóde odstrániť vśetky vstupy cez klávesnicu (interakcie).
# aktuálne je zabezpePcený 1 priechod cez loop
# Test je zameraný na overenie funkcie overujúcej voľnú bunku


# Hra PIŠKVORKY

import sys
import time
import unittest
from datetime import timedelta
from datetime import datetime


class Matica:
    def __init__(self, stlpec, riadok):
        self.stlpec = stlpec
        self.riadok = riadok
        self.data = [["_" for _ in range(stlpec)] for _ in range(riadok)]

    def __str__(self):
        matica_str = ""
        for stlpec in self.data:
            matica_str += " ".join(map(str, stlpec)) + "\n"
        return matica_str

#    def over_zasah(self):

    def check_free_item(self, stlpec, riadok):
        if self.data[stlpec - 1][riadok - 1] == "_":
            answer = True
        else:
            answer = False
        return answer

    def hracia_pocha(self):
        print("Aktuálny stav na hracej ploche:")
        for i in range(self.stlpec):
            if i < 9:
                print(f" {i + 1}", end=" ")
            else:
                print(i + 1, end=" ")
            for j in range(self.riadok):
                print(self.data[i][j], end=" ")
            print()
        return

    def nastav_hodnotu_bunky(self, stlpec, riadok, znak):
        self.data[stlpec-1][riadok-1] = znak
        return

    def over_volnu_bunku(self, stlpec, riadok):
        if self.data[stlpec-1][riadok-1] == "_":
            priznak = True
        else:
            priznak = False
        return priznak

    def zadaj_suradnice_tahu(self, player_nr):
        a = 0
        b = 0
        prebieha = True
        while prebieha:
            korektne_zadanie = True
            while korektne_zadanie:
                print("Na ťahu je hráč ", player_nr, ". Zadaj súradnicu x : ", end="")
                a = 10
                if a < 1 or a > self.riadok:
                    print("hodnoty môžu byť z intervalu <1,", self.riadok, ">. Zadajte znovu")
                else:
                    korektne_zadanie = False
            #    korektne_zadanie = True
            # start
            # while korektne_zadanie:
            print("Zadajte súradnicu y : ", end="")
            b = 10
            if b < 1 or b > self.stlpec:
                print("hodnoty môžu byť z intervalu <1,", self.stlpec, ">. Zadajte znovu")
            elif not self.over_volnu_bunku(a, b):
                print("zadali ste súradnice poľa, ktoré už obsahuje hrací kameň. Prosím, opakujte znova!")
                prebieha = True
            else:
                # self.over_volnu_bunku(a, b)
                korektne_zadanie = False
                prebieha = False
        if players.meno1 == player_nr:
            self.data[a - 1][b - 1] = "o"
        elif players.meno2 == player_nr:
            self.data[a - 1][b - 1] = "x"
        return

    def over_susedov(self, row, col, znak):
        # row = row
        # col = col
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, 5):
                r = row + dr * i
                c = col + dc * i
                if 0 <= r < self.riadok and 0 <= c < self.stlpec and self.data[r][c] == znak:
                    count += 1
                else:
                    break
            if count == 5:
                print("Víťaz")
                return True
#        print("nema vitaza")
        return False

    def over_vitaza(self, znak):
        for row in range(self.riadok):
            for col in range(self.stlpec):
                if self.data[row][col] == znak and matica.over_susedov(row, col, znak):
                    return True
        return False

    def vytvor_testovacieho_vitaza(self):
        for i in range(5):
            self.data[i][i] = "o"
        return


class Players:
    def __init__(self, meno1, meno2):
        self.meno1 = meno1
        self.meno2 = meno2
        self.mena = [meno1, meno2]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.mena):
            name = self.mena[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration

    def privitaj_hracov(self):
        for name in self.mena:
            print(f"Vitaj hráč: {name}")
        print("Hra môže začať na ťahu je hráč 1. \nZadaj súradnice pre uloženie Tvojej značky.")
        print("Hráč 1 ukladá značku o, hráč 2 ukladá značku x.")

    @classmethod
    def zadaj_mena(cls):
#        meno1 = input("Zadaj meno hráča 1: ")
#        meno2 = input("Zadaj meno hráča 2: ")
        meno1 = "Test1"
        meno2 = "Test2"
        return cls(meno1, meno2)


def zadaj_pociatocne_hodnoty():
    print("Cieľom hry PIŠKVORKY je postaviť v horizontále, vertikále alebo diagonále 5 vlastných značiek pri sebe.")
    print("Hru vyhráva ten, kto ich postaví, ako prvý.")
    print("\n")
    print("Na počiatku hry vytvoríme hracie pole o veľkosti 10x10 až 30x30.  ")
    print("Zadajte číslo v intervale 10 až 30 na určenie veľkosti hracieho poľa: ", end="")
    opakuj = True
    velkost = 1
    while opakuj:
        velkost = get_input()
        if 10 <= velkost <= 30:
            opakuj = False
        else:
            print("Zadané číslo nemá hodnotu z intervalu 10 až 30. Opakujte voľbu, prosím: ", end="")
    # nastav maticu na hodnotu velkost
    print("Vytvorili ste hracie pole o veľkosti ", velkost, "x", velkost, ".")
    return velkost


def get_input():
    while True:
        try:
#            x = int(sys.stdin.readline())
            x = 10
            return x
        except ValueError:
            print("Chybné zadanie, prosím, zadajte platné číslo: ", end="")


def zadaj_volbu(retazec):
    while True:
        user_input = input(retazec).strip().lower()
        if user_input == 'a' or user_input == 'n':
            return user_input
        else:
            print("Invalid input. Please enter 'a' or 'n'.")


def zobraz_obsah_suboru(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  # Use end='' to prevent extra newline characters
    except FileNotFoundError:
        print("Súbor nebol nájdený:", file_path)


class TestMatica(unittest.TestCase):
    def test_over_volnu_bunku(self):
        # Assuming `matica` is an instance of the Matica class
        result = matica.over_volnu_bunku(1, 2)
        self.assertTrue(result)

# testy




# zadaj rozmery hracieho poľa
# rozmer = zadaj_pociatocne_hodnoty()
rozmer = 25
matica = Matica(rozmer, rozmer)
# zadaj mená hráčov
players = Players.zadaj_mena()
players.privitaj_hracov()
# zobrazenie hracej plochy
matica.hracia_pocha()
matica.over_vitaza("x")
matica.over_vitaza("o")
# test

if __name__ == '__main__':
    unittest.main()

hra = True
kolo = 0
# nastavenie času začiatku hry
start_time = time.time()
while hra:
    kolo += 1
    # tah hraca 1, zaroven overuje, ci je bunka volna
#    matica.zadaj_suradnice_tahu(players.meno1)
    # zobrazenie hracieho pola
    matica.hracia_pocha()
    # over vitaza
    if matica.over_vitaza("o"):
        print("hra sa skončila víťazstvom hráča 1", players.meno1)
        vitaz = players.meno1
        hra = False
    else:
#        matica.zadaj_suradnice_tahu(players.meno2)
        # zobrazenie hracieho pola
        matica.hracia_pocha()
        if matica.over_vitaza("x"):
            print("hra sa skončila víťazstvom hráča 2, menom: ", players.meno2)
            vitaz = players.meno2
            hra = False
    hra = False
        # kontrola moznej vyhry
# výpočet času trvania hry
vitaz = "Testovaci vitaz"
end_time = time.time()
total_time = end_time - start_time
elapsed_timedelta = timedelta(seconds=total_time)
formatted_total_time = str(elapsed_timedelta)
# zápis záznamu z hry do súboru
print("Vykonávam záznam z hry do súboru zaznamy.txt")
# from datetime import datetime
# Aktuálny čas
current_datetime = datetime.now()
# názov súboru so záznamom hry
file_name = "zaznam.txt"
current_datetime_length = 20
vitaz_length = 15
kolo_length = 3
total_time_length = 10
# formátované premenné pre zápis
formatted_datetime = f"{current_datetime.strftime('%Y-%m-%d %H:%M:%S'):<{current_datetime_length}}"
formatted_vitaz = f"{vitaz[:vitaz_length]:<{vitaz_length}}"
formatted_kolo = f"{kolo:<{kolo_length}}"
# formatted_total_time = f"{total_time.strftime('%H:%M:%S'):<{total_time_length}}"
print("Aktuálny dátum a čas ukončenia hry: ", formatted_datetime)
print("Víťazom je hráč: ", formatted_vitaz)
print("Počet kôl: ", formatted_kolo)
print("Dĺžka trvania hry: ", formatted_total_time)

with open(file_name, "a") as file:
    record = "dátum: " + formatted_datetime + ", víťaz: " + formatted_vitaz + ", počet odohraných kôl: " + formatted_kolo + ", dĺžka trvania hry: " + formatted_total_time + "\n"
    file.write(record)
print("Hra ukončená")

#if zadaj_volbu("Zadajte 'a' pre možnosť zobrazenia histórie hier, alebo 'n' pre opustenie hŕy bez zobrazenia histórie.") == "a":
#    print("\nZobrazenie histórie odohraných hier:")
#    zobraz_obsah_suboru(file_name)
#else:
#    print("Ukončenie bez zobrazenia súboru s históriou hier.")
print("Dovidenia pri ďalšej hre")



"""
######################
STARY PROJEKT
######################
# startove hodnoty pre hraciu plochu
def reset_matrix():
    hracie_pole = [["_", "_", "_"],
                   ["_", "_", "_"],
                   ["_", "_", "_"]]
    return hracie_pole


def input_player_name():
    name = input("zadaj meno hráča: ")
    return name


def get_input():
    x = int(sys.stdin.readline())
    return x


def input_suradnice_tahu(player_nr, matrix_e):
    a = 0
    b = 0
    prebieha = True

    while prebieha:

        print("Player ", player_nr, ". Enter x coordinate for input")
        a = get_input()
        if a < 1:
            print("hodnoty môžu byť z intervalu <1,3>. Zadajte znovu")
        elif a > 3:
            print("hodnoty môžu byť z intervalu <1,3>. Zadajte znovu")
        else:
            prebieha = False

        print("Enter y coordinate for input")
        b = get_input()
        if b < 1:
            print("hodnoty môžu byť z intervalu <1,3>. Zadajte znovu")
        elif b > 3:
            print("hodnoty môžu byť z intervalu <1,3>. Zadajte znovu")
        elif check_free_item(matrix_e, a, b):
            prebieha = False
        elif matrix_e[a - 1][b - 1] != "_":
            print("zadali ste súradnice poľa, ktoré už obsahuje hrací kameň. Prosím, opakujte znova!")
            prebieha = True
    if player_nr == 1:
        matrix_e[a - 1][b - 1] = "o"
    else:
        matrix_e[a - 1][b - 1] = "x"
    return matrix_e


def check_free_item(matrix_M, c, d):
    if matrix_M[c - 1][d - 1] == "_":
        answer = True
    else:
        answer = False
    return answer


def check_matrix_winner(matrix_D):
    go_on = True
    for i in range(0, 3):
        j = 0
        if matrix_D[i][j] == matrix_D[i][j + 1] == matrix_D[i][j + 2] != "_":
            go_on = False
    if go_on:
        for j in range(0, 3):
            i = 0
            if matrix_D[i][j] == matrix_D[i + 1][j] == matrix_D[i + 2][j] != "_":
                print("vyhral")
                go_on = False
    if go_on:
        if matrix_D[0][0] == matrix_D[1][1] == matrix_D[2][2] != "_":
            print("vyhral")
            go_on = False
    if go_on:
        if matrix_D[0][2] == matrix_D[1][1] == matrix_D[2][0] != "_":
            print("vyhral")
            go_on = False
    return go_on


def print_hracie_pole(pole, rows, columns):
    k = 0
    l = 0
    print("  ", end="")
    for f in range(1, 4):
        print(f, end=" ")
    print("\n")
    for l in range(0, rows):
        print(l + 1, end=" ")
        for k in range(0, columns):
            print(pole[l][k], end=" ")
        print("\n")
    return

#   PROGRM


# create matrix 3x3 and set variables
matrix = [["", "", ""],
          ["", "", ""],
          ["", "", ""], ]
#   print(matrix)

matrix = reset_matrix()

riadok = 1
stlpec = 1
hra = True
players = ["AA", "BB"]
print(players)
print(matrix)
print("------------------------\n")
print("-  Zadanie mien hráčov -\n")
print("------------------------\n")
print("dĺžka poľa matrix je: ", len(matrix))
print("dĺžka poľa players je: ", len(players))
print(players)
#  print matrix on start ###########
print_hracie_pole(matrix, 3, 3)

#  Zadanie mien hráčov
i = 0
for i in range(0, 2):
    players[i] = input_player_name()
print("************")
#  ##############################################
#  print names of players and corresponding sign
#  #############################################
print("Vitaj hráč 1: ", players[0], ". Tvoj hrací kameň je o")
print("Vitaj hráč 2: ", players[1], ". Tvoj hrací kameň je x")


#  Program jadro

a = True
#   prebieha = True
hra = True



for round_id in range(1, 6):
    print("Round: ", round_id)
    hra = check_matrix_winner(matrix)
    print(hra)
    for player in range(1, 3):
        print("Player ", player, " to turn:")
        input_suradnice_tahu(player, matrix)
        print_hracie_pole(matrix, 3, 3)
        a = check_matrix_winner(matrix)
        if not a:
            print("************ VYHRAL************")
            break

    if not a:
        print("************ VYHRAL************")
        break"""
