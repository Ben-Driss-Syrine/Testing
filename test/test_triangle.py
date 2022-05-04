from triangle import triangle_id


def test_triangle_id() -> str:
    # Validity
    assert triangle_id((0, 1, 0)) == 'invalid'
    assert triangle_id((0, 0, 0)) == 'invalid'
    assert triangle_id((-8, 9, 0)) == 'invalid'
    # testing Scalene properties
    assert triangle_id((3, 5, 4)) == 'scalene'
    assert triangle_id((3, 4, 5)) == 'right scalene'
    assert triangle_id((8, 3, 6)) == 'scalene'

    # testing equilateral properties
    assert triangle_id((2, 2, 2)) == 'equilateral'
    assert triangle_id((3, 3, 3)) == 'equilateral'
    assert triangle_id((5.2, 5.2, 5.2)) == 'equilateral'
    # Isosceles properties
    assert triangle_id((2, 5, 5)) == 'isosceles'
    assert triangle_id((4.2, 4.2, 5)) == 'isosceles'
    assert triangle_id((5, 5, 7)) == 'right isosceles'
