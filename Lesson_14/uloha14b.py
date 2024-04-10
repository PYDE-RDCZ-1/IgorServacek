# napisat 2 testy ba vypocet trojuholniku, kruhu test pre overenie
# korektnosti vypoctu pre rôzne vstupy

import pytest

def povrch_trojuholniku(a, b):
# výpočet povrchu pravouhlého trojuholníku v závislosti od veĺkosto oboch odvesien
    p = (a * b) / 2
    print(p)
    return p


def test_obsahu():
# testy na veľkosť povrchu
    assert povrch_trojuholniku(3, 3) == 4.5 , "obsah je nesprávny"
    assert povrch_trojuholniku(8, 8) == 32, "obsah je nesprávny"


def test_hodnoty():
    assert povrch_trojuholniku(3, 3) > 0 , "obsah je nesprávny"


povrch = povrch_trojuholniku(3, 4)
print(povrch)
test_obsahu()
test_hodnoty()
