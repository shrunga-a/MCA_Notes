# python 3 syntax
# single inheritance example

class parent:                  # parent class
    def func1(self):
        print("Hello Parent")

class child(parent):
  # child class
    def func2(self):                 # we include the parent class
        print("Hello Child")   # as an argument in the child
                               # class

test = child()                 # object created
test.func1()                   # parent method called via child object
test.func2()                   # child method called







# multiple inheritance example
class parent1:                     # first parent class
    def func1(self):
        print("Hello Parent1")

class parent2:                     # second parent class
    def func2(self):
        print("Hello Parent2")

class parent3:                     # third parent class
    def func2(self):                     # the function name is same as parent2
        print("Hello Parent3")

class child(parent1, parent2, parent3):     # child class
    def func3(self):                     # we include the parent classes
        print("Hello Child")       # as an argument comma separated

# Driver Code
test = child()        # object created
test.func1()          # parent1 method called via child
test.func2()          # parent2 method called via child instead of parent3
test.func3()          # child method called

# to find the order of classes visited by the child class, we use __mro__ on the child class
print(child.__mro__)




class grandparent:                 # first level
    def func1(self):
        print("Hello Grandparent")

class parent(grandparent):         # second level
    def func2(self):
        print("Hello Parent")

class child(parent):               # third level
    def func3(self):
        print("Hello Child")


test = child()                     # object created
test.func1()                       # 3rd level calls 1st level
test.func2()                       # 3rd level calls 2nd level
test.func3()                       # 3rd level calls 3rd level
