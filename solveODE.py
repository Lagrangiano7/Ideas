# I want to solve the first order Cauchy problem:


"""
dx/dt = f(x, t)
x(t0)=x0

"""

# Approach (admitting x analytic on t): if we knew all the coefficients of the Taylor series of x(t) we would be able to
# reconstruct the whole function for all of its domain. Nonetheless, we can truncate the series to get an approximate
# solution around some point (for instance, t=0). We can figure out all the Taylor coefficients of the solution
# using the ODE

from sympy import *
from math import factorial
import numpy as np
import matplotlib.pyplot as plt

n = 6 # Truncate at 6 (included)

x = Symbol("x")
t = Symbol("t")

f1 = -x+cos(t)
f = -x+cos(t)
func = lambdify((x, t), f, "math")

t0=0
x0=1

coefs = [x0, func(x0, t0)] # x0, x1

for i in range(2, n+1):
    f = diff(f, x)*f1+diff(f, t)
    func = lambdify((x, t), f, "math")
    coefs.append(func(x0, t0)/factorial(i))

print(coefs)

############ RESUELVO Y COMPARO ############

f = lambda x, t: -x+np.cos(t)

tp = np.linspace(0,3,1000)
h = 3/1000
x=1
xp=[]

for t in tp:
    xp.append(x)
    k1 = h*f(x, t)
    k2 = h*f(x+k1/2, t+h/2)
    k3 = h*f(x+k2/2, t+h/2)
    k4 = h*f(x+k3, t+h)

    x+=1/6*(k1+2*k2+2*k3+k4)

plt.plot(tp, xp, "r", label="RK4")
plt.plot(tp, np.polyval(coefs[::-1], tp), label="Polynomial (n=6)")
plt.legend()
plt.show()