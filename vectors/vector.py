import math


# TODO: Implement TypeErrorss
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
        """
        Checks if two vectors are equal
        :param v2: second vector.
        :return: boolean
        """
        return self.coordinates == v2.coordinates

    def __add__(self, v2):
        return tuple(map(lambda x: x[1] + v2[x[0]], enumerate(self)))

    def __sub__(self, v2):
        """
        Performs subtraction of vectors.
        :param v2: second vector.
        :return: returns sum of the two vectors type vector.
        """
        return tuple(map(lambda x: x[1] - v2[x[0]], enumerate(self)))

    def __iter__(self):
        return iter(self.coordinates)

    def __mul__(self, other):
        """
        Multiplication of vectors.
        :param other: second operand.
        :return: Product of multiplication (may be scalar or vector).
        """
        if isinstance(other, float) or isinstance(other, int):
            return tuple(map(lambda x: x * other, self))

        # ||v1||.||v2||.cosO
        # v1.v2 = v1,1 * v2,1 + ... + v1,n * v2,n
        # Let's us find angle between 2 angles.
        if isinstance(other, Vector):
            return sum([x * y for x, y in zip(self, other)])

    def is_parallel_to(self, v2):
        """
        Parallel if in the same direction or opposite direction.
        :param v2:
        :return:
        """
        return (self.is_zero() or v2.is_zero()
                or self.get_angle_with(v2, True) == 0
                or self.get_angle_with(v2, True) == 180)

    def is_othogonal_to(self, v2):
        """

        :param v2:
        :return:
        """
        pass

    def project_onto(self, b):
        """
        Project this vector onto the basis provided
        :param v: The basis
        :return: Vector projection of this onto b.
        """
        pass

    def is_zero(self):
        return self.magnitude() == 0

    def get_angle_with(self, v2, in_degrees=False):
        """
        Angle between self and v2.
        :param in_degrees:
        :param v2:
        :return:
        """
        # Derived from Dot Product formulae.
        # return math.acos((self * v2) / (self.magnitude() * v2.magnitude()))
        # Couch-Schwarz Inequality
        # - |v1 * v2| <= ||v1|| * ||v2|| NB!!!
        # - Assuming neither v1 and v2 are 0
        # -- if v1 * v2 = ||v1|| * ||v2|| then cosO = 1 (O = 0) and v1 and v2 in same direction.
        # -- if v1 * v2 = -(||v1|| * ||v2||) then cosO = -1 (O = 180) and v1 and v2 in opposite direction.
        # -- if v1 * v2 = 0 then cosO = 0 (O = 90) and v1 and v2 form right angle
        # - v1 * v1 = ||v1|| ** 2 therefore ||v1||=sqrt(v1 * v1)
        # - since O = 0.
        if not in_degrees:
            return math.acos(self.normalise() * v2.normalise())
        else:
            return math.degrees(self.get_angle_with(v2))

    def __rmul__(self, other):
        return self * other

    def __getitem__(self, item):
        return self.coordinates[item]

    def magnitude(self):
        """
        Calculates the magnitude or length of the vector.
        :return: Magnitude (scalar).
        """
        return math.sqrt(sum(map(lambda x: x ** 2, self)))

    def __len__(self):
        return len(self.coordinates)

    def normalise(self):
        """
        Converts current vector to magnitude 1.
        :return: A unit vector (Direction).
        """
        if self.is_unit_vector():
            print('unit!')
            return Vector(self)

        try:
            return Vector((1 / self.magnitude()) * self)

        except ZeroDivisionError:
            raise Exception('Cannot normalise the zero vector')

    def is_unit_vector(self):
        """
        Checks if current vector is unit vector.
        :return: boolean.
        """
        return self.magnitude() == 1

    def is_zero_vector(self):
        """
        Checks if current vector is unit vector.
        :return: boolean
        """
        return self.magnitude() == 0
