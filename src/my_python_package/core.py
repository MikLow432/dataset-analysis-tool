print("hi from core")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import my_python_package as mpp
import csv

def load_data(path):
    with open('Income.csv', mode='r', encoding='utf-8') as file:
      reader = csv.DictReader(file)
    return reader


def summary(df):
    return df.describe()

def correlation(df):
    return df.corr(numeric_only=True)

def histogram(df, column):
    df[column].hist()
    plt.title(f"Histogram of {column}")
    plt.show()

def scatter(df, x, y):
    df.plot.scatter(x=x, y=y)
    plt.show()

