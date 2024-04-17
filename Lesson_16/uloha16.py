# Napiš funkci pro vytvoření Pascalova trojúhelníku za pomoci knihovny NumPy.
import numpy as np


def create_pt(matica, rozmer):
    for i in range(0, rozmer+1):
        for j in range(0, i+1):
            if j == 0 or i == j:
                matica[i, j] = 1
            else:
                matica[i, j] = matica[i-1, j-1] + matica[i-1, j]
    print("Kontrolná tlač vygenerovanej matice:")
    print(matica)
    print(" ")
    return matica


def vytlac_pt(matica, rozmer):
    for a in range(0, rozmer+1):
        print(f"riadok {a} :   ", end="")
        for b in range(0, a+1):
            print(matica[a, b], end=" ")
        print("\n")
    return


def create_pt_np(rozmer):
    trojuholnik = np.zeros((rozmer+1, rozmer+1), dtype=int)
    trojuholnik[:, 0] = 1
    for i in range(1, rozmer+1):
        for j in range(1, i + 1):
            trojuholnik[i, j] = trojuholnik[i-1, j-1] + trojuholnik[i-1, j]
    return trojuholnik


dimenzia = int(input("Zadajte rozmer Pascalovho trojuholníku: "))
print("Počet riadkov Pascalovho trojuholníka je: ", dimenzia)

# standard versian
pt = {}
pt = create_pt(pt, dimenzia)
print("Tlač Pascalovho trojuholníka, vytvoreného klasickou metódou.")
vytlac_pt(pt, dimenzia)

# využitie knižnice numpy
pt = create_pt_np(dimenzia)
print("Tlač toho istého Pascalovho trojuholníka, vytvoreného pomocou knižnice numpy.")
vytlac_pt(pt, dimenzia)
