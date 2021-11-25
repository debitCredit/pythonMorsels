class Point:

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        sum_z = self.z + other.z
        return Point(sum_x, sum_y, sum_z)

    def __sub__(self, other):
        """Return copy of our point, shifted by other."""
        sum_x = self.x - other.x
        sum_y = self.y - other.y
        sum_z = self.z - other.z
        return Point(sum_x, sum_y, sum_z)

    def __mul__(self, scalar):
        """Return new copy of our point, scaled by given value."""
        x, y, z = self
        return Point(x*scalar, y*scalar, z*scalar)

    __rmul__ = __mul__

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
