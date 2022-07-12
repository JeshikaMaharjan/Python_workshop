# CONSTRUCTOR

class Animal:
    def __init__(self): #Constructor , first parameter jaile ni self hunu parxa(self equivalent to this object)
        self.name = "Cat"
        self.lifespan = 12

    def print_animal(self):
        print(f"I am a {self.name}")

cat = Animal() #object create
cat.print_animal()

class Animal:
    blood_type = 'Hot'

    def __init__(self, name, lifespan):
        self.name = name
        self.lifespan = lifespan

    def print_animal(self,):
        print(f"I am a {self.name} I will die in {self.lifespan} years")


cat = Animal("Cat", 12)
dog = Animal("Dog", 15)

cat.blood_type = 'Cold'
print(cat.blood_type)
print(dog.blood_type)


cat.print_animal()
print(cat.name)
print(cat.lifespan)

cat={"name":'cat','lifespan':12}
cat['name']
cat.name


class Animal:
    animal_count = 0

    def __init__(self, name, lifespan):
        self.name = name
        self.lifespan = lifespan
        Animal.animal_count += 1

    def print_animal(self,):
        print(f"I am a {self.name} I will die in {self.lifespan} years")


cat = Animal("Cat", 12)
dog = Animal("Dog", 15)

print(cat.animal_count)
print(dog.animal_count)


# Inheritance

class Polygon:
    def __init__(self, number_of_sides):
        self.no_of_sides = number_of_sides

    def how_many_sides_do_i_have(self):
        print(f"I have {self.no_of_sides} sides.")


class Triangle(Polygon): #class child_class(parent_class):

    def __init__(self):
        # Polygon.__init__(self,3)
        super().__init__(3) #calls constructor of base class and psses 3 as argument

    def how_many_sides_do_i_have(self):
        print(f"Ofcourse,,I have {self.no_of_sides} sides.")


poly1 = Polygon(3)
t1 = Triangle()
t1.how_many_sides_do_i_have()
t1.how_many_sides_do_i_have()
print(t1.no_of_sides)

poly1 = Polygon(4)
poly1.how_many_sides_do_i_have()

# Create Rectangle Children class of Polygon
# Should have Length and Breadth property
# Should have a method to print its Area


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__(4)
        self.length = length
        self.breadth = breadth

    def print_my_area(self):
        print(f"My area is {self.length*self.breadth}")

    def __str__(self):
        return f"I am a poly with {self.no_of_sides} sides."


rect1 = Rectangle(2, 3)
rect1.print_my_area()

print(rect1)


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


s1 = Student("Seeru")
print(s1)


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x+other.x, self.y+other.y)

    def _make_me_private(self):
        print("I am private function")
    #


lint = [1, 2, 3, 5, ]
for _, item in enumerate(lint):
    print(item)

coord1 = Coord(1, 2)
coord2 = Coord(3, 2)
coord1._make_me_private()
print(coord1+coord2)