#   *** Úloha č.4

#   Úkol: Vytvořte dva nákupní seznamy (list nebo tuple), jeden s potravinami a druhý s drogerií.
#   Do jednoho z nich vložte duplicitní položku a pak tento seznam převeďte na datový typ set.
#   Nakonec přehledně vypište oba seznamy najednou pomocí jediné funkce print.



nakupny_zoznam_potraviny = ["maslo", "hladká múka", "minerálka", "soľ", "pečivo"]
nakupny_zoznam_drogeria = ["mydlo", "zubná pasta", "mydlo", "zubná pasta", "soda bikarbona", "mydlo"]


print("Nakupny zoznam potraviny: ", nakupny_zoznam_potraviny)
print("Nakupny zoznam drogeria: ", nakupny_zoznam_drogeria)
nakupny_zoznam_drogeria_set = set(nakupny_zoznam_drogeria)
print("Nakupny zoznam drogeria, prevedeny na set: ", nakupny_zoznam_drogeria_set)

finalny_zoznam =nakupny_zoznam_potraviny + list(nakupny_zoznam_drogeria_set)
print("Obidva zoznamy v jednom riadku: ")

print(finalny_zoznam)
