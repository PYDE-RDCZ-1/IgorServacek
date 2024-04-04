# výpočet obsahu kruhu
# Autor: Igor Serváček

import math
print("*** Program pre výpočet obvodu a obsahu kruhu, jednotky v cm. ***")
pi = 3.14
polomer = input("zadajte polomer kruhu: ")
obvod = 2 * pi * int(polomer)
obsah = pi * int(polomer) ** 2
print("obvod kruhu je: ", obvod)
print("obsah kruhu je: ", obsah)


print("*** Program pre ýpočet obsahu trojuholníka podľa Heronovej vety, jednotky v cm ***")
a = int(input("Zadajte stranu a: "))
b = int(input("Zadajte stranu a: "))
c = int(input("Zadajte stranu a: "))
s = (a + b + c)/2
obsah_trojuholnika = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Obsah trojuholníka je: ", obsah_trojuholnika)

