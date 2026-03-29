print("hi from main")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import my_python_package as mpp

import os

from importlib import resources


print(mpp.add(1,2))
print(mpp.add(10,100))

plt.figure()
plt.plot([1,2,3],[4,5,6])
"""plt.show()"""

print(np.array((1,2,3,4)))
print(np.random.standard_normal(10))



path = resources.files("my_python_package").joinpath("Income.csv")
df = pd.read_csv(path)
print(df.head())

