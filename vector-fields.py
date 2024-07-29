#!usr/bin/python3

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import assoc_legendre
from sympy import cos,sin,Abs,factorial
from sympy import sqrt
from sympy import latex
from sympy import trigsimp
from sympy import Derivative
import matplotlib.cm as cm

print('vector field plots')
#def plot(self,func):
x=np.linspace(0,1,20)  #x poinst between 0 nand 1, sample data is 20 points.
y=np.linspace(0,1,20)   # y points
z=np.linspace(0,1,20)
x,y=np.meshgrid(x,y) # 2D plot in a mesh


f=np.sin(x)*np.cos(y)   #function assigned to the grid
plt.contourf(x,y,f, 20, cmap=cm.Reds_r) # Contour plot
plt.title('Contour plot of scalar function f')
plt.show()

[gf1,gf2]=np.gradient(f)  #calcultaes the gradients of the function f, grad_f
plt.quiver(x,y, gf1, gf2, color = ['r'],angles='xy', scale_units='xy', scale=0.9)
plt.title('Vector field of gradient of f')
plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

x=np.arange(-0.8,1,0.2)
y=np.arange(-0.8,1,0.2)
z=np.arange(-0.8,1,0.2)
x,y,z=np.meshgrid(x,y,z)

u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
ax.set_xlim([-1,1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.quiver(x,y,z,u,v,w,length=0.1)

plt.show()


 



 
