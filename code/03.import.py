from numpy import *
from matplotlib.pyplot import *

x = linspace(0, 2*pi, 100)
y = sin(x)
plot(x,y); 

grid(); title("sine curve")
xlabel("x"); ylabel("sin(x)")
show()

