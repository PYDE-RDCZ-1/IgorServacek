#   Úloha 9
#   Lesson 9:
#   Volanie funkcie kalkulačka ako reťazca čilo + funkcia + číslo
#   kalkulacka osetruje delnie nulou a nezadaný/zabudnutý argumernt

def kalkulacka(string):
    string = vstup.strip(",.!?")
    if "+" in string:
        index = string.find("+")
        if len(string[0: index]) == 0 or len(string[index + 1:]) == 0:
            print("sčítanec nebol nájdený")
        else:
            print(int(string[0: index]) + int(string[index+1:]))
    elif "-" in string:
        index = string.find("-")
        if len(string[0: index]) == 0 or len(string[index + 1:]) == 0:
            print("argument nebol nájdený")
        else:
            print(int(string[0: index]) - int(string[index + 1:]))
    elif "*" in string:
        index = string.find("*")
        if len(string[0: index]) == 0 or len(string[index + 1:]) == 0:
            print("činiteľ nebol nájdený")
        else:
            print(int(string[0: index]) * int(string[index + 1:]))
    elif "/" in string:
        index = string.find("/")
        if len(string[0: index]) == 0 or len(string[index + 1:]) == 0:
            print("delenec, alebo deliteľ nebol nájdený")
        else:
            if int(string[index + 1:]) == 0:
                print("nema riesenie/delenie nulou")
            else:
                print("nema riesenie/delenie nulou")
    else:
        print(string)
        print("Nezadali ste operáciu")
    return


vstup = "1"
while vstup != "0":
    vstup = input("Zadajte celé číslo ľubovoľnú operaciu a celé číslo (Pr: 100+80): ")
    print("Výsledok je: ", end="")
    if vstup == "0":
        print("Ukončili ste prácu kalkulačky zadaním čisla 0")
    else:
        kalkulacka(vstup)

#   print("ukončili ste vstup zadaním hodnoty 0, alebo maximálnym počtom cyklov.")






# funkcia faktoriál

def faktorial (argument):
    sum = 1
    while argument > 0:
       sum = sum * argument
       argument = argument - 1
    return (sum)
print("program pre výpočet faktoriálu čisla")
cislo = int(input(" Zadaj číslo pre výpočet faktoriálu (!): "))
print(cislo,"! = ", faktorial(cislo))