from math import e

import numpy as np
import matplotlib.pyplot as plt
from num_methods import euler, improved_euler, runge_kutta


plt.figure()  # Problem 1

f = lambda t, y: 1-(20*y)

x1, y1 = euler(f, 0, 0, 0.1, 20)
x2, y2 = improved_euler(f, 0, 0, 0.1, 20)
x3, y3 = runge_kutta(f, 0, 0, 0.1, 20)

plt.plot(x1, y1, color='green', linestyle='-.', label='Euler')
plt.plot(x2, y2, color='red', linestyle='-', label='Improved Euler')
plt.plot(x3, y3, color='blue', linestyle=':', label='Runge Kutta')

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('y` = 1−20y')

plt.savefig("Problem1.png")

plt.figure()  # Problem 2 #3


g = lambda t, y: t*(e**t) - (2/t)*y

x4, y4 = euler(g, 1, 0, 0.1, 30)
x5, y5 = improved_euler(g, 1, 0, 0.1, 30)
x6, y6 = runge_kutta(g, 1, 0, 0.1, 30)

x7, y7 = euler(g, 1, 0, 0.05, 60)
x8, y8 = improved_euler(g, 1, 0, 0.05, 60)
x9, y9 = runge_kutta(g, 1, 0, 0.05, 60)

plt.plot(x4, y4, color='blue', linestyle='-.', label='Euler')
plt.plot(x5, y5, color='red', linestyle='-', label='Improved Euler')
plt.plot(x6, y6, color='green', linestyle=':', label='Runge Kutta')

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('y` = te^t - (2/t)y Step Size 0.1')

plt.savefig("Problem23.png")


plt.figure()  # Problem 2 #4

plt.plot(x7, y7, color='blue', linestyle='-.', label='Euler')
plt.plot(x8, y8, color='red', linestyle='-', label='Improved Euler')
plt.plot(x9, y9, color='green', linestyle=':', label='Runge Kutta')

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title('y` = te^t - (2/t)y Step Size 0.05')

plt.savefig("Problem24.png")


plt.figure()  # Problem 3

h = lambda t, y: (3*(t**2))/(3*(y**2)-4)

x10, y10 = runge_kutta(h, 0, 0, 0.1, int( 100*1.5))
x11, y11 = runge_kutta(h, 0, 0, 0.05, int(200*1.5))
x12, y12 = runge_kutta(h, 0, 0, 0.01, int(1000*1.5))

plt.plot(x10, y10, color='blue', linestyle='--', label='Step Size 0.1')
plt.plot(x11, y11, color='red', linestyle=':', label='Step Size 0.05')
plt.plot(x12, y12, color='green', linestyle='-.', label='Step Size 0.01')

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title("y` = (3t^2)/(3y^2 - 4) Runge Kutta")

plt.savefig("Problem3.png")


plt.figure()

p = lambda t: -t*(e**t)
p1 = lambda t: t-((t**2)/2)
p2 = lambda t: t-(t**2)-((t**3)/6)
p3 = lambda t: t-(t**2)-((t**3)/3)-((t**4)/24)
p4 = lambda t: t-(t**2)-((t**3)/3)-((t**4)/12)-((t**5)/120)
p5 = lambda t: t-(t**2)-((t**3)/3)-((t**4)/12)-((t**5)/60)-((t**6)/720)

x = [j/100 for j in [i for i in range(0, 201)]]

pic = [p(i) for i in x]
pic1 = [p1(i) for i in x]
pic2 = [p2(i) for i in x]
pic3 = [p3(i) for i in x]
pic4 = [p4(i) for i in x]
pic5 = [p5(i) for i in x]

plt.plot(x, pic, color='red', linestyle='-', label='Calculated', marker='D',
         markevery=[i == 1 for i in x])
plt.plot(x, pic1, color='purple', linestyle='-.', label='Pic1', marker='o',
         markevery=[i == 1 for i in x])
plt.plot(x, pic2, color='green', linestyle='--', label='Pic2', marker='o',
         markevery=[i == 1 for i in x])
plt.plot(x, pic3, color='red', linestyle=':', label='Pic3', marker='o',
         markevery=[i == 1 for i in x])
plt.plot(x, pic4, color='yellow', linestyle='-.', label='Pic4', marker='o',
         markevery=[i == 1 for i in x])
plt.plot(x, pic5, color='blue', linestyle=':', label='Pic5', marker='D',
         markevery=[i == 1 for i in x])

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title("y` = 1-t-y Picard Iterations")

plt.savefig('Problem42.png')


plt.figure()  # Problem 4

i = lambda t, y: 1-t-y

x13, y13 = euler(i, 0, 0, 0.05, 40)
x14, y14 = improved_euler(i, 0, 0, 0.05, 40)
x15, y15 = runge_kutta(i, 0, 0, 0.05, 40)

x16, y16 = euler(i, 0, 0, 0.01, 200)
x17, y17 = improved_euler(i, 0, 0, 0.01, 200)
x18, y18 = runge_kutta(i, 0, 0, 0.01, 200)

plt.plot(x13, y13, color='blue', linestyle='-.', label='Euler', marker='o',
         markevery=[i == 1 for i in x13])
plt.plot(x14, y14, color='red', linestyle='-', label='Improved Euler', marker='D',
         markevery=[i == 1 for i in x14])
plt.plot(x15, y15, color='green', linestyle=':', label='Runge Kutta', marker='o',
         markevery=[i == 1 for i in x15])

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title("y` = 1-t-y Step Size 0.05")

plt.savefig('Problem43.png')


plt.figure()  # Problem 4..

plt.plot(x16, y16, color='blue', linestyle='-.', label='Euler', marker='o',
         markevery=[i == 1 for i in x16])
plt.plot(x17, y17, color='red', linestyle='-', label='Improved Euler', marker='D',
         markevery=[i == 1 for i in x17])
plt.plot(x18, y18, color='green', linestyle=':', label='Runge Kutta', marker='o',
         markevery=[i == 1 for i in x18])

plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.title("y` = 1-t-y Step Size 0.01")

plt.savefig("Problem44.png")


#plt.show()

'''


plt.figure()
m = lambda t: -(e**(-20*t) -1)/20
x = [j/100 for j in [i for i in range(0, 201)]]
y = [m(i) for i in x]

plt.plot(x, y, color='blue', linestyle=':', label='P1')

plt.savefig("misc.png")

# importing the required modules 
import matplotlib.pyplot as plt 
import numpy as np 
  
# setting the x - coordinates 
x = np.arange(0, 2, 0.01) 
# setting the corresponding y - coordinates 
y = np.sin(x)
  
# potting the points 
plt.plot(x, y) 
  
# function to show the plot 
plt.show() 
'''