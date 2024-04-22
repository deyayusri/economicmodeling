import random

from Point import Point


class ColoredPoint(Point): # this class inherits from point
    COLORS = ["red", "blue", "green", "yellow", "purple", "pink", "beige", "bordeaux",
              "marsala", "peach", "turquoise", "saffron", "magenta"]
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color in self.COLORS:
            self.color = color
        else:
            raise Exception(f"That is an invalid color. Accepted colors are {self.COLORS}")

    def __str__(self):
        return f"{self.color}({self.x}, {self.y})"

    @classmethod
    def add_extra_color(cls, color):
        cls.COLORS.append(color)

    @property
    def distance_origin(self):
        result = (self.x**2 + self.y**2)**0.5
        if result == int(result):
            return int(result)
        else:
            return result

# lets creat a list of random 5 numbers
# colored_points = []
# for _ in range(5):
#     colored_points.append(
#         ColoredPoint(random.randint(-100, 100),
#                      random.randint(-100, 100),
#                      random.choice(colors)
#@classmethod is a decorator that is used to define a method within a class as a class method. A class method is a method that is bound to the class itself rather than to instances of the class.
#@property is a built-in decorator that allows you to define methods in a class that can be accessed like attributes. It enables you to define getter, setter, and deleter methods for a class attribute, providing control over how the attribute is accessed, set, and deleted.

# lets create a list of random 5 colored points
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100, 100),
                     random.randint(-100, 100),
                     random.choice(ColoredPoint.COLORS)
                     )
    )

if __name__ == "__main__":
    print(colored_points)
    # lets add orange as an extra color
    ColoredPoint.add_extra_color("orange")
    p2 = ColoredPoint(3, 4, "orange")
    p2.x = 77 # this feels wrong, lets fix it in the child class
    print(p2)
    print(f"p2={p2} and has distance to origin={p2.distance_origin}")

#The code checks if the script is being run directly and not imported as a module.
#It then prints a list of colored points.
#It adds "orange" as an additional color to the colored point class and creates a new colored point object with coordinates (3, 4) and color "orange".
#It changes the x-coordinate of the new point to 77, which is perceived as incorrect, suggesting a need for correction in the child class.
#Finally, it prints the new point's details and its distance from the origin.
