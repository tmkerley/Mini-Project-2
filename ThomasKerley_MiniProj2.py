# INF 601 Advanced Python Programming
# Fall 2022
# Thomas Kerley
# Mini Project 2
# Due 9/25/2022

import requests
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import kerleyFunctions as kf

path = "Charts/inflationData.csv"

# will skip pulling data if the file is already saved. 
# or will download and save a new CSV to reduce API calls
# TODO add an update feature
if kf.existingFile(path):
    infDF = pd.read_csv(path, index_col=0)
else:
    api_url = 'https://api.api-ninjas.com/v1/inflation?'
    response = requests.get(api_url, headers={'X-Api-Key': 'XAnRBGt717T92RQT6/9rig==UD2M9TYjxtSswYLY'})
    if response.status_code == requests.codes.ok:
        infDF = pd.DataFrame(response.json())
        print("Data successfully downloaded")
        infDF.to_csv(path)
    else:
        print("Error:", response.status_code, response.text)

# remove outliers
# infDF = kf.removeOutliers(infDF)

# print stats
infDF.agg({"monthly_rate_pct": ["min", "max", "median", "mean", "std"],
    "yearly_rate_pct": ["min", "max", "median", "mean", "std"]})

# Start with a square Figure.
fig = plt.figure(figsize=(6, 6))
# Add a gridspec with two rows and two columns and a ratio of 1 to 4 between
# the size of the marginal axes and the main axes in both directions.
# Also adjust the subplot parameters for a square plot.
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
# Create the Axes.
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)

# Create a Figure, which doesn't have to be square.
fig = plt.figure(constrained_layout=True)
# Create the main axes, leaving 25% of the figure space at the top and on the
# right to position marginals.
ax = fig.add_gridspec(top=0.75, right=0.75).subplots()
# The main axes' aspect can be fixed.
ax.set(aspect=1)
# Create marginal axes, which have 25% of the size of the main axes.  Note that
# the inset axes are positioned *outside* (on the right and the top) of the
# main axes, by specifying axes coordinates greater than 1.  Axes coordinates
# less than 0 would likewise specify positions on the left and the bottom of
# the main axes.
ax_histx = ax.inset_axes([0, 1.05, 1, 0.25], sharex=ax)
ax_histy = ax.inset_axes([1.05, 0, 0.25, 1], sharey=ax)
# Draw the scatter plot and marginals.
kf.scatter_hist(infDF["monthly_rate_pct"], infDF["yearly_rate_pct"], ax, ax_histx, ax_histy)

# Format the chart and export it to a saved file.
fname = "Charts/Master Chart"
plt.title("Rate of inflation")
plt.xlabel("Monthly Delta")
plt.ylabel("Yearly Delta")
plt.savefig(fname, bbox_inches='tight')