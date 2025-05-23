points = []

def rotate(points, rotateAmt):
    newPoints = []
    for i in points:
        if amt==1:
            x, y = i
            newPoints.append((-y, x))
        elif amt==2:
            x, y = i
            newPoints.append((-x, -y))
        elif amt==3:
            x, y = i
            newPoints.append((y, -x))
    return newPoints

nums = int(input("Enter the amount of points in the shape: "))
for i in range(nums):
    inp = input(f"point #{i+1}: ")
    points.append((int(inp.split(', ')[0]), int(inp.split()[1])))

amt = int(input("1 = 90, 2 = 180, 3=270, all ccw: "))

print(rotate(points, amt))
