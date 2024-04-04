# Cvicenie 8
# Cykly
fruits = ["apple", "banana", "cherry", "annanas"]
for fruit in fruits:
    print(fruit)
print(fruits)

i = 1
while i <= 6:
    print(i, end=", ")
    print()
    i += 1
print(i)


i = 1
for i in range (1, 7):
    print(i, end=", ")
    i += 1
print(",,,,,,,,")

for fruit in fruits:
    print(fruit, "   ", len(fruit))



ovocie = ["jablko", "hruška", "banan", "kiwi"]
ceny =  [10, 16, 8, 2]
slovnik = []

for i in range (len(ovocie)):
    a = ovocie[i]
    b = ceny[i]
    print(a, b)
    pom = (a, b)
    slovnik.append(pom)

print(dict(slovnik))

pocet = len(ovocie)

#   PR 5
#   Spočítanie slov v reťazci

slovnik = {}
# string = "Dobre je dnes je pekne dnes zajtra bude slovo je slovo"
string = input("Zadajte reťazec s opakovaním slov: ")
dlzka = len(string)
words = string.split()
print(words)
for item in words:
#   odstranenie neziaducich znakov a eliminovanie velkych pismen
    item = item.strip(",.!?").lower()
    if slovnik.get(item):
        word_count = slovnik.get(item)
        slovnik [item] = word_count + 1
        print(item, slovnik[item])
    else:
        slovnik[item] = 1
        print(item, slovnik[item])
print(slovnik)

# sortovanie podľa kľúčov
sorted_slovnik = dict(sorted(slovnik.items()))
print(sorted_slovnik)

# soertovanie podľa hodnôt
sorted_slovnik = dict(sorted(slovnik.items(), key=lambda item: item[1], reverse=True))
print(sorted_slovnik)


#    zoznam[i] = print(i)

#   for i in range (dlzka-1):
#   print(words[i])

#   for word in words:
#    word = word.strip(",.!?").lower()
#    if word in word_count


#   PR 6
#   faktorial
vysledok = 1
cislo= int(input("zadajte cislo"))
print(cislo)
sum = 1
while cislo > 0:
    sum = sum * cislo
    cislo -=1
print("Faktoriál čísla ", cislo, " je ",sum)

heslo_vzor = "Test123"
heslo = input("zadaj heslo: ")

while heslo != heslo_vzor:
    print("incorrect pswd.")
    heslo = input("zadaj heslo: ")
print("access granted")



