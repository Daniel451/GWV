import matplotlib.pyplot as plt
import numpy as np

__author__ = 'daniel'

with open("blatt3_environment.txt") as f:
    fdata = f.read()


my_data = np.arange(0, 9).reshape(3, 3)

plt.imshow(my_data, interpolation="none")
plt.show()