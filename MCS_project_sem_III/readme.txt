pandas
regex


1) connect.py - used to connect python to the mysql
2) writeDict.py - will fetch all p60 related tests from rtcdb
3) 

re(regex) module
Python's built-in "re" module provides excellent support for regular expressions, with a modern and complete regex flavor. 
The only significant features missing from Python's regex syntax are atomic grouping, possessive quantifiers, and Unicode properties.
The first thing to do is to import the regexp module into your script with import re.

syntax:
	re.sub(regex, replacement, subject)
Search and Replace
performs a search-and-replace across subject,
replacing all matches of regex in subject with replacement. 
The result is returned by the sub() function. The subject string you pass is not modified.

If the regex has capturing groups, you can use the text matched by the part of the regex inside the capturing group.
To substitute the text from the third group, insert \3 into the replacement string.
If you want to use the text of the third group followed by a literal three as the replacement,
use \g<3>3. \33 is interpreted as the 33rd group. It is an error if there are fewer than 33 groups. 
If you used named capturing groups, you can use them in the replacement text with \g<name>.
The re.sub() function applies the same backslash logic to the replacement text as is applied to the regular expression.
Therefore, you should use raw strings for the replacement text.
The re.sub() function will also interpret \n and \t in raw strings.
If you want c:\temp as a replacement, either use r"c:\\temp" or "c:\\\\temp". The 3rd backreference is r"\3" or "\\3".


1dictTestNames.csv
conatains all the tests related to p60 from the file test.py


rtcdb1 = regretion test center database
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
