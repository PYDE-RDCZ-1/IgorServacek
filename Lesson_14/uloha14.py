# napisat 2 testy, použité v programe na generovanie rodného čísla
# 1. test kontroluje dĺžku generovaného císla
# 2. test kontroluje deliteľnosť 11

import random
import calendar
import pytest

def generuj_nahodny_den():
    # od 1900 po dnešok
    rok = random.randint(1900, 2023)  # Change 2023 to the desired end year
    rok_skrateny = str(rok)
#    print(rok_skrateny)
    # mesic od 1 po 12
    mesiac = random.randint(1, 12)

    # počet dní v danom mesiaci a roku
    den = calendar.monthrange(rok, mesiac)[1]
    # generovanie náhodného dňa v príslušnom mesiaci
    denday = random.randint(1, den)
    return rok, mesiac, den


def dopln_kod(rok, kod):
#   generovanie pohlavia (1 = zena, 2 = muz)
    pohl = generuj_pohavie()
    if pohl == 1:
        # zena
#        print ("kod: ", kod)
        if rok > 1953:
            a = random.randint(0, 9999)
            b = int(kod) * 10000 + 5000000 + a
        elif rok < 1954:
            a = random.randint(1, 999)
            b = int(kod) * 1000 + a + 5000000
    elif pohl == 2:
        # muz
        if rok > 1953:
            a = random.randint(1, 9999)
            b = int(kod) * 10000  + a
#            print(a, b)
        elif rok < 1954:
            a = random.randint(1, 999)
            b = int(kod) * 1000 + a
#           print(a, b)
#           print(b)
    c = b % 11
    b += (11 - c)
#    print("rodné číslo: ", b)
    if rok < 1954 and len(str(b)) == 8:
        b = "0" + str(b)
    elif rok >= 1954 and len(str(b)) == 9:
        b = "0" + str(b)
    print("rodné číslo: ", b)
    return b


def generuj_pohavie():
    p = random.randint(1, 2)
    if p == 1:
        print("pohlavie = zena")
    elif p ==2:
        print("pohlavie muz")
    return p


def test_rc():
# testy na dĺžku rodného čísla a deliteľnos't 11
    assert len(str(rc)) == 10 or len(str(rc)) == 9, "dĺžka rodného čísla nezodpovedá predpísanej dĺžke"
    assert int(rc) % 11 == 0, "číslo nie je deliteľné 11"


# x =0
# print("Generator rodných čísiel vytlačí 8 rôznych RČ:")
# cyklus = int(input("zadajte počet generovaných rodných čísiel: "))
for x in range(0, 8):
    nahodny_den = generuj_nahodny_den()
    print("Nahodny den:", nahodny_den, end=", ")
    if 1 <=nahodny_den[1] <= 9:
        nahodny_den_d = "0" + str(nahodny_den[1])
    else:
        nahodny_den_d = str(nahodny_den[1])
    datum_skr = str(nahodny_den[0])[2:4] + nahodny_den_d + str(nahodny_den[2])
    #    print(datum_skr)
    datum_cely = nahodny_den[0]
    #    print(rc_datum)
    print(datum_skr, datum_cely)

rc = dopln_kod(datum_cely, datum_skr)
test_rc()


