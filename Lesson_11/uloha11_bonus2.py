# Projekt generátora náhodných hesiel
# program generuje heslá v rozsahu 5 - 12 znakov z abecedy, ktorá je defivan'=a v program (obsahuje malé, veĺké písmená, číslice a zvláštne znaky

import random
# definovanie znakov, z ktprých pozostáva množina znakov na zopstavenie hesla


def generuj_heslo(dlzka):
    heslo = ""
    index_A = abeceda.index("A")
    index_Z = abeceda.index("Z")
    for i in range (0, dlzka):
# Prvý znak hesla je veľké písmeno
        if i == 0:
            index = (random.randint(index_A, index_Z))
            heslo += abeceda[index]
        else:
            index = (random.randint(0, dlzka_abecedy))
            heslo += abeceda[index]
    return heslo

# Telo programu
global abeceda, dlzka_abecedy
abeceda = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZ./?_%0123456789#&"
dlzka_abecedy = len(abeceda)
print("Toto sú povolené znaky, pre zostavenie hesla: \n", abeceda)
dlzka_abecedy = len(abeceda)
check = True
while check:
    dlzha_hesla = int(input("Zadajte pocet znakov na generovanie hesla (min. 5, max.12):"))
    if dlzha_hesla >= 5 and dlzha_hesla <= 12:
        nove_heslo = generuj_heslo(dlzha_hesla)
        print("Vaše nové heslo je: ", nove_heslo)
        check = False
    else:
        print("Zadali ste zlú hodnotu mimo povoleného intervalu.")
