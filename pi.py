import math

pi = input('pi (to use the full pi, type "pi"): ')
if pi == "pi":
    pi = math.pi
else:
    pi = float(pi)

notfound = input("empty variable (c, d, r, a): ")

if notfound == 'd': #diameter not found
    if input('area or circumference (type "a" or "c"): ') == 'a':
        a = float(input("a: "))
        print(2 * math.sqrt(a / pi))
    else:
        c = float(input("c: "))
        print(c / pi)
elif notfound == 'a': #area not found
    if input("d or r: ") == 'd':
        d = float(input("d: "))
        print((d / 2) ** 2 * pi)
    else:
        r = float(input("r: "))
        print(r ** 2 * pi)
elif notfound == 'c': #circumfrence not found
    if input("d or r: ") == 'd':
        d = float(input("d: "))
        print(d * pi)
    else:
        r = float(input("r: "))
        print(2 * r * pi)
elif notfound == 'r': #radius not found
    if input("c or a: ") == 'c':
        c = float(input("c: "))
        print((c/pi)/2)
    else:
        a = float(input("a: "))
        print(math.sqrt(a / pi))