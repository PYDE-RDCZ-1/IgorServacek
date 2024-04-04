# Vytvořte si vlastní projekt s komplexní funkcionalitou. Využijte co nejvíce dosud získaných znalostí,
# dodržujte konvence, vytvářejte funkce nebo samostatné moduly. Inspirujte se příklady v prezentaci.
# from typing import List, Any


#   popis projektu: hra. Uhádni, aké číslo medzi 1-100 (vrátane) si myslím. Hráč háda ˇćislo, aké si myslí počítač.
#   počitač si odpamäta postupnosť %čísiel, ktorú si hráč postupne zadal.


def check(vzor: int, number: int):
#   kontrola správne zadaných hraníc intervalu pre hru
    dalej = True
    if number == vzor:
        print("Uhádol si, myslené číslo je: ", number)
        dalej = False
    elif number < vzor:
        print("Číslo, ktoré si zadal, je menšie od mysleného čísla")
    elif number > vzor:
        print("Číslo, ktoré si zadal, je väčšie od mysleného čísla")
    return dalej


def give_number():
# generovanie náhodného celého čísla zo zadného intervalu
    global low_b, high_b
    import random
    nr = random.randint(low_b, high_b)
    return nr


def record_move(record):
# áznam priebehu hry
    game_record.append(record)
    pass


def border():
#   zadanie intervalu pre hru
    global low_b, high_b
    go = True
    while go:
        low_b = input("Zadaj spodnú hranicu intervalu pre hľadanie čísla: ")
        high_b = input("Zadaj hornú hranicu intervalu pre hľadanie čísla: ")
        if low_b.isdigit() and high_b.isdigit():
            print(type(low_b), type(high_b))
            print(low_b, high_b)
            if int(low_b) < int(high_b):
                print("Tvoje zadanie bolo akceptované, budeš hádať číslo v intervale od ",low_b, " do ", high_b, ".")
                go = False
        else:
            print("Nesprávne zadané hranice. Opakuj zadanie.")
    return


#   Program Hra
global low_b, high_b, game_record
game_record = []
print("****************************************")
print("Vitaj v hre. Počítač generuje celé číslo v intervale, ktorý sám nastavíš.")
print("Tvojou úlohou bude uhádnuť ho na čo najmenej pokusov.")
print("Pre opustenie hry zadaj číslo 0.")
meno = input("Zadaj svoje meno: ")
border()
low_b = int(low_b)
high_b = int(high_b)
hadanka = give_number()
game = True
count = 0
while game:
    count += 1
    pokus = int(input("Zadaj číslo: "))
    if pokus == "0":
        print("Opustil si hru stlačením klávesu 0.")
        rame = False
    record_move(pokus)
    game = check(hadanka, pokus)

print(meno, ", Tvoje ťahy boli nasledovné: ", game_record, " využil si ", count, " ťahy/ov.")
