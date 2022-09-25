# INF 601 Advanced Python Programming
# Fall 2022
# Thomas Kerley
# Mini Project 2
# Due 9/25/2022

import numpy as np
import pandas as pd
import scipy.stats as stats
import os

# Check whether the specified path exists
def existingFile(path):
    # Check whether the specified path exists
    isExist = os.path.exists("Charts/inflationData.csv")
    if isExist:
        print("Existing data file found.")
    else:
        print("File not found.")
    return isExist

# matplotlib scatter 
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')

def removeOutliers(data):
    #find Q1, Q3, and interquartile range for each month
    q1 = np.quantile(data, q=.25, axis="monthly_rate_pct")
    q3 = np.quantile(data, q=.75, axis="monthly_rate_pct")
    iqr = data.apply(stats.iqr)

    #only keep rows in dataframe that have values within 1.5*IQR of Q1 and Q3 monthly
    data_clean = data[~((data < (q1-1.5*iqr)) | (data > (q3+1.5*iqr))).any(axis=1)]

    #find Q1, Q3, and interquartile range for each year
    q1 = data.quantile(q=.25, axis="yearly_rate_pct")
    q3 = data.quantile(q=.75, axis="yearly_rate_pct")
    iqr = data.apply(stats.iqr)

    #only keep rows in dataframe that have values within 1.5*IQR of Q1 and Q3 yearly
    data_clean = data[~((data < (q1-1.5*iqr)) | (data > (q3+1.5*iqr))).any(axis=1)]

    return data_clean