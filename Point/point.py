import operator


class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __add__(self, other):
        return Point(*map(operator.add, self, other))

    def __sub__(self, other):
        return Point(*map(operator.sub, self, other))

    def __mul__(self, other):
        # return Point(*tuple([x * other for x in self]))
        return Point(*[x * other for x in self])

    __rmul__ = __mul__
