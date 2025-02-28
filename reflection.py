ogx = int(input("enter the original x: "))
ogy = int(input("enter the original y: "))
x = 0
y = 0

axis = input("enter what axis you are reflecting by (x or y): ")
if axis == "x":
    x = ogx
    y = -ogy
else:
    x = -ogx
    y = ogy


print(f"({x}, {y})")