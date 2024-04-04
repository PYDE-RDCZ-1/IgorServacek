#   Cvicenie 11
#   print(default)
#   print(class)

# BMI kalkulkulátor
import numpy
def bmi(weight, height):
    vysledok = float(weight / ((height/100)**2))
    if vysledok < 18.5:
        print("Máte podváhu.")
    elif vysledok <25:
        print("Vaša váha je v norme.")
    else:
        print("Trpíte nadváhou.")
    return(vysledok)

#   Telo programu
a = int(input("zadaj výšku v cm: "))
b = int(input("zadaj váhu v kg: "))
print(bmi(b, a))



