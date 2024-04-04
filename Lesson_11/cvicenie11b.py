def detect_jednotky(ask):
    if ask[-1] == "m":
        print("prevod z metrov na cm")
    else:
        print("prevod z cm na metre")
    return()



def convert_cm_m(cislo):
    cislo = float(cislo/100)
    return(cislo)


def convert_m_cm(cislo):
    cislo = int(cislo * 100)
    return(cislo)

def detect(ret):
    if "cm" in ret:
        print("prevod cm na m")
        jednotka = "cm"
    elif "m" in ret:
        print("prevod m na cm")
        jednotka = "m"
    else:
        jednotka = "x"
    return(jednotka)


def odsekni_podretazec(retazec, sekvencia):
    if sekvencia in retazec:
        return retazec.replace(sekvencia,"")
    else:
        "miera nenájdená"
        return retazec


#   Program
# prevod cm na m a naopak. Stačí zadať čislo s mierou (m, alebo cm).
# Program sám vyhodnotí smer prevodu.
print("prevod cm na m a naopak. Stačí zadať čislo s mierou (m, alebo cm).")
print("Program sám vyhodnotí smer prevodu.")
print("Zadanie čísla 0 ukončuje slučku.")
run = True
while run:
    ret_in = input("zadaj cislo a jednotku, ktorú chces previest: ")
    if ret_in == "0":
        run = False
    else:
        a = detect(ret_in)
        if a == "m":
            vysledok = odsekni_podretazec(ret_in, "m")
            print (vysledok, " m = ",int(vysledok)*100, " cm")
        elif a =="cm":
            vysledok = odsekni_podretazec(ret_in, "cm")
            print(vysledok, " cm = ",int(vysledok) / 100, " m")
        elif a == "x":
            print("zle zadané miery")

print("Program ukončený")


