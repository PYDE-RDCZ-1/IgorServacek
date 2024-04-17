# Napiš funkci pro zapsání položek nákupního seznamu do textového souboru.

def zapis_text (text, subor):
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
            print("Obsah suboru: ", subor, "je:\n", str(obsah) )
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
    # pridanie položiek nakupného zoznamu do suboru (subor)
    if type(retazec) != str:
        retazec = str(retazec)
    try:
        with open(subor, 'a') as subor:
            subor.write(retazec)
    except FileNotFoundError:
        print("nenajdeny subor")
    except PermissionError:
        print("nemate povolenie na citanie tohoto suboru")
    return


def pridaj_polozku(subor, item, number):
    # pridanie položky do súboru s nákupným zoznamom
    try:
        with open(subor, 'a') as subor:
            subor.seek(0,2)
            subor.write(f"{item}, {number}\n")
    except FileNotFoundError:
        print("nenajdeny subor")
    except PermissionError:
        print("nemate povolenie na citanie tohoto suboru")
    return


nak_zoznam = {
    ("kofola", 2),
    ("múka", 3),
    ("minerálka", 6),
    ("maslo", 2)
}

print(type(nak_zoznam))
naz_suboru = input("Zadaj názov txt súboru v tvare nazov.txt:")
vymaz_subor(naz_suboru)
zoz = str(nak_zoznam)
print(zoz)
zapis_text(nak_zoznam,naz_suboru)
zobraz_subor(naz_suboru)
# manuálny vstup položiek nákupu
cyklus = True
print("Ak zadáš počet kusov v nákupnej položke == 0, ukončíš zadávanie položiek zoznamu.")
while cyklus == True:
    polozka = input("zadaj názov nákupnej položky: ")
    pocet = input("zadaj počet kusov danej položky: ")
    if int(pocet) == 0:
        cyklus = False
    else:
        pridaj_polozku(naz_suboru, polozka, pocet)

zobraz_subor(naz_suboru)
