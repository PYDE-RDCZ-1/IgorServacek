#   Cvicenie 9
def sucet(a, b):
    vyledok = a + b
    print(vyledok)


vysledok = sucet(5, 4)
print(vysledok)


def super_function():
    pass


super_function()
pass


print(super_function())


def spocitaj(words):
    slovnik = {}
    for item in words:
        #   odstranenie neziaducich znakov a eliminovanie velkych pismen
        item = item.strip(",.!?").lower()
        if slovnik.get(item):
            word_count = slovnik.get(item)
            slovnik[item] = word_count + 1
            print(item, slovnik[item])
        else:
            slovnik[item] = 1
            print(item, slovnik[item])
    print(slovnik)
    return(slovnik)


veta = input("Zadaj reťazec s opakovaním: ")
spocitaj(veta)

#   PR










def kalkulacka(string):
    string = vstup.strip(",.!?")
    print(type(string))
    if "+" in string:
        index = string.find("+")
        print(int(string[0:index]), int(string[index+1:]))
        print(int(string[0: index]) + int(string[index+1:]))
    elif "-" in string:
        index = string.find("-")
        print(int(string[0:index]), int(string[index + 1:]))
        print(int(string[0: index]) - int(string[index + 1:]))
    elif "*" in string:
        index = string.find("*")
        print(int(string[0:index]), int(string[index + 1:]))
        print(int(string[0: index]) * int(string[index + 1:]))
    elif "/" in string:
        index = string.find("/")
        print(int(string[0:index]), int(string[index + 1:]))
        if int(string[index + 1:]) == 0:
            index = string.find("/")
            print("nema riesenie")
    else :
        index = string.find("/")
        print(int(string[0: index]) / int(string[index + 1:]))
    return
u = 1
while u < 10:
    u = u + 1
    vstup = input("zadajte cislo, operacia, cislo: ")
    vysledok = kalkulacka(vstup)