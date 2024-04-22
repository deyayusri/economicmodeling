# POINT.PY


class Point:
    def __init__(self, x, y):
        """
        this will be called when instantiating an object
        :param x: the value of x
        :param y: the value of y
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        this will return the string value used in printing the point
        :return:
        """
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """
        this is when the point is in a list or other container
        :return:
        """
        return self.__str__()

    def distance_origin(self):
        """
        calculate the distance to origin of  the point
        :return:
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        deifne how a point is greater than another
        :param other: the other point to compare against
        :return:
        """
        return self.distance_origin() > other.distance_origin()

    def __eq__(self, other):
        """
        define when 2 points are equal
        :param other:
        """
        return self.distance_origin() == other.distance_origin()


a = Point(2, 3)
b = Point(7, 9)
c = Point(10, 11)

print(f"a=({a.x}, {a.y})")
print(f"b=({b.x}, {b.y})")
print(f"c=({c.x}, {c.y})")

# creating a list of 5 random numbers
import random


points = []  # initialize an empty list
for _ in range(5):
    x = random.randint(-10, 10)  # Adjust range as needed
    y = random.randint(-10, 10)  # Adjust range as needed
    random_point = Point(x, y)
    points.append(random_point)

for point in points:
    print(f"p({point.x}, {point.y})")

# try to ptint the first point
print("printing a point value", points[0])
print(points)
a = Point(3, 4)
print(f"distance origin a={a.distance_origin()}")
b = Point(5, 12)
print(f"distance origin b={b.distance_origin()}")
print(f"a > b = {a > b}, a < b = {a < b}")

points.sort()
print(f"largest point in the list is {points[-1]}")

#######################################



colors = ["red", "blue", "yellow", "purple", "pink", "beige", "marsala", "peach", "turquoise"]


class ColoredPoint(Point):  # this class inherits from point
    def __int__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"{self.color}({self.x}, {self.y})"


# lets creat a list of random 5 numbers
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(colors)
                     )
    )

print(colored_points)
