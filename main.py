from vector import Vector

if __name__ == "__main__":
    # Addition
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])
    print('{} + {} = {}'.format(v1, v2, v1 + v2))
    print()

    # Subtraction
    v3 = Vector([7.119, 8.215])
    v4 = Vector([-8.223, 0.878])
    print('{} - {} = {}'.format(v3, v4, v3 - v4))
    print()

    # Multiplication
    v5 = 7.41
    v6 = Vector([1.671, -1.012, -0.318])
    print('{} * {} = {}'.format(v5, v6, v5 * v6))
    print()

    # Magnitude
    v7 = Vector([-0.221, 7.437])
    v8 = Vector([8.813, -1.331, -6.247])
    print('||{}|| = {}'.format(v7, v7.magnitude()))
    print('||{}|| = {}'.format(v8, v8.magnitude()))
    print()

    # Normalisation
    v9 = Vector([5.581, -2.136])
    v10 = Vector([1.996, 3.108, -4.554])
    print('1/||{}|| * {} = {}'.format(v9, v9, v9.normalise()))
    print('1/||{}|| * {} = {}'.format(v10, v10, v10.normalise()))
    print()

    # Dot Product
    v11 = Vector([7.887, 4.138])
    v12 = Vector([-8.802, 6.776])
    v13 = Vector([-5.955, -4.904, -1.874])
    v14 = Vector([-4.496, -8.755, 7.103])
    print('{} * {} = {}'.format(v11, v12, v11 * v12))
    print('{} * {} = {}'.format(v13, v14, v13 * v14))
    print()

    # Angle Between
    v15 = Vector([3.183, -7.627])
    v16 = Vector([-2.668, 5.319])
    v17 = Vector([7.35, 0.221, 5.188])
    v18 = Vector([2.751, 8.259, 3.985])
    print('Angle between {} and {} = {}'.format(v15, v16, v15.get_angle_with(v16)))
    print('Angle between {} and {} = {}'.format(v17, v18, v17.get_angle_with(v18, True)))
