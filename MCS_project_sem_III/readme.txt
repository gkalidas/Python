rtcdb = regretion test center database

writeDict.py
will fetch all p60 related tests from rtcdb

1dictTestNames.csv
conatains all the tests related to p60 from the file test.py


****TestData.csv
there are two ****TestData.csv's normal and retrieval
normalTestData.csv conatains tests with less than two regretion tests performed on it.
retrievalTestData.csv contains tests with more than two regretion tests performed on it.	

statOps.py
reads all p60 related data from ****Testdata.csv
calculate length, mean and all the statistics values needed
stores statistics into a csv named statOps****TestData.csv

scatterPlotAllValues.py
#reads the statOpsNormTestData.csv and stores all values into a dictionary for further usage.
#while storing these values into a dictionary also saves test name and it's mean into a separate lists to plot a scatter diagram.
#once the scatter plot is plotted and if user mouse hovers any one of the tests from the plot, the program will display all the 
#stat values like length, mean, minValue, maxValue, stdDev, median of the test

centroid.py
Will show the centroid for the given data based on segregation of the tests performed by k-means and another algorithms.
