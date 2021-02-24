import numpy as np
# from scipy.interpolate import interp1d

from scipy.interpolate import interp1d

x = np.array([2,7,19])
print(x)
y = np.array([2,3,4])
f = interp1d(x, y)

xnew = np.linspace(2, 19, num=100)
print(xnew)
ynew=f(xnew)
print(x)
print(ynew)
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), 'o')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()