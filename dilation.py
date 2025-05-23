points = []

def dilate(points, sf):
    newPoints = []
    for i in points:
        x, y = i
        newPoints.append((x*sf, y*sf))
    return newPoints

nums = int(input("Enter the amount of points in the shape: "))
for i in range(nums):
    inp = input(f"point #{i+1}: ")
    points.append((int(inp.split(', ')[0]), int(inp.split()[1])))

sf = int(input("scale factor: "))

print(dilate(points, sf))