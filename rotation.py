points = []
nums = int(input("Enter the amount of points in the shape: "))
for i in range(nums):
    inp = input(f"point #{i+1}: ")
    points.append((int(inp.split(', ')[0]), int(inp.split()[1])))
print(points)
