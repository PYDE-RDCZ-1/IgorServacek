# Program na validáciu rodného čísla
# validace rodneho cisla
# nacteni vsupu - tvar bez lomitka     ok
# 9 nebo 10 znaku - typ int     ok
# if 10 znaku then delitelne 11 beze zvyšku         ok
# if 9 znaku then rok < 1.1.1954            ok
# určení datumu narození
# prvych 6 čísel -> 3 promenne - rok_narozeni, mesic_narozeni, den_narozeni
# kalkulace celého roku narození            ok
# mesic_narozeni a zaroven urcime pohlavi -> skusíme odečíst 20, 50, 70; výsledek porovnáme s intervalem <01,12>
# vypocet prestupni rok
# den_narozeni -> odvodime od prestupniho roku a mesice


def validacia_rc(cislo):
    global rc, datum, rok, mes, den, pohlavie, vydanie, rok_nar, mes_nar, den_nar
    # 10 znakove je delitelne 11
    # 9 znakov, narodenie pred 1.1.1954
    dlzka = len(cislo)
    datum = int(cislo[0:6])
    rok = int(cislo[0:2])
    mes = int(cislo[2:4])
    den = int(cislo[4:6])
    pohlavie = ""
    rc = int(cislo)
    chyba = True
    vydanie = ""
    if dlzka == 10 and rc % 11 == 0 and rok >= 54:
        # over ci muz, ci zena
        if mes <= 12:
            pohlavie = "muz"
            print("pohlavie muz")
            vydanie = "new"
        elif 51 <= mes <= 62:
            pohlavie = "zena"
            print("pohlavie zena")
            vydanie = "new"
#        print("zadane cislo, typu od 1.1.1954")
    elif dlzka == 9 and rok < 54 and (mes < 13 or 50 < mes < 63):
        # over ci muz, ci zena
        if mes <= 12:
            pohlavie = "muz"
            vydanie = "old"
            print("pohlavie muz")
        elif 51 <= mes <= 62:
            pohlavie = "zena"
            vydanie = "old"
            print("pohlavie zena")
#        print("zadane cislo, typu pred 1.1.1954")
    else:
        chyba = False
        print("nekorektne zadane cislo. Nie je delitelne 11")
    if chyba:
        # validacia_datumu_narodenia(rok, mes, den, pohlavie, vydanie)
        validacia_datumu_narodenia()
    return chyba


def kontrola_dna():
    global rc, datum, rok, mes, den, pohlavie, vydanie, rok_nar, mes_nar, den_nar
    # kontrola správneho zadania dna k mesiacu
#    print("kontrola mesiac:", mes)
    if mes <= 7:
        if mes % 2 == 0 and mes != 2:
            # párny mesiac (4,6)
            if den <= 30:
                # správny počet dní v mesiacoch 4,6
                tlac_den()
                print("zadaný korektný deň v mesiaci (<=30)")
            else:
                print("zadaný nekorktný  deň v mesiaci (>30)")
#        elif mes == 2:
#                je_priestupny_rok()
        else:
            # nepárny mesiac (1,3,5,7
            if den <= 31:
                # správny počet dní v mesiacoch 1,3,5,7
                tlac_den()
                print("zadaný korektný  deň v mesiaci (<=31)")
            else:
                print("zadaný nekorktný  deň v mesiaci (>31)")
    elif mes >= 8:
        if mes % 2 == 0:
            # párny mesiac (8,10,12)
            if den <= 31:
                # správny počet dní v mesiacoch 8,10,12
                tlac_den()
                print("zadaný korektný  deň v mesiaci (<=31)")

            else:
                print("zadaný nekorktný  deň v mesiaci (>31)")
        else:
            # nepárny mesiac (9,11)
            if den <= 30:
                # správny počet dní v mesiacoch 1,3,5,7
                tlac_den()
                print("zadaný korektný  deň v mesiaci (<=30)")
            else:
                print("zadaný nekorktný  deň v mesiaci (>30)")
    return


def tlac_den():
    global den
    print("den je: ", den)
    return


def validacia_datumu_narodenia():
    # def validacia_datumu_narodenia(rok, mes, den, pohlavie, vydanie):
    global rc, datum, rok, mes, den, pohlavie, vydanie, rok_nar, mes_nar, den_nar
#   podla roku overuje typ rc
    if vydanie == "old":
        print("starý typ rc")
        if rok < 54:
            rok_nar = int("19" + str(rok))
            print("rok narodenia je: ", rok_nar)
    elif vydanie == "new":
        print("nový typ rc")
        if 53 < rok <= 99:
            rok_nar = int("19" + str(rok))
            print("rok narodenia je: ", rok_nar)
        elif 0 <= rok <= 24:
            rok_nar = int("20" + str(rok))
            print("rok narodenia je: ", rok_nar)
# nastavenie mesiaca podla rc pre muza aj pre zenu a jeho zobrazenie
    if pohlavie == "muz":
        if 1 <= mes <= 12:
            print("mesiac je: ", mes)
        else:
            print("chyba zadania mesiaca")
    elif pohlavie == "zena":
        mes = mes - 50
        print("mesiac je: ", mes)
    kontrola_dna()
    # nastavenie a overenie dna podla kalendára
    # den_nar = int(den)
    # print("den narodenia je: ", den_nar)
#   ako cheme zobrazovat prietupny/nepriestupny rok, pouzi nasl. riadok
    je_priestupny_rok()
    return


def je_priestupny_rok():
    # overenie priestupneho roka
    global rc, datum, rok, mes, den, pohlavie, vydanie, rok_nar, mes_nar, den_nar
    if rok_nar % 400 == 0 or rok_nar % 4 == 0 and rok_nar % 100 != 0:
        print("narodený v priestupnom roku")
        if mes == 2 and den > 29:
            print("vybraný deň v mesiaci február je nekorektný")
    else:
        print("narodený v nepriestupnom roku")
    return


def zadaj_rc():
    global rc, datum, rok, mes, den, pohlavie, vydanie, rok_nar, mes_nar, den_nar
    cyklus = True
    is_int = True
    while cyklus:
        try:
            rc = input("zadajte Vase rodne cislo v tvare rrmmddxxxx : ")
            int(rc)
        except ValueError:
            print("zadali ste chybné číslo")
        else:
            if not type(isinstance(rc, int)):
                is_int = False
                print("Vami zadana hodnota rc obsahuje nepovolene znaky")
            if (len(rc) == 10 or len(rc) == 9) and is_int:
                print("zadané číslo: ", rc, " má správny počet číslic: ", len(rc))
                cyklus = False
            else:
                print("dĺžka rc je nesprávna, zadali ste : ", len(rc), " znakov. ")
    return rc


# Main
# nacitanie vstupu rc
global rc, datum, rok, mes, den, pohlavie, vydanie, rok_nar, mes_nar, den_nar


zadaj_rc()
validacia_rc(rc)
# kontrola_dna()
