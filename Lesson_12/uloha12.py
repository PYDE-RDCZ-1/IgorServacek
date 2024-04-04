""" Lekce 12:
Spočítejte celkovou hodnotu položek v nákupním seznamu s jejich odpovídajícími množstvími.
Vytvořte seznam obsahující tuples, kde každý tuple představuje položku a její množství. Každý tuple by měl obsahovat dvě položky: název položky (string) a její množství (integer).
Definujte slovník pojmenovaný prices, kde klíče jsou názvy položek a hodnoty jsou jejich odpovídající ceny za jednotku.
Použijte enumerate() k iteraci přes seznam tuples.
Pro každý tuple spočítejte celkovou cenu položek (cena za jednotku * množství) a sečtěte je.
Celkovou cenu uložte do proměnné s názvem total_price.
"""

# Verzia 1 bez enumerate
print("Program bez enumerate")
zoznam = [("kofola", 2), ("maslo", 5), ("chlieb", 1), ("mineralka", 6)]
prices = {"kofola": 1.30, "maslo": 2.60, "chlieb": 2.10, "mineralka": 0.5}
total_price = 0
for name, price in zoznam:
    total_price = total_price + price * prices.get(name, 0)
    print(f"Jednotkova cena pre {name} je: {prices[name]} EUR pre mnozstvo :  {prices.get(name, 0)} ks. Cena spolu je {price * prices.get(name, 0)}")
print(f"Celková suma za nákup je: {total_price}")


# Verzia 2 s enumerate
print("Program s použitím enumerate I")
total_price = 0
for index, (polozka, price) in enumerate(zoznam):
    total_price += price * prices.get(polozka, 0)
    print(f"Jednotkova cena pre {polozka} je: {price} EUR pre mnozstvo :  {prices.get(polozka, 0)} ks. Cena spolu je {price * prices.get(polozka, 0)}")
print(f"Celková suma za nákup je: {total_price}")


# Verzia 3 s enumerate
print("Program s použitím enumerate II")
total_price = 0
for index, (polozka, mnozstvo) in enumerate(zoznam):
    if polozka in prices:
        total_price += prices[polozka] * mnozstvo
# kontrolná tlač po každom výpočte
        print(f"Jednotkova cena pre {polozka} je: {prices[polozka]} EUR pre mnozstvo :  {mnozstvo} ks. Cena spolu je {prices[polozka] * mnozstvo}")
print("Total price:", total_price)