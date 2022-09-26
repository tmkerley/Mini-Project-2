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
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')

# remove outliers from the data set
def removeOutliers(data, arr):
    # calculate the z-value of the data subset
    z = np.abs(stats.zscore(data[arr]))
    # add z value to dataframe
    data["Z-" + arr] = z
    return data[data["Z-" + arr] < 3]    