import pytest
from math import sqrt

from vector.vector import Vector


def test_constructor():
    vector = Vector()

    assert vector.x == 0.0
    assert vector.y == 0.0
    assert vector.a == 4.0
    assert vector.b == 10.0


def test_constructor_exceptions():
    with pytest.raises(ValueError):
        Vector('error', 'fail')

    with pytest.raises(TypeError):
        Vector(Vector(), Vector())


def test_setters():
    vector = Vector()

    assert vector.x == 0.0
    assert vector.y == 0.0

    vector.x = -10
    vector.y = 5

    assert vector.x == 6.0
    assert vector.y == 5.0


def test_setters_exceptions():
    vector = Vector()

    with pytest.raises(ValueError):
        vector.x = 'error'

    with pytest.raises(TypeError):
        vector.y = Vector()


def test_operators():
    a = Vector()
    b = Vector(1, 2)

    assert a != b
    assert not a == b


def test_vector_diff():
    a = Vector()
    b = Vector(1, 1)

    assert b.diff(a)
