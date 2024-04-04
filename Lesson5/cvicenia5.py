from typing import List, Union

my_string = "Hello World!"
print(my_string.upper())
print(my_string.lower())
# metódu voláme na premenej. metóda pracuje s daným objektom a umožňuje pracovať s jeho datami
# rozdiel medzi metódou a funkciou

#rozdelenie reťazca na zoznam podreťazcov
print(my_string.split())

print(my_string.find("H"))
print(my_string.find("l"))
print(my_string.count("l"))
print(my_string.count(" "))
print(my_string.split()[0])
print(my_string.split()[1])

print(my_string.lstrip("Hello "))
print(my_string)

my_list = my_string.split(" ")
print(my_list)

my_list = ["káva", "čaj", 5, "mlieko", 5,"voda", 5, "one"]
print("my_list = ", my_list)


pocet_prvkov = len(my_list)
pocet_vyskytov_5 = my_list.count(5)

print(pocet_vyskytov_5)
for i in range (0, pocet_vyskytov_5, 1):
    smerovnik = my_list.index(5)
    print(i, "   ", smerovnik)
    my_list.pop(smerovnik)
    print(my_list)
print("my_list po odstraneni prvku 5 :", my_list)




new_string = my_string.replace("Hello", "Jano")
print(new_string)


print(my_string)
my_second_list = [7, 8, 9, 1, 2]
my_second_list.sort()
print(my_second_list)

my_list = my_string.split()
print(my_list)

#   metody pre tuple (immutable)
my_tuple = (1, 5, 6, 88, 90, 88, 1005, 88, "a", "b", "c")
print("Tuple")
print("dĺžka my_Tuple: ", len(my_tuple), " prvkov.")
print(my_tuple.count(88))
print(my_tuple.index(88))
print(my_tuple.index(88))




set1 = {1, 2, 3, 4, 7, 8, 9, 8}
set2 = {1, 4, 5}
intesection_set = set1.symmetric_difference(set2)

print(intesection_set)

print(min(set1))
print(max(set1))
sum = sum(set1)
print(sum)

p = 0
print([p, 3])

x = [15,10,2,84] + [1,4,8,7,9]
print(x)
print(x.index(x.count(x[0])))

import numpy as np

np.array([True, 1, 2]) + np.array([3, 4, False])
