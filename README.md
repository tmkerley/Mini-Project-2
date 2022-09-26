INF 601 Advanced Python Programming
Fall 2022
Thomas Kerley

# Mini Project 2

### Purpose
To explore data frame manipulations with the pandas package. Initial test tried to use the faker package to create network data. After discovery it would take more work to create fake data for a desired effect, I switched to using the inflation calculator from API Ninjas.

This should output a scatter plot that shows the difference of monthly vs yearly 
inflation rate of 38 major countries. The histograms show the distribution across
the time periods more clearly. The data shown does have the outliers removed.

### Third-party Packages

* Matplotlib Version 3.6.0
    install using pip:

        pip install matplotlib

    Support Website:

        https://matplotlib.org/stable/index.html#

* NumPy Version 1.23.0
    install using pip:

        pip install numpy

    Support Website:

        https://numpy.org/

* SciPy Version 1.9.1
    install using pip:

        pip install scipy

    Support Website

        https://docs.scipy.org/doc/scipy/index.html

* pandas Version 1.4.4
    install using pip:

        pip install pandas

    Support Website:

        https://pandas.pydata.org/pandas-docs/stable/index.html

### Notes

As I was trying to clean up outliers of the data, it appeared that the period data for each nation would change. I misunderstood some of the data and how it was sent to me. Instead of a scatter/histogram, I would have prefered to done inflation overtime with .head(5) nations. 

Another thing, if the file is already created, the dataframe/file won't be updated to the latest inflation rates and the outliers that are removed will get updated to a smaller set. Hindsight is a pain.