# Úloha 8
# Lekce 7: Pomocí podmínek a for cyklu vytvoř nový slovník obsahující
# cenové kategorie (levné, středně drahé, drahé) položek z našeho nákupního seznamu.

my_list = [("mlieko", 0.8), ("múka hladká", 1.2), ("chlieb", 2.2), ("maslo", 2.6)]

my_dictionary = dict(my_list)
# print("my_dictionary zo zoznamu my_list:", my_dictionary)
# hranice rozhodovania
lacne = 1
stredne_drahe = 2
#   print(len(my_dictionary))   ,  m
new_dictionary ={}

for item in my_dictionary:
#    if my_dictionary[item] <= lacne:
    if  my_dictionary[item] <= lacne:
        new_dictionary[item] = my_dictionary[item]
        new_dictionary[item] = "lacné"
    elif my_dictionary[item] <= stredne_drahe:
        new_dictionary[item] = my_dictionary[item]
        new_dictionary[item] = "stredne drahé"
    else:
        my_dictionary[item] > stredne_drahe
        new_dictionary[item] = my_dictionary[item]
        new_dictionary[item] = "drahé"

print("Pôvodný slovník s cenami:", my_dictionary)
print("Upravený slovník, zoznam dvojíc kľúč/hodnota v dictionary: ", (new_dictionary).items())
print("Upravený slovník s kategóriami cien", new_dictionary)

print(my_dictionary["mlieko"])
print(my_dictionary.keys())
print(type(my_dictionary))