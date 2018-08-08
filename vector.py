import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimensions = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v2):
        return self.coordinates == v2.coordinates

    def __add__(self, v2):
        return tuple(map(lambda x: x[1] + v2[x[0]], enumerate(self)))

    def __sub__(self, v2):
        return tuple(map(lambda x: x[1] - v2[x[0]], enumerate(self)))

    def __iter__(self):
        return iter(self.coordinates)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return tuple(map(lambda x: x * other, self))

        raise NotImplemented

    def __rmul__(self, other):
        return self * other

    def __getitem__(self, item):
        return self.coordinates[item]

    def magnitude(self):
        return math.sqrt(sum(map(lambda x: x ** 2, self)))

    def __len__(self):
        return len(self.coordinates)

    def normalise(self):
        if self.is_unit_vector():
            return Vector(self)

        return Vector((1 / self.magnitude()) * self)

    def is_unit_vector(self):
        return self.magnitude() == 1
