import matplotlib.pyplot as plt
import numpy as np
import math
m = 0.04593
g = 9.81
v_0 = 50
angle = math.pi / 4
vy_0 = 50* math.sin(angle)
vx_0 = 50 * math.sin(angle)
x_0 = 0
y_0 = 0
ro = 1.2
A = 0.427
c_D = 0.3
# F_D = 0.5 * ro * v * v * c_D * A
# F_G = m*g

time = np.linspace(0,2*vy_0/g,100)
y = -0.5*time*time*g + vy_0*time + y_0
x = vx_0 * time + x_0
v = -1 *time*g
x_with_F_D = -0.5*time*time*g + v_0*time + x_0 - 0.5 * ro * v * v * c_D * A


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'r')

plt.show()


