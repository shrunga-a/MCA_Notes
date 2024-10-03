#Array manipulation, Searching, Sorting and splitting.
import numpy as np
lt = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
 ele = int(input())
 lt.append(ele)
print(lt)
arr=np.array(lt)
arr = np.sort(arr)
print("Sorted Array = ",arr)
ele = int(input("Enter element to search : "))
i = np.where(arr == ele)
print("index = “,i)
s = int(input("Enter spliting value : "))
newarr = np.array_split(arr, s)
print(newarr)
#Broadcasting and Plotting NumPy arrays
# importing the library
import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
x = np.arange(1, 11)
y = np.array([100, 10, 300, 20, 500, 60, 700, 80, 900, 100])
#Alternatively.
#x = np.arange(5, 10)
#y = np.arange(12, 17)
# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="pink")
plt.show()
7. OUTPUT:
#Sorting
Enter number of elements : 5
2 3 14 45 23
[2, 3, 14, 45, 23]
Sorted Array = [ 2 3 14 23 45]
#Searching
Enter element to search : 23 index = (array([3]),)
Enter spliting value : 2
#Splitting
[array([ 2, 3, 14]), array([23, 45])]