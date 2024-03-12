x = [()]
print(x)
res = [False] * 2
print(res)
if x:
    res[0] = True
    print(x)
    print(res[0])
if x[0]:
    res[1] = True
print(x[0])
print(res[1])

x = 10
y = 20

if x > y:
    result = "x is greater than y"
elif x < y:
    result = "x is less than y"
else:
    result = "x is equall y"

print(result)


x = 20
y = 30
if x > y:
    result = "x is grater than y"
elif x < y:
    if x <10:
        result = "x is less than 10 and less or equall to y"
    elif x < 15:
        result = "x is less tahn 15 and less y"
    else:
        result = "x is less than y and greater or equall than 15"
else:
        result = "x is equall y"

print(result)


vek = float(input("Zadajte vek:"))
print(vek)

if vek <0:
    print("zadali ste zlú hodnotu.")
elif vek < 13:
    result = "dieťa"
elif vek < 20:
    result = "teenager"
elif vek < 64:
    result = "dospelý"
else:
    result = "senior"

print(result)

ultra_list = [f"Hey_{index}" for index in range(1000)]

print(ultra_list)
print(ultra_list[20:100])

my_set = {1, 4, 2, 3, 2, 3, 4, 4}
my_tuple = tuple(my_set)
back = set(my_tuple)
print(back)
print(my_set, my_tuple)



