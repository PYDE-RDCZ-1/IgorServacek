import pytest

def add(a, b):
    return (a + b)


def subtr (a, b):
    return a - b


def div (a, b):
    return a / b

def test_add():
    assert add(2,3)  == 5
    assert add(5, 5) == 10
def test_subtr():
    assert subtr(8, 4) == 4

def test_div():
    assert div(12, 4) == 3, vysledok nedopadol dobre



test_div()
