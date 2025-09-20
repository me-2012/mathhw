import matplotlib.pyplot as plt

c90 = False
cc90 = False
any180 = False

degreesRotated = input()
if degreesRotated == '1':
    c90 = True
elif degreesRotated == '2':
    cc90 = True
elif degreesRotated == '3':
    any180 = True

preX = list(map(int, input('x: ').split(', ')))
preX.append(preX[0])
preY = list(map(int, input('y: ').split(', ')))
preY.append(preY[0])

x = []
y = []

'''
1 = 270 cc or 90 c
2 = 90 cc or 270 c
3 = 180
'''

if c90:
    for i in range(len(preX)):
        x.append(preY[i])
        y.append(-preX[i])
elif cc90:
    for i in range(len(preX)):
        x.append(-preY[i])
        y.append(preX[i])
elif any180:
    for i in range(len(preX)):
        x.append(-preX[i])
        y.append(-preY[i])

# plotting the points 
plt.plot(preX, preY, color = ("blue"))
plt.plot(x, y, color = ("red"))

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('rotation (with a graph!!!)')

# function to show the plot
plt.show()