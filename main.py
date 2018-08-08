from vector import Vector

if __name__ == "__main__":
    # Addition
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])

    # Subtraction
    v3 = Vector([7.119, 8.215])
    v4 = Vector([-8.223, 0.878])

    # Multiplication
    v5 = 7.41
    v6 = Vector([1.671, -1.012, -0.318])

    print('{} + {} = {}'.format(v1, v2, v1 + v2))
    print('{} - {} = {}'.format(v3, v4, v3 - v4))
    print('{} * {} = {}'.format(v5, v6, v5 * v6))