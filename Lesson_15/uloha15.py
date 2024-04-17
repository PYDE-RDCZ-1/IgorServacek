# Napiš funkci pro zapsání položek nákupního seznamu do textového souboru.


def zapis_text(text, subor):
    # zapis nakupneho zoznamu (text) do suboru (subor)
    # ak neexistuje subor, tak ho vytvori
    try:
        with open(subor, 'w+') as subor:
            for item in text:
                subor.write(f"{item[0]}, {item[1]}\n")
    except FileNotFoundError:
        print("nenajdeny subor")
    except PermissionError:
        print("nemate povolenie na citanie tohoto suboru")
    return


def zobraz_subor(subor):
    # zobrazenie obsahu suboru s nazvom (subor)
    try:
        with open(subor, '+r') as subor:
            obsah = subor.read()
            print(obsah)
            print("Súbor ", subor, " obsahuje nasledovný zoznam: \n", str(obsah))
    except FileNotFoundError:
        print("nenajdeny subor")
    except PermissionError:
        print("nemate povolenie na citanie tohoto suboru")
    return


def vymaz_subor(naz):
    # vymazanie suboru z predchadzajuceho behu programu
    with open(naz, "w") as file:
        pass
    return


def pridaj_text(subor, retazec):
    # jednorazové pridanie položiek nakupného zoznamu (retazec) do suboru (subor)
    if type(retazec) / str:
        retazec = str(retazec)
    try:
        with open(subor, 'a') as subor:
            subor.write(retazec)
    except FileNotFoundError:
        print("nenajdeny subor")
    except PermissionError:
        print("nemate povolenie na citanie tohoto suboru")
    return


def pridaj_polozku_v_subore(txtsubor, retazec, pocet):
    # najdeny = False
    try:
        with open(txtsubor, 'r') as file:
            content = file.read()
            content = content.replace(",", "")
            slova = content.split()
            if retazec in slova:
                print("položka nájdená. Nový záznam pripisujem na koniec súboru.")
                with open(txtsubor, 'a') as novy_subor:
                    novy_subor.seek(0, 2)
                    novy_subor.write(f"{retazec}, {pocet}\n")
            else:
                print("položka nenájdená, zapisujem nový riadok.")
                with open(txtsubor, 'a') as novy_subor:
                    novy_subor.seek(0, 2)
                    novy_subor.write(f"{retazec}, {pocet}\n")
    except FileNotFoundError:
        print("nenajdeny subor")
    except PermissionError:
        print("nemate povolenie na citanie tohoto suboru")
    return


def osetri_subor(file):
    # sumarizácia jednotlivých položiek podľa názvu (odstránenie opakovania položiek a ošetrenie súčtov podĺa polo%ziek)
    sumy = {}
    try:
        with open(file, 'r') as file:
            for line in file:
                # Split each line into items and numbers
                items, numbers = line.strip().split(',')
                numbers = int(numbers)
                if items in sumy:
                    sumy[items] += numbers
                else:
                    sumy[items] = numbers
            # zápis sumarizovaných poloźiek do zoznamu

        with open("kontrola.txt", 'w') as file_zapis:
            for items, total in sumy.items():
                file_zapis.write(f"{items},{total}\n")
#            print(summary)
    except FileNotFoundError:
        print("Vstupný súbor nebol nájdený.")
    print("Sumarizačný súbor vytvorený korektne.")

    return


nak_zoznam = {
    ("kofola", 2),
    ("múka", 3),
    ("minerálka", 6),
    ("maslo", 2)
}

naz_suboru = input("Zadaj názov txt súboru v tvare nazov.txt:")
vymaz_subor(naz_suboru)
zoz = str(nak_zoznam)
print("Počiatočný nákupný zoznam je: ", zoz)
zapis_text(nak_zoznam, naz_suboru)
# zobraz_subor(naz_suboru)
# manuálny vstup položiek nákupu
cyklus = True
print("Ak zadáš počet kusov v nákupnej položke == 0, ukončíš zadávanie položiek zoznamu.")
while cyklus:
    polozka = input("zadaj názov nákupnej položky: ")
    pocet = input("zadaj počet kusov položky: ")
    if int(pocet) == 0:
        cyklus = False
    else:
        pridaj_polozku_v_subore(naz_suboru, polozka, pocet)
#        zobraz_subor(naz_suboru)
print("Surový nákupný zoznam s opakujúcimi sa položkami: ")
zobraz_subor(naz_suboru)
osetri_subor(naz_suboru)
print("Upravený nákupný zoznam: ")
zobraz_subor(naz_suboru)
