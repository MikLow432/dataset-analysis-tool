print("hi from main")

from importlib import resources
import my_python_package as mpp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




path = resources.files("my_python_package").joinpath("Income.csv")
df = pd.read_csv(path)

print(df.head())

mpp.summary(df)
mpp.histogram(df)
mpp.scatter(df)



plt.show()
