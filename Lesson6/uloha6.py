# Zadání
# Transformuj předchozí vytvořené nákupní seznamy na datový typ dictionary (slovník) a to tak,
# že jako klíč použiješ název položky a jako hodnotu cenu dané položky.


my_list = [("mlieko", 0.8), ("múka hladká", 1.2), ("chlieb", 2.2), ("maslo", 2.6)]
print(my_list)
my_dictionary_1 = dict(my_list)
print("Dictionary za pomoci dict():", my_dictionary_1)

my_dictionary = {key: value for key, value in my_list}
print("Dictionary za pomoci definovania: ", my_dictionary)
print(my_dictionary["mlieko"])


# výstupy, mimo úlohy
print("Počet prvkov v dictionary: ", len(my_dictionary))
print("Zoznam kľúčov v dictionary: ", (my_dictionary).keys())
print("Hodnoty prvkov v dictionary: ",  (my_dictionary).values())
print("Zoznam dvojíc kľúč/hodnota v dictionary: ",  (my_dictionary).items())
print("Zobraz hodnotu ku kľúču maslo: ",  (my_dictionary).get( "maslo"))
print("Zobraz hodnotu ku kľúču chlieb: ", (my_dictionary).pop("chlieb"))
print("Zobraziť dictionary bez prvku s kľúčom chllieb: ",  my_dictionary)
print("Počet prvkov v dictionary: ", len(my_dictionary))


