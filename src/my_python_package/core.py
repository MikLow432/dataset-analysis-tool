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
    print("Summary:")
    print(df.describe())

def correlation(df):
    return df.corr(numeric_only=True)

def scatter(df,thresh= 0.25):
    print("Correlations:")
    cors = mpp.correlation(df)
    print(cors)

    thresh = 0.25

    mask = np.triu(np.ones(cors.shape), k=1).astype(bool)
    unique_corr = cors.where(mask).stack().reset_index()
    unique_corr.columns = ['V1', 'V2', 'Corr']
    pairs = unique_corr[unique_corr['Corr'] >= thresh]

    print("Correlations over Threshlold:")
    print(pairs)

    width = len(pairs)
    fig, axes = plt.subplots(nrows=1, ncols=width, figsize=(4 * width, 4))

    for i in range(len(pairs)):
        col_x = pairs.iloc[i, 0]
        col_y = pairs.iloc[i, 1]
        df.plot.scatter(x=col_x, y=col_y, ax=axes[i], alpha=0.6)
        axes[i].set_title(f"Scatter:\n {col_x} vs\n {col_y}")
    plt.tight_layout()

def histogram(df):
    cols = df.columns.values.tolist()
    width = len(cols)

    fig, axes = plt.subplots(nrows=1, ncols=width, figsize=(4*width, 4))

    for col, ax in zip(cols, axes):
        df[col].hist(ax=ax)
        ax.set_title(f"Histogram of {col}")
    plt.tight_layout()
