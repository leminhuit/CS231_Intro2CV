import random
import matplotlib.pyplot as plt
import numpy as np

# Generating a Dataset to test
pointArr = []
n = int(input("Enter n : "))
for i in range(0, n):
    if (i > 0.7 * n):
        pointArr.append([random.randint(1,n), random.randint(1,n)])
    else:
        pointArr.append([i, 3 * i + 7])

# Plotting the points using matplotlib
x, y = zip(*pointArr)

plt.scatter(*zip(*pointArr))
plt.show()

# Choosing 2 random points in pointArr and find the equation of them
for i in range(3):
    belong = 0
    A, B = random.choices(pointArr, k = 2)

    # print(A, B)

    a = B[1] - A[1]
    b = A[0] - B[0]
    c = a * (A[0]) + b * (A[1])

    # print(a, b, c)

    if (b < 0):
        for i in range(len(pointArr)):
            if (c == a * pointArr[i][0] - b * pointArr[i][1]):
                belong += 1
    else:
        for i in range(len(pointArr)):
            if (c == a * pointArr[i][0] + b * pointArr[i][1]):
                belong += 1

    if (belong/n == 0.7):
        print(a,b,c)

# Plotting the result of the found line equation
formulaX = np.linspace(0,n,100)
if (b < 0):
    formulaY = (c - a * formulaX) / (-b)
else:
    formulaY = (c - a * formulaX) / (b)

plt.plot(formulaX, formulaY, '-r')
plt.title('Graph of the found line that satisfy the condition' + str(a) + 'x + ' + str(b) + 'y =' + str(c))
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.scatter(*zip(*pointArr))
plt.grid()
plt.show()
