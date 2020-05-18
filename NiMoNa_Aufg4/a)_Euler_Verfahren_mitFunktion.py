import numpy as np
import matplotlib.pyplot as plt

x=0
y=1
T=20*np.pi
h=0.05
omega=1
m=int(T/h)
xs=[x]
ys=[y]
ts=np.arange(0, T, h)

plt.plot(ts[0], xs[-1], ',') 

def f_1(x_old, omega):
    return -omega**2*x_old

def f_2(y_old, paramater):
    return y_old

# Function Parameter ist hier irrelevant, weil f_2 nicht von ihnen abh.
    

def euler(rhs, x_old, y_old, function_parameters , stepsize):
 x_new = x_old + stepsize*rhs(y_old, *function_parameters) 
 return x_new



for t in ts[1:]:
    x=euler(f_2, x, y, [omega], h)
    xs+= [x] 
    
    y=euler(f_1, y, x, [omega], h)
    ys+= [y]
   
    plt.plot(t, xs[-1], ",b")
    # Wie kann ich Listen Elemente verbinden im Plot, sodass eine durchgezogene Linie ensteht?

