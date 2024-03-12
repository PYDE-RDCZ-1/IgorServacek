# Vezmi slovník z předchozího úkolu s položkami a cenami. Napiš program,
# který na vstupu načte název položky a vypíše její cenovou kategorii (levné, středně drahé, drahé).

my_list = [("mlieko", 0.8), ("múka hladká", 1.2), ("chlieb", 2.2), ("maslo", 2.6)]

my_dictionary = dict(my_list)
# print("my_dictionary zo zoznamu my_list:", my_dictionary)
# hranice rozhodovania
lacne = 1
stredne_drahe = 2
#   print(len(my_dictionary))   ,  možnosť použiť v prípade iného nastavenia cyklu, print(my_dictionary.keys())

print("Hraničné hodnoty pre kategorizáciu cien produktov 1.00 , 2.00")
print(" Produkt je lacný, ak jeho cena je <= 1.00")
print(" Produkt je stredne drahý ak jeho cena je <=2")
print(" Produkt je drahý, ak jeho cena je > 2.00")
print(" \nKategorizácia cien:\n")
for i in my_dictionary:
    if my_dictionary[i] <= lacne:
        print(i, my_dictionary[i], ", produkt je lacný")
    elif my_dictionary[i] > lacne:
        if my_dictionary[i] <= stredne_drahe:
            print(i, my_dictionary[i], ", produkt je stredne drahý")
        else:
            print(i, my_dictionary[i], ", produkt je drahý")
