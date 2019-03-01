import numpy
import matplotlib.pyplot as plt

#Inisialisasi nilai
n = 21
t = 5
v = 1
g = 9.8

dt = t/(n-1)

#Inisialisasi nilai y1 & y2
t1 = [float(i) for i in range(n)]
y = []
y.append(100)
y.append(y[0])
y.append(y[1] + dt*v)

#Menghitung dengan rumus gerak jatuh bebas
for i in range(3,21):
    y.append((2*y[i-1]) - (y[i-2]) - (g*(dt**2)))

print(y)
plt.plot(t1,y,'o')
plt.show()