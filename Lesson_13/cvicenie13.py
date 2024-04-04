# exceptions - výnimky
"""
try:
if x=5:
    print(">5")
except

# type error
result = "Hello " + 42
tuple (1, 2, 3,)
tuple [0] = 10

# name errror

print(bata)

# value error
number = int("abc!")
"""
# zero division error
try:
    a = 10 / 0
except ZeroDivisionError:
    print("chyba: delenie nulou")
else:
    print("nevyskytla sa chyba")
finally:
# tento blok sa obvykle používa k čisteniu
    print("Tento blok sa vykoná vždy")


# cvicenie, program pre zadanie veku, ak nie je platne cislo, spracuje vynimku a vyzve uzivatela, aby zadal
def vek():
    cyklus = True
    while cyklus:
        try:
            a = int(input("zadaj Tvoj vek, celé, Číslo:"))
        except ValueError:
            print("zadali ste chybné číslo")
        else:
            print("zadali ste správne číslo: ", a)
            cyklus = False
    return a


def main():
    b = vek()
    print(vek)


