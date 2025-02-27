ogx = int(input("enter the original x: "))
ogy = int(input("enter the original y: "))

right = int(input("enter how much right (if its left, then negative): "))
up = int(input("enter how much up (if its down, then negative): "))

x = ogx + right
y = ogy + up

print(f"({x}, {y})")