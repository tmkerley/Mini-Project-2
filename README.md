# INF 601 Advanced Python Programming
# Fall 2022
# Thomas Kerley
# Mini Project 2
# Due 9/25/2022

The purpose of this project is to explore data frame manipulations with the pandas 
package. Inital test tried to use the faker package to create network data. After 
discovery it would take more work to create fake data for a desired effect, I switch
to using the inflation calculator from API Ninjas.

This should output a scatter plot that shows the difference of monthly vs yearly 
inflation rate of 38 major countries. The histograms show the distribution across
the time periods more clearly. The data shown does have the outliers removed.

As I was trying to clean up outliers of the data, it appeared that the period 
data for each nation would change. I misunderstood some of the data and how it 
was sent to me. Instead of a scatter/histogram, I would have prefered to done inflation
overtime with .head(5) nations. 

Another thing, if the file is already created, the outliers that are removed will get
updated to the smaller set. Hindsight is a pain.