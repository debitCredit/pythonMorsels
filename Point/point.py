class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        sum_z = self.z + other.z
        return Point(sum_x, sum_y, sum_z)

    def __sub__(self, other):
        sum_x = self.x - other.x
        sum_y = self.y - other.y
        sum_z = self.z - other.z
        return Point(sum_x, sum_y, sum_z)

    def __mul__(self, value):
        mul_x = self.x * value
        mul_y = self.y * value
        mul_z = self.z * value
        return Point(mul_x, mul_y, mul_z)

    __rmul__ = __mul__

    def __iter__(self):
        return iter((self.x, self.y, self.z))
