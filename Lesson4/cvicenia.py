x = 5
y = 10

result = x == y
print(result)

result = x <= y
print(result)

x = "ahoj"
y = "ahoj"

result = x == y

print(result)

my_list = [1, 2, 3, "Hello", [4, 5]]
print(my_list)
print(my_list[4][0])
print(my_list[4][1])
print(my_list[4][-1])
print(my_list[4][-2])

#   použitie konštruktora
my_list = list([1, 2, 3, "Hello", [4, 5]])
print(my_list)

#Tuple
my_tuple = (1, 2, 3, "Hello", [4, 5])
my_tuple = tuple((1, 2, 3, "Hello", [4, 5]))

print(my_tuple)
print(my_tuple[4][1])
print(my_list)
my_list[0] = 9
print(my_list)

#   DATOVÝ TYP SET (MNOŽINA), nie je indexovaný!!!!
my_set={1, 2, 3, 2, 2}
# vyplačí len po 1 prvku za kždý výskyt
print(my_set)

print(list(my_set) + my_list)
#
ultra_list = [f"Hey_{index}" for index in range(1000)]

print(ultra_list)
print(ultra_list[20:100])



ultra_list = [f"Hey_{index}" for index in range(1000)]

print(ultra_list)
print(ultra_list[20:100])

my_set = {1, 2, 3, 3, 4, 4}
my_tuple = tuple(my_set)

print(my_set, my_tuple)
