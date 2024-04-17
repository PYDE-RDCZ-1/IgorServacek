# napisat 2 testy ba vypocet trojuholniku, kruhu test pre overenie
# korektnosti vypoctu pre rôzne vstupy

import pytest

def obsah_trojuholniku(a, b):
# výpočet povrchu pravouhlého trojuholníku v závislosti od veĺkosto oboch odvesien
    if a > 0 and b > 0:
        p = (a * b) / 2
        print(p)
        return p
    else:
        print(" nesprávne zadaná hodnota")
        return 0

def test_obsahu():
# testy na veľkosť povrchu
    assert obsah_trojuholniku(3, 3) == 4.5 , "obsah je nesprávny"
    assert obsah_trojuholniku(8, 8) == 32, "obsah je nesprávny"


def test_hodnoty():
    assert obsah_trojuholniku(3, 3) > 0 , "obsah je nesprávny"
    assert obsah_trojuholniku(0, 8) == 0, "obsah je nesprávny"

obsah = obsah_trojuholniku(3, 4)
print(obsah)
test_obsahu()
test_hodnoty()
