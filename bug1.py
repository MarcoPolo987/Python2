# TODO: there's code missing in one or more lines below
class Base:

    def __init__(self, xx, yy, ssize):
        # TODO: will need to fill this in
        x = xx
        y = y
        size = ssize
        print()

    def draw(self):

        return ""


class Circle(Base):

    def __init__(self, x, y, size):

        super().__init__()

    def draw(self):

        return f"""
        ({self.x}, {self.y})
        {self.size}
        3
        CMPE 131: HW2a: Python
        , - ~ ~ ~ - ,
        , ' ' ,
        , ,
        , ,
        , ,
        , ,
        , ,
        , ,
        , ,
        , , '
        ' - , _ _ _ , '
        """


class Square(Base):

    def draw(self):

        return f"""
        ({self.x}, {self.y})
        {self.size}
        --------------------
        | |
        | |
        | |
        | |
        | |
        | |
        | |
        | |
        --------------------
        """
    # All of the code below is correct


def draw_any_shape(myShape):

    print(myShape.draw())


def main():
    s = Square(1, 2, 3)
    draw_any_shape(s)
    c = Circle(2, 2, 1)
    draw_any_shape(c)


main()
