class employee:
    def __init__(self,eno,ename,eactive):
        self.eno=eno            #instance vaiable in a constructor
        self.ename=ename
        self.eactive=eactive

    def instacemethod(self,grade):
        self.grade=grade          #Creating an instance variable within an instance method
        print(f"instance variable in a method {self.grade}")

#creating instance
inst=employee(1,"kiran",True)
print(inst.ename)
print(inst.eno)
inst.instacemethod("a+")


# creating instance variable after creation of object

class dog:
    pass

obj1=dog()
obj1.breed="German shepard"  #variabele outside a class
obj1.color="brown"

#-------------------------------------STATIC VARIABLES---------------------------------------------------------

class CAT:
    species = "Canis familiaris"  # Static variable (class variable)

    def __init__(self, name):
        self.name = name  # Instance variable

    def display_info(self):
        print(f"{self.name} is a {CAT.species}")

# Creating instances of Dog
dog1 = CAT("Buddy")
dog2 = CAT("Max")
print(CAT.species)
print(dog1.species)
print(dog2.species)

#-----------------------------------class method----------------------------------

class Pizza:
   radius=200
   @classmethod
   def get_radius(cls):
       return cls.radius
print(Pizza.get_radius())


#The static methods, in general, utility methods. Inside these methods we won’t use any instance or class variables.
# No arguments like cls or self are required at the time of declaration.

class Demo:
   @staticmethod
   def sum(x, y):
       print(x+y)
   @staticmethod
   def multiply(x, y):
       print(x*y)
Demo.sum(2, 3)
Demo.multiply(2,4)