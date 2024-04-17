from typing import TextIO

try:
    with open("priklad15.txt", "r+") as subor:
        subor.write("Ahoj\n")
        subor.seek(0)
        print(subor)
        obsah = subor.read()
        subor.seek(0, 2)
        subor.write("na zaciatok")
        obsah = subor.read()
        print(obsah)
except FileNotFoundError:
    print("nenajdeny subor")
except PermissionError:
    print("nemate povolenie na citanie tohoto suboru")


try:
    with open("priklad15.txt", "r+") as subor:
        obsah = subor.read()
        print(obsah)  # Removed quotes around obsah to print the actual contents
except FileNotFoundError:
    print("nenajdeny subor")
except PermissionError:
    print("nemate povolenie na citanie tohoto suboru")



try:
    with open("priklad15.txt", "r+") as subor:
        retazec = subor.read()
        print(retazec)
        words = retazec.split()
        print(words)
        print("dlzka je: ", len(words))
except FileNotFoundError:
    print("nenajdeny subor")
except PermissionError:
    print("nemate povolenie na citanie tohoto suboru")



try:
    subor: TextIO
    with open("priklad15.txt", "a") as subor:
        subor.write("pridany text \n")
        print("dlzka je: ", len(obsah))
except FileNotFoundError:
    print("nenajdeny subor")
except PermissionError:
    print("nemate povolenie na citanie tohoto suboru")


try:
    subor: TextIO
    with open("priklad15.txt", "r+") as subor:
        obsah = subor.read()
        slova = obsah.split()
        print(obsah)
        print("pocet znakov je: ", len(obsah))
        print("pocet slov je: ", len(slova))
except FileNotFoundError:
    print("nenajdeny subor")
except PermissionError:
    print("nemate povolenie na citanie tohoto suboru")