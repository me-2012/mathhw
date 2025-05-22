import math

pi = input('pi (to use the full pi, type "pi"): ')
if pi == "pi":
    pi = math.pi
else:
    pi = float(pi)

notfound = input("empty variable (c, d, r, a): ")

rounding = input("rounding (none for none, 1 for tenths, place -1 for tens place ect): ")
if rounding == 'none':
    roundingCheck = False
else:
    roundingCheck = True
    rounding = int(rounding)

if notfound == 'd': #diameter not found
    if input('area or circumference (type "a" or "c"): ') == 'a':
        a = float(input("a: "))
        if roundingCheck:
            print(round(2 * math.sqrt(a / pi), rounding))
        else:
            print(2 * math.sqrt(a / pi))
    else:
        c = float(input("c: "))
        if roundingCheck:
            print(round(c / pi, rounding))
        else:
            print(c / pi)
elif notfound == 'a': #area not found
    if input("d or r: ") == 'd':
        d = float(input("d: "))
        if roundingCheck:
            print(round((d / 2) ** 2 * pi, rounding))
        else:
            print((d / 2) ** 2 * pi)
    else:
        r = float(input("r: "))
        if roundingCheck:
            print(round(r ** 2 * pi, rounding))
        else:
            print(r ** 2 * pi)
elif notfound == 'c': #circumfrence not found
    if input("d or r: ") == 'd':
        d = float(input("d: "))
        if roundingCheck:
            print(round(d * pi, rounding))
        else:
            print(d * pi)
    else:
        r = float(input("r: "))
        if roundingCheck:
            print(round(2 * r * pi, rounding))
        else:
            print(2 * r * pi)
elif notfound == 'r': #radius not found
    if input("c or a: ") == 'c':
        c = float(input("c: "))
        if roundingCheck:
            print(round((c/pi)/2, rounding))
        else:
            print((c/pi)/2)
    else:
        a = float(input("a: "))
        if roundingCheck:
            print(round(math.sqrt(a / pi), rounding))
        else:
            print(math.sqrt(a / pi))
