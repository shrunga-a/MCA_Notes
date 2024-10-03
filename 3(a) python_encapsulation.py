#Python Encapsulation- Encapsulation means wrapping up of data and its associated functions into a single unit called class.
class car:

    # attributes
        year = 2016     # car model's year
        mpg =  20       # mileage
        speed = 100     # current speed

    # methods
        def accelerate(self):
            return car.speed + 20

        def brake(self):
            return car.speed - 50


car1=car()

car1.accelerate()
120

car1.brake()
50

car1.year
2016

car1.mpg
20

car1.speed
100
class Students:
   def __init__(self, name, rank, points):
      self.name = name
      self.rank = rank
      self.points = points

   # custom function
   def printfunction(self):
      print("I am "+self.name)
      print("I got Rank ",+self.rank)

# create 2 objects
st1 = Students("Gareth Bale", 1, 100)
st2 = Students("Zidane", 2, 90)

# call the functions using the objects created above
st1.printfunction()
st2.printfunction()
