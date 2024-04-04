# Program na validáciu rodného čísla
# nacteni vsuptu
# validace rodneho cisla - tvar bez lomitka
# 9 nebo 10 znaku - typ int
# if 10 znaku then delitelne 11 beze zvyšku
# if 9 znaku then rok < 1.1.1954
# určení datumu narození
# prvych 6 čísel -> 3 promenne - rok_narozeni, mesic_narozeni, den_narozeni
# kalkulace celého roku narození
# mesic_narozeni a zaroven urcime pohlavi -> skusíme odečíst 20, 50, 70; výsledek porovnáme s intervalem <01,12>
# vypocet prestupni rok
# den_narozeni -> odvodime od prestupniho roku a mesice


def validacia_rc(cislo):
    # 10 znakove je delitelne 11
    # 9 znakov, narodenie pred 1.1.1954
    dlzka = len(cislo)
    datum = int(cislo[0:6])
    rok = int(cislo[0:2])
    mes = int(cislo[2:4])
    den = int(cislo[4:6])
    pohlavie = ""
    rc = int(cislo)
    if dlzka == 10 and rc % 11 == 0:
#        print("korektne zadane cislo")
# over ci muz, ci zena
        if mes <= 12:
            pohlavie = "muz"
            print("pohlavie muz")
            vydanie = "new"
        elif mes >= 51 and mes <= 62:
            pohlavie = "zena"
            print("pohlavie zena")
            vydanie = "new"
        print("korektne zadane cislo, typu od 1.1.1954")
    elif dlzka == 9 and rok < 54 and ( mes < 13 or mes > 50 and mes < 63):
        # over ci muz, ci zena
        if mes <= 12:
            pohlavie = "muz"
            vydanie = "old"
            print("pohlavie muz")
        elif mes >= 51 and mes <= 62:
            pohlavie = "zena"
            vydanie = "old"
            print("pohlavie zena")
        print("korektne zadane cislo, typu pred 1.1.1954")
    else:
        print("nekorektne zadane cislo. Nie je delitelne 11")
    validacia_datumu_narodenia(rok, mes, den, pohlavie, vydanie)
    return


def validacia_datumu_narodenia(rok, mes, den, pohlavie, vydanie):
#nastavenie roku
    print("zahajujem proces validacie datumu")
    if vydanie == "old" :
        print("starý typ rc")
        if rok <54:
            rok_nar = int("19" + str(rok))
            print("rok narodenia je: ", rok_nar)
    elif vydanie == "new":
        print("nový typ rc")
        if rok > 53 and rok <= 99:
            rok_nar = int("19" + str(rok))
            print("rok narodenia je: ", rok_nar)
        elif rok >= 0 and rok <= 24:
            rok_nar = int("20" + str(rok))
            print("rok narodenia je: ", rok_nar)
# nastavenie mesiaca
    if pohlavie == "muz":
        if mes >= 1 and mes <=12:
            print("mesiac je: ", mes)
        else:
            print("chyba zadania mesiaca")
    elif pohlavie == "zena":
            mes = mes - 50
            print("mesiac je: ", mes)
# nastavenie a overenie dna podla kalendára


    return

def zadaj_rc():
    cyklus = True
    while cyklus:
        try:
            rc = input("zadajte Vase rodne cislo v tvare rrmmddxxxx : ")
        except ValueError:
            print("zadali ste chybné číslo")
        else:
            print("zadali ste správne číslo: ", rc)
            cyklus = False
    return rc

#nacitanie vstupu rc
global rc, datum, rok, mes, den, pohlavie, vydanie
# vydanie =""
# rc_type pre datumy od 1.1.1954 je "new", pre dátumy pred týmto termínom je "old"

# rc = input("zadajte Vase rodne cislo v tvare rrmmddxxxx : ")

rc = zadaj_rc()
validacia_rc(rc)



# validace rodneho cisla
# nacteni vsuptu
# tvar bez lomitka
# 9 nebo 10 znaku - typ int     ok
# if 10 znaku then delitelne 11 beze zvyšku         ok
# if 9 znaku then rok < 1.1.1954            ok
# určení datumu narození
# prvych 6 čísel -> 3 promenne - rok_narozeni, mesic_narozeni, den_narozeni
# kalkulace celého roku narození            ok
# mesic_narozeni a zaroven urcime pohlavi -> skusíme odečíst 20, 50, 70; výsledek porovnáme s intervalem <01,12>
# vypocet prestupni rok
# den_narozeni -> odvodime od prestupniho roku a mesice