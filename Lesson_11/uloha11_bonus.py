# vytvorenie abcedy a - z
# vytvarame dictionary key value - hodnota
# na jeho zaklade napisat text, zasifrovat a potom ho prelozit do zrozumitelneho jazyka
# cesarova šifra, alebo substitučná šifra
abeceda = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZ ."
def koduj(posun, retazec):
    kodovany_text = ""
    for char in retazec:
        index = abeceda.index(char)
        new_index = index + posun
        new_index = new_index % 54
        kodovany_text += abeceda[new_index]
    return kodovany_text

def dekoduj(posun, retazec):
    dekodovany_text = ""
    for char in retazec:
        index = abeceda.index(char)
        old_index = index - posun
        old_index = old_index % 54
        dekodovany_text += abeceda[old_index]
    return dekodovany_text


# text = "toto je tajna sprava urcena na zasifrovanie."
text = input("Zadajte text pre zakódovanie (aoužívajte len znaky a - Z, medzeru a bodku: ")
posun_znaku = int(input("Zadaj cislo pre posun mriezky: "))

# posun_znaku = 10
print(koduj(posun_znaku, text))
zakodovany_text = koduj(posun_znaku, text)

print(dekoduj(posun_znaku, zakodovany_text))
print("originálny text: ", text)
print("zakódovaný text: ", koduj(posun_znaku, text))
print("Znovu odkodovana sprava: ", dekoduj(posun_znaku,zakodovany_text))
