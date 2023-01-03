import matplotlib.pyplot as plt
import numpy as np
ar2=[1, 7, 21, 35, 32, 21, 7, 1]
s=np.sin(ar2)
c=np.cos(ar2)
t=np.tan(ar2)
plt.title("my graph")
plt.figure(figsize=(15, 7))
plt.xlabel("sin cos tan")
plt.ylabel("numbers")
plt.plot(ar2, s, color='c', label='range')
plt.plot(ar2, c, color='r', label='range2')
plt.plot(ar2, t, color='k', linestyle="dashed", label='range3')
plt.legend(loc=2)
plt.show()
