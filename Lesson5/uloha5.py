#   Úloha 5 zo dňa 4/3/2024
#   Vypracoval:Igor Serváček

# Seznamy (Lists):
# ● Vytvořte seznam obsahující několik různých prvků (například čísla, řetězce).
my_list = [1, 3, 1000, ["Peter", "Pavol"], "počasie"]
print(my_list)


# ● Použijte metodu append() k přidání nového prvku na konec seznamu.
my_list.append("vzdialenosť")
my_list.append(100)
print(my_list)


# ● Použijte metodu insert() k vložení nového prvku na specifickou pozici v seznamu.
my_list.insert(2,"meno")
print(my_list)

# ● Použijte metodu remove() k odstranění konkrétního prvku ze seznamu.
my_list.remove("počasie")
my_list.remove("vzdialenosť")
my_list.remove("meno")
my_list.remove(my_list[3])
print(my_list)


# ● Použijte metodu sort() k seřazení prvků seznamu.
print(my_list)
my_list.sort()
print(my_list)


# ● Použijte metodu pop() k odstranění a vrácení posledního prvku seznamu.
removed_element = my_list.pop()
print(my_list)
print("Removed element: ", removed_element)
my_list.append(removed_element)
print(my_list)


# N-tice (Tuples):
# ● Vytvořte n-tici obsahující několik různých prvků.
tuple_1 = (2, 100, 1000, "Opel", "BMW", 2024, "Opel", 2024)


# ● Použijte metodu index() k zjištění indexu konkrétního prvku v n-tici.
print(tuple_1.index(1000))
print(tuple_1.index("BMW"))



# ● Použijte metodu count() k zjištění, kolikrát se konkrétní prvek v n-tici vyskytuje.
print(tuple_1.count("BMW"))
print(tuple_1.count(2024))


# Množiny (Sets):
# ● Vytvořte dvě množiny obsahující různé prvky.
set_1 = {1, 5,900, 30, 900}
set_2 = {"auto", "bicykel", "autobus", "auto"}


# ● Použijte metodu add() k přidání nového prvku do jedné z množin.
set_2.add(5)
print(set_2)


# ● Použijte metodu intersection() k nalezení prvků, které jsou společné pro obě množiny.
print(set_1.intersection(set_2))

# ● Použijte metodu union() k vytvoření sjednocení obou množin Řetězce (Strings):
set_result = set_1.union(set_2)
print(set_result)


# ● Vytvořte řetězec obsahující několik slov nebo vět.
string = "Hron Dunaj Váh Morava"
print(string)


# ● Použijte metodu split() k rozdělení řetězce na seznam slov.
set = string.split()
print(set)


# ● Použijte metodu upper() k převedení všech písmen v řetězci na velká.
string =string.upper()
print(string)

