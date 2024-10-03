# to start with, we will need
from matplotlib import pyplot
import numpy
i = 5
#NumPy to generate random numbers from 10 to 90 into a array of shape 4,5
a=numpy.random.randint(10,90,(4,5))
#To display the array
print(a)
#save it to a text file.
numpy.savetxt("filename.csv", a, delimiter=",")
#To display the shape of the array.
a.shape
#To reshape the array
a.reshape(5,4)
#To display individual item size in bytes.
x.itemsize
#To display the data type of array
x.dtype 


# Plotting the NumPy array using Line graph.
import matplotlib.pyplot as plt
import numpy as np
# Creating a new figure
plt.figure(dpi=100)
# Creating an array from the list
# Plotting Numpy array
plt.plot(a)
# Adding details to the plot
plt.title('Line Plot of a NumPy Array')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# Displaying the plot
plt.show() 
