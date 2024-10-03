#Program 6 2. TITLE: Implement a python program to demonstrate Data visualization with various Types of Graphs using Numpy

#1Line Plot
import matplotlib.pyplot as plt 
import numpy as np
x = np.array([2,4,6,8]) # X-axis points 
y = x*2 # Y-axis points
plt.plot(x, y) # Plot the chart 
plt.show() # display

#Box Plot
import pandas as pd import numpy as np
df = pd.DataFrame(np.random.rand(20,5), columns=['A','B','C','D','E']) 
df.plot.box(grid="True")

#Scatter Plot
from matplotlib import pyplot as plt 

# x-axis values
x = [74, 88, 52, 72, 78]
# Y-axis values
y = [23, 22, 54, 69, 80]

# Function to plot scatter 
plt.scatter(x, y)
# function to show the plot 
plt.show()


#Histogram
from matplotlib import pyplot as plt # Y-axis values
y = [1,15,19,40,65]
# Function to plot histogram plt.hist(y)
# Function to show the plot plt.show()

#HeatMaps
from pandas import DataFrame 
import matplotlib.pyplot as plt 
data=[{8,9,3,4},{4,6,9,1},{7,4,1,3},{9,5,1,3},{7,1,3,9}] 
Index= ['I1', 'I2','I3','I4','I5']
Cols = ['C1', 'C2', 'C3','C4']
df = DataFrame(data, index=Index, columns=Cols) plt.pcolor(df)
plt.show()












End of Program
__________________________________________________________________________________________
Detailed Explanation of concepts:
  


#Line Graph
import pandas as pd
import matplotlib.pyplot as plt
data = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
        'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
       }
df = pd.DataFrame(data)
plt.plot(df['year'], df['unemployment_rate'], color='red', marker='p')
plt.title('unemployment rate vs year', fontsize=14)
plt.xlabel('year', fontsize=14)
plt.ylabel('unemployment rate', fontsize=14)
plt.grid(True)
plt.show()
'''
The Above describe a complete line graph.
fontsize is the attribute that defines the font size of title
xlabel and ylabel are used to define the text labels for x and y axis.
grid(True) is used to draw grids.
df['year'], df['unemployment_rate'] shows the data to be fed to X and Y axis (You can alternatively define list values )
There can be multiple lines.
If you use plt2.plot(list1,list2,color:'green')
'''
#Scatter Plot
import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()
'''Please include title, xlabel, ylabel, color and other attributes to the above Scatter Plot program.
For detailed reference refer.
https://www.w3schools.com/python/matplotlib_scatter.asp
'''

#Bar Graph
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()
#Alternatively we can make use of
#plt.barh(x,y)
#To display the bars horizontally.
#plt.bar(x,y,color="red") color attribute defines the color of the bar graph.
#There are around 140 Accepted colors
#Reference: https://www.w3schools.com/colors/colors_names.asp
'''
plt.bar(x, y, width = 0.1)
Width Attribute is used to define the width of the Bars
plt.barh(x, y, height = 0.1)
Height attribute is used to define the height by default it is 0.8 
'''#Include title, labels and other attributes along with it.

#Box Plot
import matplotlib.pyplot as plt  
import numpy as np  
np.random.seed(10)  
dataSet1 = np.random.normal(100, 10, 220)  
dataSet2 = np.random.normal(80, 20, 200)  
dataSet3 = np.random.normal(60, 35, 220)  
dataSet4 = np.random.normal(50, 40, 200)  
dataSet = [dataSet1, dataSet2, dataSet3, dataSet4]  
figure = plt.figure(figsize =(10, 7))  
ax = figure.add_axes([0, 0, 1, 1])  
bp = ax.boxplot(dataSet)  
plt.show()


#Histogram Graph
'''
A histogram is a graph showing frequency distributions.
It is a graph showing the number of observations within each given interval.
Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
'''
from matplotlib import pyplot as plt
import numpy as np
fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
ax.hist(a, bins = [0,25,50,75,100])
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()

'''
In the above example
Following example plots a histogram of marks obtained by students in a class.
Four bins, 0-25, 26-50, 51-75, and 76-100 are defined.
The Histogram shows number of students falling in this range.
'''
#HeatMaps
from pandas import DataFrame 
import matplotlib.pyplot as plt 
data=[{8,9,3,4},{4,6,9,1},{7,4,1,3},{9,5,1,3},{7,1,3,9}] 
Index= ['I1', 'I2','I3','I4','I5']
Cols = ['C1', 'C2', 'C3','C4']
df = DataFrame(data, index=Index, columns=Cols) plt.pcolor(df)
plt.show()


#Matplotlib Pie charts
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15]) #Percentage out of 100
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 



'''
plt.title("Sports Watch Data", loc = 'left')
loc attribute in title function is used to decide where the title is to be placed.
fontsize is the attribute that defines the font size of title
xlabel and ylabel are used to define the text labels for x and y axis.
grid(True) is used to draw grids.
plt.plot(list1,list2, marker = '*')
There are different Markers in Matplotlib it is used to describe how the points are to be displayed.
Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline


The type of line to be drawn is inserted right after the marker value.
#plt.plot(ypoints, 'o-')
In the above example o is the marker and - represents solid line. 
Line Syntax	Description
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line


#plt.plot(xlist,ylist, 'o-r')
In the above example o is the marker and - represents solid line. r refers to color red.
The color is used to define the line's color. 

Color Syntax	Description
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White

plt.plot(xlist,ylist, marker = 'o', ms = 20, mec = 'r')
ms means the size of the point depicted.

plt.plot(xpoints,ypoints, linestyle = 'dashed')
Alternatively linestyle is an attribute that can be used to define line
The line style can be written in a shorter syntax:
linestyle can be written as ls
'solid' (default)	'-'	
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	'' or ' '
#Example
plt.plot(xpoints,ypoints, ls = ':')

'''
