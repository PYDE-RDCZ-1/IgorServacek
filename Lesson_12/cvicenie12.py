from typing import Tuple, Callable, Any

name = ("Alice")
b = 20
print(f"name: {name}, b = {b}")

#list comprehension
print("List comprehension")
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

squared_numbers = [x**2 for x in range (1,17)]
print(squared_numbers)

numbers_with_sum = [x * (x-1) for x in range (1,20) ]
print(numbers_with_sum)
numb_sum = [1]
x = [1, 2]
pom_sum = [x.append(x[i-1] * x[i]) for i in range (1,10)]
x.pop(0)
x.pop(0)
print(x)



#tuple

#dictionary

words = ["apple", "banana", "grape", "orange", "kiwi", "pineapple", "strawberry", "melon"]
print(words)
new_words = [word for word in words if len(word) > 5]
print(new_words)

word_length_dictionary = {word: len(word) for word in words }
print(word_length_dictionary)

my_list = ["a", "b", "c"]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Hodnota: {value}")

new_words = {index: word for index, word in enumerate(words)}
print(f"Index: {index}, Hodnota: {value}")

slovnik = {index: word for index, word in enumerate(words)}
print(slovnik)


iterator = iter([1, 2, 3])
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("enumerate ********  next")
enum_iterator = enumerate(my_list)
first_item = next(enum_iterator)
print(first_item)
second_item = next(enum_iterator)
thitth_item = next(enum_iterator)
print(second_item)
print(thitth_item)

print("zip  ********")
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
names =["Peter", "Jano", "Duro"]

combined = list(zip(numbers, letters, names))
print(combined)

# Lambda funkcia, bezmenná funkcia
addition = lambda a, b: a + b

result = addition(3,4)
print(result)

timestwo = lambda a: a * 2
result = timestwo(3)
print(result)


#   map(function, iterable)

new_numbers = map(lambda x: x * 2, numbers)
new_numbers_1 = map(timestwo, numbers)

print(list(new_numbers))
print(list(new_numbers_1))

# filter()
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

even_numbers = filter(lambda x: x % 2 == 0, range(20))
print(list(even_numbers))

#Príklad
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 16},
    {"name": "Eve", "age": 20}
]

print(list(people))
people_under_20 = list(map(lambda x: x["name"], filter(lambda x: x["age"] < 20, people)))
people_over_25 =list(map(lambda x: x["name"], filter(lambda x: x["age"]> 25, people)))
print(list(people_under_20))
print(list(people_over_25))



def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5, 6,7, 8, 9]
result = map(double, numbers)
print(list(result))

result = map(lambda x: x * 2, numbers)
print(list(result))

# párne čísla z numbers
print("párne čísla")
print(list(filter(lambda x: x % 2 == 0, numbers)))

import math
# nepárne čísla
print("nepárne čísla")
print(list(filter(lambda x: x % 2 != 0, numbers)))

prepona = lambda u, v: float  (u**2 + v**2) ** 0.5
aaa = prepona(3,4)
print(aaa)

