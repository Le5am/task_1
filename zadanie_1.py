import matplotlib.pyplot as plt
import math as mh
import numpy as np
import csv 
import os

#limits
x_min = -5
x_max = 5
dx = 0.01

#Creating a massive
x = np.arange(x_min , x_max + 1, dx)
y = -20*np.exp(-0.2*np.power(0.5*x*x, 0.5))-np.exp(0.5*(np.cos(2*mh.pi*x)+1))+mh.e+20

#counting the number of the points
num_max = int(((abs(x_max)+abs(x_min))/dx)+1)
num = np.arange(1, num_max + 1)

#points in massive
n = 0
out = []
while n < num_max:
  out.append((num[n], x[n], y[n]))
  n += 1

#out += [[num[n]] + [x[n]] + [y[n]]]

#about file
if not os.path.isdir("results"):
    os.mkdir("results")
    
with open("./results/data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(
      out
    )    

#graphic
plt.plot(x,y)   
plt.title("Line graph")   
plt.ylabel('Y axis')

plt.xlabel('X axis')
plt.xlim(x_min, x_max)

plt.show()

#conclusion
print(np.array(out))
print("\nProgramm has done its work")