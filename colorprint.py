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
