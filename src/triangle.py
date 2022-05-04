from math import sqrt


def triangle_id(sides) -> str:
    """
        pre-condition: sides is a 3-tuple containing three non-negative lengths
        post-condition: returns a string characterizing a triangle with sides of those 3 lengths. Options are:
        invalid
        scalene
        isosceles
        equilateral
        right scalene
        right isosceles
        right equilateral
        :rtype: object
    """
    adjacent, opposite, hypotenuse = sides
    triangle_type = ''
    Pythagorean_theorem = ''

    # Valid Triangle :
    if adjacent <= 0 or opposite <= 0 or opposite <= 0:
        triangle_type = 'invalid'
        return triangle_type
    if adjacent + opposite < hypotenuse or opposite + hypotenuse < adjacent or (adjacent + hypotenuse) < opposite:
        triangle_type = 'invalid'
        return triangle_type

    # Right Triangle:                   
    if hypotenuse ** 2 == opposite ** 2 + adjacent ** 2:
        Pythagorean_theorem = True

    # equilateral property:
    if adjacent == opposite == hypotenuse:
        if Pythagorean_theorem is True:
            triangle_type = 'right equilateral'
        else:
            triangle_type = 'equilateral'
            return triangle_type


    # Isosceles property:

    elif adjacent == opposite or opposite == hypotenuse or adjacent == hypotenuse:
        if hypotenuse == round(opposite * sqrt(2)) or hypotenuse == round(adjacent * sqrt(2)):
            triangle_type = 'right isosceles'
            # Pythagorean_theorem is True
            return triangle_type
        else:
            triangle_type = 'isosceles'

            return triangle_type

    #   Scalene property

    else:
        if Pythagorean_theorem is True:
            triangle_type = 'right scalene'
            return triangle_type
        else:
            triangle_type = 'scalene'

            return triangle_type


def main():
    adjacent = float(input("insert your adjacent side length : "))
    opposite = float(input("insert your opposite side length : "))
    hypotenuse = float(input("insert your hypotenuse side length: "))

    print(triangle_id((adjacent, opposite, hypotenuse)))


if __name__ == '__main__':
    main()
