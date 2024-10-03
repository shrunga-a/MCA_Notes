# Python method overloading
'''1. Assigning none as default value to the parameters (parameters = None) and then checking for number of inputs sent
based on which the required statements are to  be executed.'''
class Addition:
    def my_sum(self, a = None, b = None, c = None):
	    s = 0
	    if a != None and b != None and c != None:
			s = a + b + c
		elif a != None and b != None:
			s =  a + b
		return s

obj = Addition()
print(obj.my_sum(10,20))
print(obj.my_sum(10,20,30))







2. Method Overloading in Python Using Multipledispatch
 Multipledispatch is an external module and it has to be pip installed.
 pip3 install Multipledispatch
 Now we need to add function decorator above the function.
'''
@<decorator_name>  # adding the decorator right above the function defition
def function(...):
'''
from multidispatch import dispatch  # importing the module

@dispatch(int, int)  # using the dispatch decorator to define two parameters as int
def mul(a, b):
    return a * b

@dispatch(int, int, int)  # defining 3 parameters as int
def mul(a, b, c):
    return a * b * c

@dispatch(float, float, float)  # defining 3 parameters as float
def mul(a, b, c):
    return a * b * c

print(mul(2.1, 3.4, 5.6))
print(mul(3, 4))
print(mul(2, 3, 4))
